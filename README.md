## Description

The project code realize web scraping on [Suno Notícias](https://www.suno.com.br/noticias/), collecting the:

- **News title**,
- **Link**,
- **Publish date**,
- **Full text**.

The [Google Gemini model with API 1.5 Flash](https://ai.google.dev/gemini-api/docs?hl=pt-br) are used to receive the news title and full text to generate a economic's news summary, following the prompt:

- "Dadas as seguintes notícias, por favor, forneça um resumo geral separado por: MACROECONOMIA; AÇÕES; FIIS; INTERNACIONAL; DEMAIS."

## Results

Here the data collected and treated: [click here](data/news.xlsx)

Here the summary economoics news: [click here](data/summary.md)

## Folder Structure
- `src/`: Source code modules.
- `references/`: Contains the original script.
- `data/`: Stores generated outputs.

## Credits
This project builds upon the initial work of [@cientistadabolsa](https://www.instagram.com/cientistadabolsa/) from the 2024 masterclass in "Laboratório da Bolsa".
