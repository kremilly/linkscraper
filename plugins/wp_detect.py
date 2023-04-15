#!/usr/bin/python3

import requests
from utils.utils import *
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs
from rich.console import Console

session = requests.Session()
console = Console(record=True)
session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

def wp_generator(url):
    soup = bs(requests.get(url).text, "html.parser")

    metas = soup.find_all('meta')
    return [ 
	    meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'generator' 
	]

def plugin_wp_detect(url):
	soup = bs(session.get(url).content, "html.parser")

	wp_detected = False
	wp_version = "[italic cyan]WordPress unknown[/italic cyan]"
	wp_meta_generator = wp_generator(url)

	if len(wp_meta_generator) >= 1 and find(wp_meta_generator[0], "WordPress"):
		wp_detected = True
		wp_version = wp_meta_generator[0]
	else:
		for css in soup.find_all("link"):
			if css.attrs.get("href"):
				css_url = urljoin(url, css.attrs.get("href"))

				if find(css_url, "wp-content") or find(css_url, "wp-includes"):
					wp_detected = True
				else:
					wp_detected = False
				break

	if wp_detected:
		console.print(f"[bold green]WordPress: detected[/bold green]")
		console.print(wp_version.replace("WordPress ", "WordPress version: "))
	else:
		console.print(f"[bold red]WordPress: not detected[/bold red]")
