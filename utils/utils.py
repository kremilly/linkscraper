#!/usr/bin/python3

import urllib.request
import re, requests, json

from decouple import config
from urllib.parse import urlparse
    
def removeQuery(url):
    split = url.split("?")[1]
    return url.replace("?" + split, "")

def humanSize(bytes, units=[' bytes','KB','MB','GB','TB', 'PB', 'EB']):
    return str(bytes) + units[0] if bytes < 1024 else humanSize(bytes>>10, units[1:])

def stripScheme(url):
    parsed = urlparse(url)
    scheme = "%s://" % parsed.scheme
    return parsed.geturl().replace(scheme, '', 1)

def country(country):
    if find(country, "_"):
        country = country.split("_")[1].lower()
    else:
        country = country.lower()

    if not country:
        country = country

    r = requests.get('https://gist.githubusercontent.com/thesilvaemily/c468fb230d6fcf97de827e37f91f2f6c/raw/3e037cefa50d0381956e862de478c5e5cce758ab/countries.json')
    r = r.json()

    for code in r:
        if code['alpha2'] == country:
            return code['name']

def language(lang):
    if find(lang, "_"):
        lang = lang.split("_")[0].lower()
    else:
        lang = lang.lower()

    r = requests.get('https://gist.githubusercontent.com/thesilvaemily/fd5e5dd45d3480a8da57d56218cecd1e/raw/221c38e4a7e83e2bb9bab92cd8101c9c9adebaaf/languages.json')
    r = r.json()

    for code in r:
        if code['code'] == lang:
            return code['name']

def find(string, find):
    if string.find(find) != -1:
        return True
    else:
        return False

def isJSON(string):
    try:
        if json.loads(string):
            return True
        else:
            return False
    except ValueError as e:
        return False

def isURL(string, check_protocol = True):
    url_pattern_check_protocol = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    url_pattern = "^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    
    if string == None:
        return False
    else:
        if check_protocol == True:
            if re.match(url_pattern_check_protocol, string) != None:
                return True
            else:
                return False
        elif check_protocol == False:
            if re.match(url_pattern, string) != None:
                return True
            else:
                return False

def getENV(string):
    if find(string, "env:") or find(string, "ENV:"):
        return config(string.split(":")[1])
    else:
        return string

def check_connection(host):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False
