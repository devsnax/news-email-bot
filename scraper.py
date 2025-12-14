import requests
from bs4 import BeautifulSoup

import config

def scrape():
    url = config.URL
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    headlines = soup.find_all("h2", attrs={"data-testid": "card-headline"})
    summaries = soup.find_all("p")

    results = []
    for headline, summary in zip(headlines, summaries):
        results.append((headline, summary))

    return results