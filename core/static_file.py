import requests
from core.utils import *
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs

# initialize a session
session = requests.Session()
# set the User-agent as a regular browser
session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

# get the JavaScript files
def js_files(url):
	# get the HTML content
	html = session.get(url).content

	# parse HTML using beautiful soup
	soup = bs(html, "html.parser")

	total_files = 0

	for script in soup.find_all("script"):
		if script.attrs.get("src"):
			script_url = urljoin(url, script.attrs.get("src"))
			total_files += 1

			print(script_url)
	
	print("-" * 50)
	print(f"Total script files in the page: {total_files}")

def css_files(url):
	# get the HTML content
	html = session.get(url).content

	# parse HTML using beautiful soup
	soup = bs(html, "html.parser")

	total_files = 0
	
	for css in soup.find_all("link"):
		if css.attrs.get("href"):
			css_url = urljoin(url, css.attrs.get("href"))

			if css_url.find(".css") != -1:
				total_files += 1
				print(css_url)
	
	print("-" * 50)
	print(f"Total CSS files in the page: {total_files}")
	
def images_files(url):
	# get the HTML content
	html = session.get(url).content

	# parse HTML using beautiful soup
	soup = bs(html, "html.parser")

	total_files = 0
	
	for img in soup.find_all("img"):
		img_url = urljoin(url, img.attrs.get("src"))

		total_files += 1
		print(img_url)
	
	print("-" * 50)
	print(f"Total Images files in the page: {total_files}")

def test(url):
	# get the HTML content
	html = session.get(url).content

	# parse HTML using beautiful soup
	soup = bs(html, "html.parser")

	total_files = 0
	
	for img in soup.find_all("img"):
		img_url = urljoin(url, img.attrs.get("src"))

		total_files += 1
		print(img_url)
	
	print("-" * 50)
	print(f"Total Images files in the page: {total_files}")