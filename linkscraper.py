#!/usr/bin/python3

import argparse
from core.utils import *
from core.modules import *

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="URL to scan", required=True)
parser.add_argument("-s", "--section", help="Display a section", required=False)
parser.add_argument("-p", "--plugin", help="Load a plugin", required=False)
args = parser.parse_args()

if __name__ == "__main__":
    BASE_URL = args.url
    run_home(BASE_URL)

    if not args.section or args.section == "get-core" or args.section == "core":
        run_core(BASE_URL)
    elif args.section == "get-headers" or args.section == "headers":
        run_headers(BASE_URL)
    elif args.section == "get-cookies" or args.section == "cookies":
        run_cookies(BASE_URL)
    elif args.section == "get-js-files" or args.section == "js-files":
        run_get_js_files(BASE_URL)
    elif args.section == "get-css-files" or args.section == "css-files":
        run_get_css_files(BASE_URL)
    elif args.section == "get-images-files" or args.section == "images-files":
        run_get_images_files(BASE_URL)
    elif args.section == "get-plugins" or args.section == "plugins":
        print("-" * 50)
        print(f"Plugin: {args.plugin}")
        print("-" * 50)

        if args.plugin == "wp-detect":
            plugin_wordpress_detect(BASE_URL)
        elif args.plugin == "mshots":
            plugin_mshots(BASE_URL)
        elif args.plugin == "page-title":
            print(plugin_page_title(BASE_URL))
        else:
            print("Error: plugin invalid")