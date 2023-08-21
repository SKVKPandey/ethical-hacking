import requests
from bs4 import BeautifulSoup
from scrapy import Selector
from urllib.parse import urlparse, urljoin

# Define the target URL
url = 'https://www.arsdcollege.ac.in/'

# Function to recursively retrieve links
def retrieve_links(url, depth):
    # Send a GET request to the target URL
    response = requests.get(url)

    # Check the HTTP response status code
    if response.status_code == 200:
        print(f"\nDepth {depth} - Links on {url}:")

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Use scrapy Selector to perform more advanced parsing
        selector = Selector(text=response.text)

        # Example: Extract all the links on the page using xpath
        links = selector.xpath('//a/@href').getall()
        for link in links:
            # Resolve relative URLs
            absolute_url = urljoin(url, link)

            # Skip invalid URLs
            if urlparse(absolute_url).scheme == '':
                continue

            print(absolute_url)

            # Recursively retrieve links from the nested links
            if depth > 1:
                retrieve_links(absolute_url, depth - 1)
    else:
        print(f"\nDepth {depth} - Website {url} is not reachable or encountered an error")


# Define the depth for recursive retrieval
depth = 3

# Call the function to retrieve links
retrieve_links(url, depth)
