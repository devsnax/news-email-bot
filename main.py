import os
import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage

## Headline + summary scraping
url = "https://www.bbc.com/news/world"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

headlines = soup.find_all("h2", attrs={"data-testid": "card-headline"})
summaries = soup.find_all("p")

html_items = ""

## Mail Formatting
for headline, summary in zip(headlines, summaries):
    html_items += f"""
                    <div style="margin-top: 20px; border-bottom: 1px solid #ccc; padding-bottom: 10px;">
                        <h2 style="margin: 0; font-size: 20px; font-weight: bold;">{headline.text}</h2>
                            <p style="font-size: 15px;">{summary.text}</p>\n
                    </div>
                  """

html = f"""
            <html>
                <body style="font-family: Arial, sans-serif;">
                    <h1>BBC Daily World News</h1>\n
                        <p>Daily news summaries scraped using Python</p>\n
                        {html_items}
                    <p style="margin-top: 40px;">Scraped daily, built by Snax.</p>
                </body>
            </html>
        """


## Mail contecnt
sender_email = os.environ["EMAIL_SENDER"]
recepient = os.environ["EMAIL_RECEIVER"]
subject = "My Daily World News Scraped from BBC"

mail = EmailMessage()
mail["From"] = sender_email
mail["To"] = recepient
mail["Subject"] = subject
mail.add_alternative(html, subtype="html")

## Smtp server
smtp_server = "smtp.gmail.com"
port = 587
smtp_passwd = os.environ["SMTP_PASSWORD"]

server = smtplib.SMTP(smtp_server, port)
server.starttls()
server.login(sender_email, smtp_passwd)

server.sendmail(sender_email, recepient, mail.as_string())

print("Daily News sent successfully!\n")