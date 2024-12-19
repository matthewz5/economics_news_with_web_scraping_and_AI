import justext
import requests

# Realiza uma consulta ao site e obtém seu conteúdo
conteudo_site = requests.get(
    'https://www.suno.com.br/noticias/',
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'}
).text

# Lista de notícias
news = []
texts = justext.justext(conteudo_site, justext.get_stoplist('Portuguese'))
for paragraph in texts:
    txt = paragraph.text
    if len(txt) >= 50:
        news.append(txt)

for n in news[:15]:
    print(n)