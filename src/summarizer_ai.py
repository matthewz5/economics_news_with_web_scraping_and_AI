import google.generativeai as genai # type: ignore

def summarize_news(df, api_key):

    genai.configure(api_key=api_key)

    prompt = "Dadas as seguintes notícias, por favor, forneça um resumo geral separado por: MACROECONOMIA; AÇÕES; FIIS; INTERNACIONAL; DEMAIS\n"

    for title, text in zip(list(df['Title']), list(df['Full Text'])):
        
        prompt += f"Título: {title}\nTexto: {text}\n\n"

    model = genai.GenerativeModel("gemini-1.5-flash")

    return model.generate_content(prompt)