from core.http import *
from core.headers import *
from core.static_file import *

from core.plugins.mshots import *
from core.plugins.page_title import *
from core.plugins.wp_detect import *

def run_core(BASE_URL):
    print("-" * 50)
    print("Core")
    print("-" * 50)
    
    print("IP Address:", get_ip(BASE_URL))
    print("HTTP Code:", http_code(BASE_URL))
    print("HTTP Code Message:", http_code_list(http_code(BASE_URL)))

    if check_https_url(BASE_URL):
        print("HTTPS Status: Secure")
    elif check_http_url(BASE_URL):
        print("HTTPS Status: Not secure")

def run_headers(BASE_URL):
    print("-" * 50)
    print("Headers")
    print("-" * 50)

    get_headers(BASE_URL)

def run_cookies(BASE_URL):
    print("-" * 50)
    print("Cookies")
    print("-" * 50)
    
    get_cookies(BASE_URL)

def run_get_js_files(BASE_URL):
    print("-" * 50)
    print("Scripts JavaScript")
    print("-" * 50)
    
    js_files(BASE_URL)

def run_get_css_files(BASE_URL):
    print("-" * 50)
    print("CSS Files")
    print("-" * 50)
    
    css_files(BASE_URL)

def run_get_images_files(BASE_URL):
    print("-" * 50)
    print("Images Files")
    print("-" * 50)
    
    images_files(BASE_URL)

def run_home(BASE_URL):
    print("Target:", BASE_URL)
    print("Hostname: ", get_hostname(BASE_URL))
