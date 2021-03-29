from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def search_product(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        return render(request, 'products/fetch_info.html', {'product_name': product_name})
    else:
        return render(request, 'products/fetch_info.html')
