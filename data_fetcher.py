import requests
import feedparser
from config import ARXIV_URL, DEFAULT_PARAMS

def fetch_papers(category='cs.LG'):
    base_url = "http://export.arxiv.org/api/query?"
    search_query = f'cat:{category}'
    start = 0
    max_results = 10
    query = f"search_query={search_query}&start={start}&max_results={max_results}"
    url = base_url + query
    response = requests.get(url)
    feed = feedparser.parse(response.content)
    return feed.entries
