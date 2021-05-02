import pyppdf.patch_pyppeteer
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd


s = HTMLSession()

url = 'https://www.amazon.com/s?k=AR'

def getdata(url):
    r = s.get(url)
    r.html.render(sleep=1)
    soup = BeautifulSoup(r.html.html, 'html.parser')
    return soup

def getnextpage(soup):
    # this will return the next page URL
    pages = soup.find('ul', {'class': 'a-pagination'})
    if not pages.find('li', {'class': 'a-disabled a-last'}):
        url = 'https://www.amazon.com' + str(pages.find('li', {'class': 'a-last'}).find('a')['href'])
        return url
    else:
        return

output_limit = 5

while output_limit > 0:
    data = getdata(url)
    url = getnextpage(data)
    if not url:
        break
    print(url)
    output_limit = output_limit - 1