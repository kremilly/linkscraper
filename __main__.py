#!/usr/bin/python3

import sys, argparse
from utils.utils import *
from core.functions import *
from plugins.autoload import *
from rich.console import Console

console = Console(record=True)

version = "2.0.0"
parser = argparse.ArgumentParser()

parser.add_argument("-u", "--url", help="URL to scan", required=True)
parser.add_argument("-a", "--action", help="Run an action", required=False)
parser.add_argument("-p", "--plugin", help="Load a plugin", required=False)
parser.add_argument("-f", "--file", help="Save output file", required=False)
parser.add_argument("-filter", "--filter", help="Filter data", required=False)
parser.add_argument("-d", "--download", help="Download static files", required=False)
parser.add_argument("-up", "--upload", help="Upload the screenshot to Imgur", required=False)
parser.add_argument("-b", "--browser", help="Set browser to take screenshot", required=False)
parser.add_argument("-t", "--title", help="Set title the screenshot on Imgur", required=False)
parser.add_argument("-ssc", "--show-status-code", help="Show status code", required=False, default="false")
parser.add_argument("-version", "--version", help="Show current version", action="version", version=version)
parser.add_argument("-k", "--key", help="Set the API key to use an plugin that is needs this", required=False)
parser.add_argument("-smf", "--show-minify-files", help="Show only minify files", required=False, default="false")
parser.add_argument("-oel", "--only-external-links", help="Show only external links", required=False, default="false")

args = parser.parse_args()

if __name__ == "__main__":
    BASE_URL = args.url
    
    if isURL(BASE_URL) != True:
        console.print("[bold red]Error: URL is missing[/bold red]")
        sys.exit(1)
        
    if check_connection(BASE_URL) != True:
        console.print("[bold red]Error: connection is not established")
        sys.exit(1)

    run_home(BASE_URL, version)

    if not args.action or args.action == "get-core" or args.action == "core":
        run_core(BASE_URL)
    elif args.action == "get-headers" or args.action == "headers":
        run_headers(BASE_URL, args.filter)
    elif args.action == "get-cookies" or args.action == "cookies":
        run_cookies(BASE_URL, args.filter)
    elif args.action == "get-js-files" or args.action == "js-files":
        run_get_js_files(BASE_URL, args.show_minify_files, args.filter, args.download)
    elif args.action == "get-css-files" or args.action == "css-files":
        run_get_css_files(BASE_URL, args.show_minify_files, args.filter, args.download)
    elif args.action == "get-links" or args.action == "links":
        run_get_links(BASE_URL, args.only_external_links, args.show_status_code, args.filter)
    elif args.action == "get-emails" or args.action == "emails":
        run_get_emails(BASE_URL, args.filter)
    elif args.action == "get-images-files" or args.action == "images-files":
        run_get_images_files(BASE_URL, args.filter, args.download)
    elif args.action == "get-plugins" or args.action == "plugins":
        console.print("-" * 60)
        console.print(f"Plugin: [bold cyan]{args.plugin}[/bold cyan]")
        console.print("-" * 60)

        if args.plugin == "wp-detect":
            plugin_wp_detect(BASE_URL)
        elif args.plugin == "whois":
            plugin_whois(BASE_URL)
        elif args.plugin == "robots":
            plugin_robots(BASE_URL)
        elif args.plugin == "page-details":
            plugin_page_details(BASE_URL)
        elif args.plugin == "virustotal":
            plugin_virustotal(BASE_URL, args.key)
        elif args.plugin == "ip-location":
            plugin_ip_location(BASE_URL)
        elif args.plugin == "screenshot":
            plugin_screenshot(BASE_URL, args.file, args.browser, args.upload, args.key, args.title)
        else:
            console.print(f"[bold red]Error: Plugin invalid[/bold red]")
    else:
        console.print("-" * 60)
        console.print(f"[bold red]Error: Action invalid[/bold red]")
