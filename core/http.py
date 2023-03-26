import socket, requests
from core.utils import *
from urllib.parse import urlparse
from http.client import HTTPConnection, HTTPSConnection

def http_code_list(c):
    r = requests.get('https://gist.githubusercontent.com/thesilvaemily/31aed3c28577f78bcaace2a377f8aa17/raw/4e765d040b739f0d7bc60ef8c2c8f37c17eae81c/http-status-code.json')
    r = r.json()

    for code in r:
        if code == str(c):
            return r[code]["message"] + " (" + r[code]["spec_href"] + ")"

def http_code(url):
    try:
        r = requests.head(url)
        return r.status_code
        # prints the int of the status code. Find more at httpstatusrappers.com :)
    except requests.ConnectionError:
        return False

def get_ip(url):
    url = strip_scheme(url)
    return socket.gethostbyname(url)

def get_hostname(url):
    parsed = urlparse(url)
    return parsed.netloc

def check_https_url(url):
    url = strip_scheme(url)
    HTTPS_URL = f'https://{url}'

    try:
        HTTPS_URL = urlparse(HTTPS_URL)
        connection = HTTPSConnection(HTTPS_URL.netloc, timeout=2)
        connection.request('HEAD', HTTPS_URL.path)
        if connection.getresponse():
            return True
        else:
            return False
    except:
        return False


def check_http_url(url):
    url = strip_scheme(url)
    HTTP_URL = f'http://{url}'

    try:
        HTTP_URL = urlparse(HTTP_URL)
        connection = HTTPConnection(HTTP_URL.netloc)
        connection.request('HEAD', HTTP_URL.path)
        if connection.getresponse():
            return True
        else:
            return False
    except:
        return False
