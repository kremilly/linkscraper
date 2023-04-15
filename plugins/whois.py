#!/usr/bin/python3

import whois
from core.http import *
from rich.console import Console
from rich.table import Table

console = Console(record=True)

def plugin_whois(url):
    domain_name = get_hostname(url)

    whois_info = whois.whois(domain_name)
    table = Table(box=None)

    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Value")
    
    table.add_row("Domain name", whois_info.domain_name)
    table.add_row("Domain registrar", whois_info.registrar)
    table.add_row("WHOIS server", whois_info.whois_server)
    table.add_row("Domain creation date", str(whois_info.creation_date))
    table.add_row("Expiration date", str(whois_info.expiration_date))
    
    console.print(table)
