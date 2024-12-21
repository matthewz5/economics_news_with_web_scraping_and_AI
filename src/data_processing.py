import pandas as pd # type: ignore
from datetime import datetime, timedelta

def process_news_data(news):

    df = pd.DataFrame(news)

    df = df.drop_duplicates(subset='Title', keep='first').reset_index(drop=True)

    df = df.dropna()

    df['Publish Date'] = pd.to_datetime(df['Publish Date'], errors='coerce')

    df = df.drop(df[(df['Publish Date'].isna()) | (df['Publish Date'] <= pd.to_datetime(datetime.now().date() - timedelta(days=6)))].index).reset_index(drop=True)

    df.sort_values(by='Publish Date', ascending=False)

    return df