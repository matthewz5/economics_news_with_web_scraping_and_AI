import requests # type: ignore
from bs4 import BeautifulSoup, Tag # type: ignore

def get_content(url):

    content = requests.get(
        url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'}
    ).text

    return BeautifulSoup(content, 'html.parser')

def scrap_data(soup):

    news = []

    for a_tag in soup.find_all('a', href=True):

        title = a_tag.get_text(strip=True)

        link = a_tag['href']
        
        if title and len(title) >= 30:

            if not link.startswith('http'):

                link = f'https://www.suno.com.br{link}'

            try:

                news_soup = get_content(link)
                
                time_element = news_soup.find('time', itemprop='datePublished')

                if time_element and 'datetime' in time_element.attrs:

                    publish_date = time_element.get('datetime', '')[:10]

                else:
                    publish_date = None

                paragraphs = news_soup.find_all('p')

                full_text = "\n".join(
                    "".join(
                        element.get_text(strip=True) + " " if isinstance(element, Tag) else element
                        for element in paragraph.contents
                    ).strip()
                    for paragraph in paragraphs[2:-8]
                )
                
                news.append({'Title': title, 'URL': link, 'Publish Date': publish_date, 'Full Text': full_text})

            except requests.RequestException as e:
                print(f"Erro ao acessar {link}: {e}")

    return news