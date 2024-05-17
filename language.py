import requests
from bs4 import BeautifulSoup

def fetch_and_parse(url):
    # Fetch the page
    response = requests.get(url)
    if response.status_code != 200:
        return (url, "Failed to retrieve the website", None)

    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract title and canonical link
    title = soup.find('title')
    canonical = soup.find('link', {'rel': 'canonical'})

    # Return the results
    title_text = title.text if title else "No title found"
    canonical_link = canonical['href'] if canonical else "No canonical link found"

    return (url, title_text, canonical_link)

# List of URLs to be parsed
urls = [
'https://www.finra.org/investors/professional-designations/c3dwp',
'https://www.finra.org/investors/professional-designations/krs',
'https://www.finra.org/investors/professional-designations/aai',
'https://www.finra.org/investors/professional-designations/aams',
'https://www.finra.org/investors/professional-designations/abfp',
'https://www.finra.org/investors/professional-designations/abs',
'https://www.finra.org/investors/professional-designations/adpa',
'https://www.finra.org/investors/professional-designations/aep',
'https://www.finra.org/investors/professional-designations/afa',
'https://www.finra.org/investors/professional-designations/afc'

    
]

# Loop through the list of URLs and fetch/parse each one
results = []
for url in urls:
    result = fetch_and_parse(url)
    results.append(result)

# Print results
for result in results:
    
    print(f"URL: {result[0]}")
    print(f"Title: {result[1]}")
    print(f"Canonical Link: {result[2]}")
    print()  # Just to add a space between each result for clarity
