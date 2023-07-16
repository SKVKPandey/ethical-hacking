import requests
from bs4 import BeautifulSoup
from scrapy import Selector

# Define the target URL
url = 'https://www.arsdcollege.ac.in/'

# Send a GET request to the target URL
response = requests.get(url)

# Check the HTTP response status code
if response.status_code == 200:
    print('Website is reachable')

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract specific information from the HTML using BeautifulSoup
    title = soup.title.text.strip()
    print('Website Title:', title)

    # Use scrapy Selector to perform more advanced parsing
    selector = Selector(text=response.text)

    # Example: Extract all the links on the page using xpath
    links = selector.xpath('//a/@href').getall()
    print('Links on the page:')
    for link in links:
        print(link)

else:
    print('Website is not reachable or encountered an error')
