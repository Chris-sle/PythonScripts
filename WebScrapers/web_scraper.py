import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL for the quotes site
base_url = 'https://quotes.toscrape.com'

# Function to scrape quotes from a given page URL
def scrape_quotes_from_page(url):
    # Send a GET request to the page URL
    response = requests.get(url)
    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = []  # List to store quotes from the current page
    
    # Extract individual quotes and their authors
    for quote in soup.find_all('div', class_='quote'):
        # Extract quote text
        text = quote.find('span', class_='text').text.strip()
        # Extract the author of the quote
        author = quote.find('small', class_='author').text.strip()
        # Extract the tags associated with the quote
        quote_tags = [tag.text for tag in quote.find_all('a', class_='tag')]
        
        # Append the quote details as a dictionary to the list
        quotes.append({'Quote': text, 'Author': author, 'Tags': ', '.join(quote_tags)})
    
    return quotes  # Return the list of quotes from the page

# Get all available tags from the homepage
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the section containing tags
tags_section = soup.find('div', class_='tags-box')
# Extract the text of each tag and store in a list
tags = [a.text for a in tags_section.find_all('a', class_='tag')]

all_quotes = []  # List to store all quotes from all tag pages

# Iterate over each tag and scrape quotes
for tag in tags:
    # Construct the URL for each specific tag
    tag_url = f"{base_url}/tag/{tag}"
    print(f"Scraping quotes for tag: {tag}")
    
    page_number = 1  # Initialize page number for pagination
    while True:
        # Construct the URL for each page of the tag
        url = f"{tag_url}/page/{page_number}/"
        # Scrape quotes from the current page
        quotes = scrape_quotes_from_page(url)
        
        if not quotes:
            # If no quotes are found, break the loop (end of pagination)
            break
        
        # Add the quotes from this page to the main list
        all_quotes.extend(quotes)
        page_number += 1  # Increment page number to move to the next page

# Create a Pandas DataFrame from the list of quotes
df = pd.DataFrame(all_quotes)
# Save the DataFrame to a CSV file, without including the index
df.to_csv('quotes_by_tags.csv', index=False, encoding='utf-8')

print("Quotes have been saved to 'quotes_by_tags.csv'.")