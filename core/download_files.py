#!/usr/bin/python3

import os, requests, time

from core.http import *
from utils.utils_files import *

from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs

from rich.table import Table
from rich.console import Console

session = requests.Session()
console = Console(record=True)
session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

def download_js(url, minify_files, filter_data):
    start_time = time.time()
    domain = get_hostname(url)
    
    html = session.get(url).content
    soup = bs(html, "html.parser")

    links = []
    total_files = 0
    path = f"download/{domain}/js/"
    
    table = Table(box=None)
    table.add_column("Filename", style="cyan")
    table.add_column("URL", style="bold green")
    table.add_column("Size", style="blue")
    table.add_column("Status")
    
    createFolder(path)
    
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
        text = requests.get(script_url).text
        file_name = path + getRemoteFileName(script_url)
        
        with open(file_name, 'w', encoding="utf-8") as f:
            f.write(text)
            
        total_files += 1
        
        if os.path.exists(file_name):
            table.add_row(getRemoteFileName(script_url), script_url, localFileSize(file_name), "[bold green]Download completed[/bold green]")
        else:
            table.add_row(getRemoteFileName(script_url), script_url, localFileSize(file_name), "[bold red]Download failed[/bold red]")
    
    path = os.path.realpath(path)
    os.startfile(path)

    end_time = "{:.2f}".format(time.time() - start_time)
    
    table.caption = f"Total of downloaded files: {total_files} - Time taken: {end_time} seconds"
    console.print(table)
    
def download_css(url, minify_files, filter_data):
    start_time = time.time()
    domain = get_hostname(url)
    
    html = session.get(url).content
    soup = bs(html, "html.parser")

    links = []
    total_files = 0
    path = f"download/{domain}/css/"
    
    table = Table(box=None)
    table.add_column("Filename", style="cyan")
    table.add_column("URL", style="bold green")
    table.add_column("Size", style="blue")
    table.add_column("Status")
    
    createFolder(path)
    
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
        text = requests.get(css_url).text
        file_name = path + getRemoteFileName(css_url)
        
        with open(file_name, 'w', encoding="utf-8") as f:
            f.write(text)
            
        total_files += 1
        
        if os.path.exists(file_name):
            table.add_row(getRemoteFileName(css_url), css_url, localFileSize(file_name), "[bold green]Download completed[/bold green]")
        else:
            table.add_row(getRemoteFileName(css_url), css_url, localFileSize(file_name), "[bold red]Download failed[/bold red]")
    
    path = os.path.realpath(path)
    os.startfile(path)

    end_time = "{:.2f}".format(time.time() - start_time)
    
    table.caption = f"Total of downloaded files: {total_files} - Time taken: {end_time} seconds"
    console.print(table)

def download_images(url, filter_data):
    start_time = time.time()
    domain = get_hostname(url)
    
    html = session.get(url).content
    soup = bs(html, "html.parser")

    links = []
    total_files = 0
    path = f"download/{domain}/images/"
    
    table = Table(box=None)
    table.add_column("Filename", style="cyan")
    table.add_column("URL", style="bold green")
    table.add_column("Size", style="blue")
    table.add_column("Status", style="bold green")
    
    createFolder(path)
    
    for img in soup.find_all("img"):
        img_url = urljoin(url, img.attrs.get("src"))
        
        if filter_data:
            if find(img_url, filter_data):
                links.append(img_url)
        else:
            links.append(img_url)

    for img_url in list(set(links)):
        img_data = requests.get(img_url).content
        file_name = path + getRemoteFileName(img_url)
        
        with open(file_name, 'wb') as handler:
            handler.write(img_data)
            
        total_files += 1
        
        if os.path.exists(file_name):
            table.add_row(getRemoteFileName(img_url), img_url, localFileSize(file_name), "[bold green]Download completed[/bold green]")
        else:
            table.add_row(getRemoteFileName(img_url), img_url, localFileSize(file_name), "[bold red]Download failed[/bold red]")
    
    path = os.path.realpath(path)
    os.startfile(path)

    end_time = "{:.2f}".format(time.time() - start_time)
    
    table.caption = f"Total downloaded files: {total_files} - Time taken: {end_time} seconds"
    console.print(table)
