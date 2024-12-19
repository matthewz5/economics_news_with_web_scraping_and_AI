
This project is developed based on an initial solution by [@cientistadabolsa](https://www.instagram.com/cientistadabolsa/) presented in his 2024 masterclass for the course "Laboratório da Bolsa", [click here]().

[...]

The improvements include adding more robust web scraping, which collects the:

- **News title**,
- **Link**,
- **Publish date**,
- **Full text**.

The [Google Gemini model with API 1.5 Flash](https://ai.google.dev/gemini-api/docs?hl=pt-br) are used to receive the news title and full text to generate a economic's news summary, following the prompt:

- "Dadas as seguintes notícias, por favor, forneça um resumo geral separado por: MACROECONOMIA; AÇÕES; FIIS; INTERNACIONAL; DEMAIS."

[...]