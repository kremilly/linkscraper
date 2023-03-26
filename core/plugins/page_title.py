import requests
from bs4 import BeautifulSoup as bs

def plugin_page_title(url):
    reqs = requests.get(url)

    soup = bs(reqs.text, 'html.parser')
    
    for title in soup.find_all('title'):
        return title.get_text()