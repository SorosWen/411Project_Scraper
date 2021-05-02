from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

"""
amazon_getPrice(url)
Input: an url of a Amazon product page. 
Funtion: Retrieve product name and price from the iput url. 
Return value: a list with two strings: [product_name, price] 
"""
"""
amazon_getPrice(url)
Input: an url of a Amazon product page. 
Funtion: Retrieve product name and price from the iput url. 
Return value: a list with two strings: [product_name, price] 
"""
def amazon_getInfo(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)

    # product name
    try: 
        product_name = r.html.xpath('//*[@id="productTitle"]', first=True).text
    except: 
        product_name = 'No name for display'
    
    # product price
    try: 
        product_price = r.html.xpath('//*[@id="priceblock_ourprice"]', first=True).text
    except: 
        product_price = 'No Price for display.'

    # product rating
    try: 
        product_rating = r.html.xpath('//*[@id="acrCustomerReviewText"]', first=True).text.replace(' ratings', '')
    except: 
        product_rating = 'Rating is not available.'

    product = [product_name, product_price, product_rating]
    print(product)
    return product


def search_product(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        return render(request, 'products/fetch_info.html', {'product_name': product_name})
    else:
        return render(request, 'products/fetch_info.html')
