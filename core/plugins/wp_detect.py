import requests
from core.utils import *
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs

# initialize a session
session = requests.Session()
# set the User-agent as a regular browser
session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

def plugin_wordpress_detect(url):
	# get the HTML content
	html = session.get(url).content

	# parse HTML using beautiful soup
	soup = bs(html, "html.parser")
	
	for css in soup.find_all("link"):
		if css.attrs.get("href"):
			css_url = urljoin(url, css.attrs.get("href"))

			if css_url.find("wp-content") != -1:
				print("WordPress: detected")
			else:
				print("WordPress: not detected")
			break