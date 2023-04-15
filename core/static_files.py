#!/usr/bin/python3

import requests, time

from core.http import *
from utils.utils import *
from utils.utils_files import *
from core.download_files import *

from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs

from rich.table import Table
from rich.console import Console

session = requests.Session()
console = Console(record=True)
session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

def js_files(url, minify_files, filter_data, download):
    if download == "true":
        download_js(url, minify_files, filter_data)
    else:
        start_time = time.time()
        html = session.get(url).content
        soup = bs(html, "html.parser")
        
        table = Table(box=None)
        table.add_column("Filename", style="cyan")
        table.add_column("URL", style="bold green")

        links = []
        total_files = 0
        
        for script in soup.find_all("script"):
            if script.attrs.get("src"):
                script_url = urljoin(url, script.attrs.get("src"))
                
                if filter_data:
                    if find(script_url, filter_data):
                        links.append(script_url)
                else:
                    if minify_files == "true":
                        if find(script_url, '.min'):
                            links.append(script_url)
                    else:
                        links.append(script_url)
                
        for script_url in list(set(links)):
            table.add_row(getRemoteFileName(script_url), script_url)
            total_files += 1
        
        end_time = "{:.2f}".format(time.time() - start_time)
        
        table.caption = f"Total script files on page: {total_files} - Time taken: {end_time} seconds"
        console.print(table)

def css_files(url, minify_files, filter_data, download):
    if download == "true":
        download_css(url, minify_files, filter_data)
    else:
        start_time = time.time()
        html = session.get(url).content
        soup = bs(html, "html.parser")
        
        table = Table(box=None)
        table.add_column("Filename", style="cyan")
        table.add_column("URL", style="bold green")

        links = []
        total_files = 0
        
        for css in soup.find_all("link"):
            if css.attrs.get("href"):
                css_url = urljoin(url, css.attrs.get("href"))

                if filter_data:
                    if find(css_url, ".css") and find(css_url, filter_data):
                        links.append(css_url)
                else:
                    if minify_files == "true":
                        if find(css_url, ".css") and find(css_url, ".min.css"):
                            links.append(css_url)
                    else:
                        if find(css_url, ".css"):
                            links.append(css_url)
                    
        for css_url in list(set(links)):
            table.add_row(getRemoteFileName(css_url), css_url)
            total_files += 1
        
        end_time = "{:.2f}".format(time.time() - start_time)
        
        table.caption = f"Total CSS files on page: {total_files} - Time taken: {end_time} seconds"
        console.print(table)
    
def images_files(url, filter_data, download):
    if download == "true":
        download_images(url, filter_data)
    else:
        start_time = time.time()
        html = session.get(url).content
        soup = bs(html, "html.parser")
        
        table = Table(box=None)
        table.add_column("Filename", style="cyan")
        table.add_column("URL", style="bold green")

        links = []
        total_files = 0
        
        for img in soup.find_all("img"):
            img_url = urljoin(url, img.attrs.get("src"))
            
            if filter_data:
                if find(img_url, filter_data):
                    links.append(img_url)
            else:
                links.append(img_url)
    
        for img_url in list(set(links)):
            table.add_row(getRemoteFileName(img_url), img_url)
            total_files += 1       
        
        end_time = "{:.2f}".format(time.time() - start_time)
        
        table.caption = f"Total images files on page: {total_files} - Time taken: {end_time} seconds"
        console.print(table)
