#!/usr/bin/python3

import cloudscraper, time
from bs4 import BeautifulSoup
from utils.utils import language, country

from rich.table import Table
from rich.console import Console

console = Console(record=True)
            
def language_country(code, param):
    if param == "locale":
        return f"{language(code)} ({country(code)})"
    else:
        return False

def plugin_page_details(url):
    start_time = time.time()
    scraper = cloudscraper.create_scraper() 
    
    html = scraper.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
        
    metatitle = (soup.find('title')).get_text()
    metadescription = soup.find('meta',attrs={'name':'description'})
    robots_directives = soup.find('meta',attrs={'name':'robots'})
    viewport = soup.find('meta',attrs={'name':'viewport'})
    charset = soup.find('meta',attrs={'charset':True})
    open_graph = [[a["property"].replace("og:",""),a["content"]] for a in soup.select("meta[property^=og]")]

    console.print("[blue]Title:[/blue]", metatitle)
    if metadescription: console.print("[blue]Description:[/blue]", metadescription["content"])
    if robots_directives: console.print("[blue]Robots directives:[/blue]", robots_directives["content"].split(","))
    if viewport: console.print("[blue]Viewport:[/blue]", viewport["content"])
    if charset: console.print("[blue]Charset:[/blue]", charset["charset"])

    if open_graph:
        console.print("-" * 60)
        console.print(f"[blue]What is Open Graph?[/blue] The Open Graph protocol enables any web page to become a rich object in a social graph. For instance, this is used on Facebook to allow any web page to have the same functionality as any other object on Facebook.")
        console.print(f"[blue]Documentation:[/blue] [bold green]https://ogp.me[/bold green]")
        console.print("-" * 60)
        
        table = Table(box=None)
        table.add_column("Name", style="cyan", no_wrap=True)
        table.add_column("Value")

        for info in open_graph:
            if not language_country(info[1], info[0]):
                table.add_row("og:" + info[0], info[1])
            else:
                table.add_row("og:" + info[0], language_country(info[1], info[0]))    
        
        console.print(table)
        
    end_time = "{:.2f}".format(time.time() - start_time)
    console.print(f"Time taken: {end_time} seconds")
