#!/usr/bin/python3

import sys, time
from urllib.request import urlopen
from rich.console import Console

console = Console(record=True)

def plugin_robots(url):
    start_time = time.time()
    
    with urlopen(url + "/robots.txt") as stream:
        robots = stream.read().decode("utf-8")
        
        if robots == None:
            console.print(f"[bold red]Error: robots.txt not exist[/bold red]")
            sys.exit(1)

        for line in robots.split("\n"):
            if line.find("Allow") != -1:
                console.print(f"[green]{line}[/green]")
            elif line.find("Disallow") != -1:
                console.print(f"[red]{line}[/red]")
            elif line.find("Sitemap") != -1:
                console.print(f"[italic cyan]{line}[/italic cyan]")
            elif line.find("User-agent") != -1:
                console.print(f"[italic yellow]{line}[/italic yellow]")
            else:
                console.print(line)
                
    end_time = "{:.2f}".format(time.time() - start_time)
    console.print(f"Time taken: {end_time} seconds")
