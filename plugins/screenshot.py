#!/usr/bin/python3

import os, sys, time
from plugins.imgur import *
from selenium import webdriver
from rich.console import Console

console = Console(record=True)

def browser_chrome(url, file):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    driver.save_screenshot(file)
    driver.quit()

def browser_firefox(url, file):
    driver = webdriver.Firefox()

    driver.get(url)
    driver.save_screenshot(file)
    driver.quit()

def plugin_screenshot(url, file, browser, upload, key, title):
    if not file and not upload:
        console.print(f"[bold red]Error: Parameters is missing[/bold red]")
        sys.exit(1)

    start_time = time.time()
    if not browser or browser == 'chrome':
        browser_chrome(url, file)
    elif browser == 'firefox':
        browser_firefox(url, file)
    else:
        console.print(f"[bold red]Error: Browser invalid[/bold red]")
        sys.exit(1)

    if os.path.exists(file):
        console.print(f"[bold green]Success: screenshot saved with successfully.[/bold green]")

        if not upload:
            os.startfile(file)
            
            end_time = "{:.2f}".format(time.time() - start_time)
            console.print(f"Time taken: {end_time} seconds")
        else:
            if upload == 'imgur':
                plugin_imgur(file, key, title)
            else:
                console.print(f"[bold red]Error: Parameter -up is invalid[/bold red]")
                sys.exit(1)