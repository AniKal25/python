import requests
from bs4 import BeautifulSoup

def fetch_and_parse(url):
    # Fetch the page
    response = requests.get(url)
    if response.status_code != 200:
        return "Failed to retrieve the website"

    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract title and canonical link
    title = soup.find('title')
    canonical = soup.find('link', {'rel': 'canonical'})

    # Print the results
    title_text = title.text if title else "No title found"
    canonical_link = canonical['href'] if canonical else "No canonical link found"

    return title_text, canonical_link

# URL to be parsed
url = 'https://en.wikipedia.org/wiki/Aari_language'
title, canonical = fetch_and_parse(url)
print("Title:", title)
print("Canonical link:", canonical)


