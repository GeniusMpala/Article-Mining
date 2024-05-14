import requests
import feedparser

# Define the URL template to fetch papers from specific categories
base_url = "http://export.arxiv.org/api/query?"

# Search query parameters
search_query = 'cat:cs.LG+OR+cat:quant-ph'  # search for machine learning and quantum computing papers
start = 0                                   # start at the first result
max_results = 10                            # retrieve 10 results at a time

query = f"search_query={search_query}&start={start}&max_results={max_results}"

# Complete URL
url = base_url + query

# Send a GET request to the API
response = requests.get(url)

# Parse the response using feedparser
feed = feedparser.parse(response.content)

# Print the titles and summary of each entry
for entry in feed.entries:
    print('Title:', entry.title)
    print('Authors:', ', '.join(author.name for author in entry.authors))
    print('Published:', entry.published)
    print('Summary:', entry.summary)
    print('Link:', entry.link)
    print('\n')
