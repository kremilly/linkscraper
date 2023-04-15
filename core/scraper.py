#!/usr/bin/python3

import re, requests, time

from core.http import *
from utils.utils import *
from utils.utils_files import *

from bs4 import BeautifulSoup as bs

from rich.table import Table
from rich.console import Console

console = Console(record=True)

def get_links(url, external_links, status_code, filter_data):
    start_time = time.time()
    reqs = requests.get(url).text
    soup = bs(reqs, 'html.parser')
    
    table = Table(box=None)
    table.add_column("Domain", style="cyan")
    table.add_column("URL", style="bold green")
    
    if status_code == "true":
        table.add_column("Status", style="bold")
    
    links = []
    total_links = 0
    
    for link in soup.find_all('a'):
        if link.get('href') != None:
            if filter_data:
                if isURL(link.get('href')) and find(link.get('href'), filter_data):
                    links.append(link.get('href'))
            else:
                if not external_links or external_links != "true":
                    if isURL(link.get('href')):
                        links.append(link.get('href'))
                else:
                    if isURL(link.get('href')) and find(get_hostname(link.get('href')), get_hostname(url)) != True:
                        links.append(link.get('href'))
    
    for link in list(set(links)):
        if status_code == "true":
            table.add_row(get_hostname(link), link, str(http_code(link)))
        else:
            table.add_row(get_hostname(link), link)
            
        total_links += 1

    end_time = "{:.2f}".format(time.time() - start_time)
    
    table.caption = f"Total of links in page: {total_links} - Time taken: {end_time} seconds"
    console.print(table)

def get_emails(url, filter_data):
    start_time = time.time()
    text = requests.get(url).text
    soup = str(
        bs(text,'html.parser').body
    )
    
    table = Table(box=None)
    table.add_column("Domain", style="cyan")
    table.add_column("Email", style="bold blue")
    
    total_emails = 0
    emails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', soup)
    list_emails = list(set(emails))
    
    for email in list_emails:
        if filter_data:
            if find(email, filter_data):
                table.add_row(email.split('@')[1], email)
                total_emails += 1
        else:
            table.add_row(email.split('@')[1], email)
            total_emails += 1
    
    end_time = "{:.2f}".format(time.time() - start_time)
    
    table.caption = f"Total of emails on page: {total_emails} - Time taken: {end_time} seconds"
    console.print(table)
