#!/usr/bin/python3

import pyfiglet, time
from datetime import datetime

from core.http import *
from core.headers import *
from core.scraper import *
from core.static_files import *
from rich.console import Console

console = Console(record=True)

def run_core(url):
    console.print("-" * 60)
    console.print("Core")
    console.print("-" * 60)
    
    start_time = time.time()
    console.print("IP Address:", get_ip(url))
    console.print("HTTP Code:", str(http_code(url)))
    console.print("HTTP Code Message:", http_code_list(http_code(url)))

    if check_https_url(url):
        console.print("HTTPS Status: [bold green]Secure[/bold green]")
    elif check_http_url(url):
        console.print("HTTPS Status: [bold red]Not secure[/bold red]")
        
    end_time = "{:.2f}".format(time.time() - start_time)
    console.print(f"Time taken: {end_time} seconds")

def run_headers(url, filter_data):
    console.print("-" * 60)
    console.print("Headers")
    console.print("-" * 60)

    get_headers(url, filter_data)

def run_cookies(url, filter_data):
    console.print("-" * 60)
    console.print("Cookies")
    console.print("-" * 60)
    
    get_cookies(url, filter_data)

def run_get_js_files(url, minify_files, filter_data, download):
    console.print("-" * 60)
    console.print("Scripts JavaScript")
    console.print("-" * 60)
    
    js_files(url, minify_files, filter_data, download)

def run_get_css_files(url, minify_files, filter_data, download):
    console.print("-" * 60)
    console.print("CSS Files")
    console.print("-" * 60)
    
    css_files(url, minify_files, filter_data, download)

def run_get_images_files(url, filter_data, download):
    console.print("-" * 60)
    console.print("Images Files")
    console.print("-" * 60)
    
    images_files(url, filter_data, download)

def run_get_links(url, external_links, status_code, filter_data):
    console.print("-" * 60)
    console.print("Links")
    console.print("-" * 60)
    
    get_links(url, external_links, status_code, filter_data)

def run_get_emails(url, filter_data):
    console.print("-" * 60)
    console.print("Emails")
    console.print("-" * 60)
    
    get_emails(url, filter_data)

def run_home(url, version):
    console.print(
        "[bold blue]" + pyfiglet.figlet_format("Linkscraper") + "[/bold blue]"
    )
    
    today = datetime.today()
    datetime_obj = today.strftime("%a, %b %d %Y - %I:%M:%S %p")

    console.print(f"\t\tv.[bold green]{version}[/bold green]")
    console.print("-" * 60)

    console.print(f"Target: [bold green]{url}[bold green]")
    console.print(f"Hostname: [bold blue]{get_hostname(url)}[/bold blue]")
    console.print(f"Scan: [italic cyan]{datetime_obj}[/italic cyan]")
