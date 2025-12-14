from scraper import scrape
from format import formatText
from mailer import sendMail
import config

def main():
    text = scrape()
    formatted_text = formatText(text)
    sendMail(formatted_text)

    print(f"Email successfully sent to {config.RECEPIENT}")


if __name__ == "__main__":
    main()