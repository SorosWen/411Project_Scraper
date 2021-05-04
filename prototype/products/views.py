from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from bs4 import BeautifulSoup
import requests

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})


def search_product(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        product_list = amazon_getSearchResult(product_name)
        return render(request, 'products/fetch_info.html', {'product_name': product_name, 'product_list': product_list})
    else:
        return render(request, 'products/fetch_info.html')


############################################################################
############################################################################
# Amazon Scrapping Function #
############################################################################
"""
amazon_getSearchResult(product_name)
Input: the name of a product. 
Function: It take this product name and scrap information of all related products from Amazon. 
Output: a list of product information, each element is the info of a product.
    ex. [   [title1, price1, rating1], 
            [title2, price2, rating2], 
            [title3, price3, rating3]   ]
"""
def amazon_getSearchResult(product_name):
    url = 'https://www.amazon.com/s?k=' + product_name.replace(' ', '+')
    webpage = requests.get(url, headers = HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})
    product_list = []
    count = 10
    for link in links: 
        link = "https://www.amazon.com" + link.get('href')
        product_list.append(amazon_product(link))
        count -= 1
        if count <= 0:
            break
    return product_list


"""
amazon_product(url) # helper
Input: the url of the Amazon product page. 
Output: a list of information about this product. [title, price, rating]
"""
def amazon_product(url):
    webpage = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    title = soup.find("span", attrs={"id":'productTitle'}).text.replace('\n', '').replace('\'', '')
    price = get_price(soup)
    rating = get_rating(soup)
    return [title, price, rating]


"""
get_price(soup) # helper
Input: a soup object of the Amazon product page. 
Output: a string containing the price of this product. 
"""
def get_price(soup):
    try:
        price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()
    except AttributeError:
        price = ""  
    return price

"""
get_rating(soup) # helper
Input: a soup object of the Amazon product page. 
Output: a string containing the rating of this product. 
"""
def get_rating(soup):
    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = ""
    return rating
