from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def search_product(request):
    if request.method == 'POST':
        product = request.POST['product_name']
        return results(request, product)
    else:
        return render(request, 'products/fetch_info.html', {'message': "You are using GET"})


def results(request, product):
    return render(request, 'products/results.html', {'product': product})
