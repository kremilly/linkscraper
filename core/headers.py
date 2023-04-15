#!/usr/bin/python3

import requests, time

from utils.utils import *

from rich.json import JSON
from rich.table import Table
from rich.console import Console

console = Console(record=True)

def get_cookies(url, filter_data):
    table = Table(box=None)
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Value")
    
    cookies = []
    total_cookies = 0
    start_time = time.time()
    response = requests.Session().get(url)
    
    for cookie in response.cookies.get_dict():
        if filter_data:
            if find(cookie, filter_data):
                cookies.append(cookie)
        else:
            cookies.append(cookie)
    
    for cookie in cookies:
        table.add_row(cookie, response.cookies.get_dict()[cookie])
        total_cookies += 1
    
    end_time = "{:.2f}".format(time.time() - start_time)
    table.caption = f"Total of cookies on page: {total_cookies} - Time taken: {end_time} seconds"
    console.print(table)

def get_headers(url, filter_data):
    table = Table(box=None)
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Value")

    headers = []
    total_headers = 0
    start_time = time.time()
    req_headers = requests.get(url)
    
    for header in req_headers.headers:
        if filter_data:
            if find(header, filter_data):
                headers.append(header)
        else:
            headers.append(header)
    
    for header in headers:
        if isJSON(req_headers.headers[header]):
            table.add_row(header, JSON(req_headers.headers[header]))
        else:
            table.add_row(header, req_headers.headers[header])
        
        total_headers += 1
    
    end_time = "{:.2f}".format(time.time() - start_time)
    table.caption = f"Total of headers: {total_headers} - Time taken: {end_time} seconds"
    console.print(table)
