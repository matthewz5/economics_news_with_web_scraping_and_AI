from src.config import URL, API_KEY
from src.data_collection import get_content, scrap_data
from src.data_processing import process_news_data
from src.summarizer_ai import summarize_news

print("Scraping news...")
soup = get_content(URL)
news = scrap_data(soup)

print("Processing data...")
df = process_news_data(news)

print("Summarizing news...")
summary = summarize_news(df, API_KEY)

print(summary.text)

