# IMPORTAÇÃO DE BIBLIOTECAS

import pandas as pd
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup, Tag
import google.generativeai as genai

# COLETA DOS DADOS

url = 'https://www.suno.com.br/noticias/'

print('='*60, '\n', f'Iniciando coleta de dados \n de {url}', '\n', '='*60)

conteudo_site = requests.get(
    url,
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'}
).text

soup = BeautifulSoup(conteudo_site, 'html.parser')

news = []

for a_tag in soup.find_all('a', href=True):

    # coleta do titulo
    title = a_tag.get_text(strip=True)
    # coleta do link
    link = a_tag['href']
    
    if title and len(title) >= 30:

        if not link.startswith('http'):
            link = f'https://www.suno.com.br{link}'

        # coleta da data
        news_page = requests.get(
            link,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'}
        ).text

        news_soup = BeautifulSoup(news_page, 'html.parser')
        
        time_element = news_soup.find('time', itemprop='datePublished')

        if time_element and 'datetime' in time_element.attrs:
            publish_date = time_element.get('datetime', '')[:10]

        else:
            publish_date = None

        # coleta do conteúdo
        paragraphs = news_soup.find_all('p')

        full_text = "\n".join(
            "".join(
                element.get_text(strip=True) + " " if isinstance(element, Tag) else element
                for element in paragraph.contents
            ).strip()
            for paragraph in paragraphs[2:-8]
        )
        
        news.append({'Title': title, 'URL': link, 'Publish Date': publish_date, 'Full Text': full_text})

# TRATAMENTO DOS DADOS

print('='*60, '\n', f'Iniciando tratamento dos dados', '\n', '='*60)

df_news = pd.DataFrame(news)

duplicates = df_news[df_news.duplicated(subset='Title', keep='first')]

if not duplicates.empty:
    print("Notícias duplicadas removidas:")
    print(duplicates)

df_news = df_news.drop_duplicates(subset='Title', keep='first').reset_index(drop=True)

df_news = df_news.dropna()

df_news['Publish Date'] = pd.to_datetime(df_news['Publish Date'], errors='coerce')

df_news = df_news.drop(df_news[(df_news['Publish Date'].isna()) | (df_news['Publish Date'] <= pd.to_datetime(datetime.now().date() - timedelta(days=6)))].index).reset_index(drop=True)

df_news.sort_values(by='Publish Date', ascending=False)

# MOSTRA DOS DADOS

print('='*60, '\n', f'Notícias coletadas', '\n', '='*60)

for id, row in df_news.iterrows():

    print('-'*60, '\n')
    print(row['Title'], '-', row['Publish Date'].strftime('%d/%m/%Y'))
    print('Link:', row['URL'])
    print(row['Full Text'])
    print('\n', '-'*60)

# RESUMO VIA GOOGLE GEMINI

list_news = list(df_news['Title'])
text_news = list(df_news['Full Text'])

genai.configure(api_key="AIzaSyAAKQ_j3hHwcFS4T0-TzDcbUW4QEv_5sZM")

model = genai.GenerativeModel("gemini-1.5-flash")

prompt = f"Dadas as seguintes notícias, por favor, forneça um resumo geral separado por: MACROECONOMIA; AÇÕES; FIIS; INTERNACIONAL; DEMAIS".join(list_news).join(text_news)

response = model.generate_content(prompt)

print('='*60, '\n', f'Resumo via Google Gemini 1.5 Flash', '\n', '='*60)

print(response.text)

print('='*60, '\n', f'... Obrigado', '\n', '='*60)