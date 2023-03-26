import requests
from urllib.parse import urlparse
    
def query_string_remove(url):
    return url[:url.find('?')]

def human_readable_size(size, decimal_places=2):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if size < 1024 or unit == 'PB':
            break
        size /= 1024.0

    return f"{size:.{decimal_places}f} {unit}"

def remote_file_size(url):
    try:
        req_headers = requests.get(url)
        return human_readable_size(int(req_headers.headers["Content-Length"]))
    except:
        print("unknown error")

def strip_scheme(url):
    parsed = urlparse(url)
    scheme = "%s://" % parsed.scheme
    return parsed.geturl().replace(scheme, '', 1)
