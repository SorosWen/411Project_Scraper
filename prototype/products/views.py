from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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


# Register an account
def register_request(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f"New account created: {username}")
      login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    else:
      messages.error(request,"Account creation failed")

    return redirect("products:search")

  form = UserCreationForm()
  return render(request,"products/register.html", {"form": form})

# Login to an account
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

# Logout of account
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("products:search")