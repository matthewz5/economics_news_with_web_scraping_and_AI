import win32com.client

def send_email(subject, email_to, text):

    try:
        outlook = win32com.client.Dispatch("Outlook.Application")
        mail = outlook.CreateItem(0)
    except Exception as e:
        print(f"Error on create e-mail in Outlook: {e}")

    formatted_text = text.replace("##", "<h1>").replace("**", "<strong>").replace("*", "<p>").replace("\n", "<br>")

    html_body = f"""
    <html>
    <head>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
        }}
        h1 {{
            color: #000000;
            font-size: 24px;
            margin-bottom: 20px;
        }}
        strong {{
            font-weight: bold;
        }}
        p {{
            font-size: 14px;
            margin: 10px 0;
        }}
    </style>
    </head>
    <body>
        {formatted_text}
        <div style="margin-top: 30px; font-size: 12px; color: #666;">
            <p>Mensagem automática gerada pelo sistema.</p>
        </div>
    </body>
    </html>
    """

    mail.Subject = subject
    mail.To = email_to
    mail.HTMLBody = formatted_text

    try:
        mail.Send()
        print("Success!")
    except Exception as e:
        print(f"Error on sending: {e}")