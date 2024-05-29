import requests
from bs4 import BeautifulSoup
import re

def scrape_wiki_page(url, output_file):
    """
    Scrapes a Wikipedia page, removes links and references, and saves the text.

    Args:
        url: The URL of the Wikipedia page to scrape.
        output_file: The path to the output text file.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all headings and paragraphs
    text_blocks = soup.find_all(['h2', 'h3', 'h4', 'h5', 'h6', 'p'])

    # Clean each block
    cleaned_text = []
    for block in text_blocks:
        # Remove internal links
        for link in block.find_all('a'):
            link.replace_with(link.text)
        # Remove references section entirely
        if block.name == 'sup':
            block.extract()
        cleaned_text.append(block.text.strip())

    # remove references like example [13] or [citation needed] or [c]
    cleaned_text = [re.sub(r'\[\d+\]', '', block) for block in cleaned_text]

    # Join cleaned blocks and save to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(cleaned_text))

    cleaned_text = '\n'.join(cleaned_text)

    return cleaned_text

#  test
url = "https://en.wikipedia.org/wiki/Luke_Skywalker"
output_file = "test_cleaned_text.txt"
text = scrape_wiki_page(url, output_file)