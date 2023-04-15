#!/usr/bin/python3

from utils.utils import *
from utils.utils_files import *

import requests, pyperclip, time
from rich.console import Console

console = Console(record=True)

def getTitle(title):
    if not title:
        return 'Screenshot made by Linkscraper'
    else:
        return title
    
def embedCode(imgur_code_img, direct_link, imgur_page, title):
    console.print("-" * 60)
    console.print("Embed codes")
    console.print("-" * 60)
    
    console.print(f'[italic yellow]Imgur Post[/italic yellow]: <blockquote class="imgur-embed-pub" lang="en" data-id="{imgur_code_img}"><a href="{removeExtension(imgur_page)}">{getTitle(title)}</a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>')
    console.print(f"[italic yellow]HTML[/italic yellow]: <img src='{direct_link}' alt='{getTitle(title)}'>")
    console.print(f"[italic yellow]Markdown[/italic yellow]: ![{getTitle(title)}]({direct_link})")
    console.print(f"[italic yellow]BBCode[/italic yellow]: [img]{direct_link}[/img]")

def plugin_imgur(file, key, title):
    console.print("-" * 60)

    if not key:
        print(f"[bold red]Error: Key is required[/bold red]")
        print(f"Get yor client id here: [bold green]https://api.imgur.com/oauth2/addclient[/bold green]")
    else:
        start_time = time.time()
        key = getENV(key)
        
        response = requests.request("POST", "https://api.imgur.com/3/image", headers = {
            'Authorization': f"Client-ID {key}"
        }, data = {
            'image': toBase64(file),
            'title': getTitle(title)
        })

        callback = response.json()
        if callback["success"] == True:
            direct_link = callback['data']['link']
            imgur_page = direct_link.replace("i.", "")
            imgur_code_img = removeExtension(imgur_page).replace("https://imgur.com/", "")

            console.print(f"Imgur page: [bold green]{removeExtension(imgur_page)}[/bold green]")
            console.print(f"Link Direct: [bold green]{direct_link}[/bold green]")

            embedCode(imgur_code_img, direct_link, imgur_page, title)

            console.print("-" * 60)
            pyperclip.copy(direct_link)
            console.print(f"[cyan]Link copied to clipboard[/cyan]")
            
            end_time = "{:.2f}".format(time.time() - start_time)
            console.print(f"Time taken: {end_time} seconds")
        else:
            console.print(f"[bold red]Error: {callback['status']} - {callback['data']['error']}[/bold red]")
