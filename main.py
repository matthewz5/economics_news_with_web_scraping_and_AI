from src.config import URL, API_KEY, NEWS_EXCEL_PATH, SUMMARY_MD_PATH
from src.data_collection import get_content, scrap_data
from src.data_processing import process_news_data
from src.summarizer_ai import summarize_news
from src.send_email import send_email

print("Scraping news...")
soup = get_content(URL)
news = scrap_data(soup)

print("Processing data...")
df = process_news_data(news, NEWS_EXCEL_PATH)

print("Summarizing news...")
summary = summarize_news(df, API_KEY, SUMMARY_MD_PATH)

print("Sending news email...")
send_email(f"Resumo de notícias econômicas semanal SUNO", "mail here", summary.text)
