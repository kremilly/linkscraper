#!/usr/bin/python3

import requests, sys, time

from core.http import *
from rich.table import Table
from rich.console import Console

console = Console(record=True)

def plugin_virustotal(url, key):
    if not key:
        console.print(f"[bold red]Error: VirusTotal key is required[/bold red]")
        console.print(f"Get the VirusTotal key: [bold green]https://www.virustotal.com/gui/my-apikey[/bold green]")
    else:
        key = getENV(key)
        start_time = time.time()
        
        response = requests.post("https://www.virustotal.com/api/v3/urls", data="url=" + stripScheme(url), headers={
            "x-apikey": key,
            "accept": "application/json",
            "content-type": "application/x-www-form-urlencoded"
        })
        
        if response.status_code != 200:
            if response.json()["error"]["code"] == "WrongCredentialsError":
                console.print(f"[bold red]Error: VirusTotal key is invalid[/bold red]")
                console.print(f"Get the VirusTotal key: [bold green]https://www.virustotal.com/gui/my-apikey[/bold green]")
            else:
                console.print(f"[bold red]Error: {response.json()['error']['message']}[/bold red]")
    
            sys.exit(1)

        response = requests.get(response.json()["data"]["links"]["self"], headers={
            "x-apikey": key,
            "accept": "application/json",
        })

        resp_json = response.json()
        permalink = resp_json["data"]["links"]["item"].replace("api/v3/urls", "gui/url")

        console.print("\t\t Stats:")
        console.print("-" * 60)

        console.print("[bold green]Harmless: [/bold green]" + str(resp_json["data"]["attributes"]["stats"]["harmless"]))
        console.print("[bold red]Malicious: [/bold red]" + str(resp_json["data"]["attributes"]["stats"]["malicious"]))
        console.print("[bold yellow]Suspicious: [/bold yellow]" + str(resp_json["data"]["attributes"]["stats"]["suspicious"]))
        console.print("[bold cyan]Undetected: [/bold cyan]" + str(resp_json["data"]["attributes"]["stats"]["undetected"]))

        console.print("-" * 60)
        console.print(f"Permalink: [bold green]{permalink}[/bold green]")

        console.print ("-" * 60)
        console.print("Result:")
        console.print("-" * 60)
        
        table = Table(box=None)
        table.add_column("Engine", style="cyan", no_wrap=True)
        table.add_column("Result")
        table.add_column("Category")

        for engine in resp_json["data"]["attributes"]["results"]:
            result = resp_json["data"]["attributes"]["results"][engine]["result"]
            category = resp_json["data"]["attributes"]["results"][engine]["category"]

            if result == "clean":
                table.add_row(engine, f"[bold green]{result}[/bold green]")
            elif result == "unrated":
                table.add_row(engine, f"[bold cyan]{result}[/bold cyan]")
            else:
                table.add_row(engine, f"[bold red]{result}[/bold red]", f"[bold red]{category}[/bold red]")
                
        end_time = "{:.2f}".format(time.time() - start_time)
        
        table.caption = f"Time taken: {end_time} seconds"  
        console.print(table)
