from django.http import HttpResponseRedirect
from django.shortcuts import render

def search_product(request):
    if request.method == 'POST':
        return render(request, 'products/fetch_info.html', {'message': "You are using POST"})
    else:
        return render(request, 'products/fetch_info.html', {'message': "You are using GET"})