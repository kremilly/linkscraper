import requests
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs
import urllib3

def get_cookies(url):
    session = requests.Session()
    response = session.get(url)
    
    for cookie in response.cookies.get_dict():
        print(cookie + ":", response.cookies.get_dict()[cookie])

def get_headers(url):
    req_headers = requests.get(url)

    for i in req_headers.headers:
        print(i + ":", req_headers.headers[i])
