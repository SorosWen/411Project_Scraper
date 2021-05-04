from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse



def search_product(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        return render(request, 'products/fetch_info.html', {'product_name': product_name})
    else:
        return render(request, 'products/fetch_info.html')


"""
amazon_getInfo(url)
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



from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages #import messages

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("products:search")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="products/register.html", context={"register_form":form})




from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("products:search")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="products/login.html", context={"login_form":form})





from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("products:search")