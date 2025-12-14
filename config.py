import os
import smtplib

URL = "https://www.bbc.com/news/world"
SENDER_MAIL = os.environ["EMAIL_SENDER"]
RECEPIENT = os.environ["EMAIL_RECEIVER"]
SUBJECT = "My Daily World News Scraped from BBC"

SMTP_SERVER = "smtp.gmail.com"
PORT = 587
SMTP_PASSWD = os.environ["SMTP_PASSWORD"]

SERVER = smtplib.SMTP(SMTP_SERVER, PORT)