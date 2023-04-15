#!/usr/bin/python3

import os, requests, base64
from urllib.parse import urlparse

from utils.utils import *

def localFileSize(file):
    file_size = os.stat(file)
    return humanSize(file_size.st_size)

def remoteFileSize(url):
    try:
        req_headers = requests.get(url)
        return humanSize(
            int(req_headers.headers["Content-Length"])
        )
    except:
        return None

def toBase64(file):
    with open(file, "rb") as f:
        output = base64.b64encode(f.read())
    
    return output

def removeExtension(file):
    return file.rsplit(".", 1)[0]

def getExtension(file):
    ext = os.path.splitext(file)
    
    if ext != "" or ext != ".":
        return ext
    else:
        return None

def getFileName(string):
    name = os.path.split(string)[1]
        
    if find(string, "?"):
        return removeQuery(name)
    else:
        return name

def getRemoteFileName(url):
    a = urlparse(url)
    basename = os.path.basename(a.path)
    
    if find(basename, "."):
        return basename
    else:
        for file in a.path.split("/"):
            if find(file, ".") and len(file) > 1:
                return file

def createFolder(folder):
    if os.path.isdir(folder) != True:
        os.makedirs(folder)
