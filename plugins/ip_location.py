#!/usr/bin/python3

import requests, time
from core.http import get_ip

from rich.table import Table
from rich.console import Console

console = Console(record=True)

def plugin_ip_location(url):
    ip = get_ip(url)
    start_time = time.time()
    
    response = requests.get(f"http://ip-api.com/json/{ip}")
    resp_json = response.json()

    table = Table(box=None)
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Value", style="white")

    for data in resp_json:
        if resp_json[data] != '':
            table.add_row(data, str(resp_json[data]))
            
    end_time = "{:.2f}".format(time.time() - start_time)
    
    table.caption = f"Time taken: {end_time} seconds"
    console.print(table)
