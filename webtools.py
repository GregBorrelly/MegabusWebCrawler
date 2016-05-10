from urllib.request import urlopen
from  urllib.error import URLError
import urllib.request
import time
from bs4 import BeautifulSoup

def set_headers(url):
    """Prepares headers"""
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    request = urllib.request.Request(url, headers=headers)
    return request

def connect(request, sleep=0):
    """Create a connection with website"""
    while True:
        try:
            time.sleep(sleep) # slows down the requests.
            connection = urlopen(request)
            return connection

        except URLError as e:
            print('Something is wrong', e, ' Attemting to fix it.\n')
            continue

def create_bs4_obj(connection):
    """Creates a beautiful Soup object"""
    soup = BeautifulSoup(connection, 'html.parser')
    return soup

def DownloadData(url):
    """Downloads data from given url, and returns a BEAUTIFUL SOUp object"""
    requests = set_headers(url)
    connection = connect(requests)
    html = create_bs4_obj(connection)
    return html


