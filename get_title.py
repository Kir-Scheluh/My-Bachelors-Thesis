import requests
from bs4 import BeautifulSoup

def get_html_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.title.string
