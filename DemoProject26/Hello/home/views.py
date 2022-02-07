from django.shortcuts import render, HttpResponse

from home.models import Stock
from django.contrib import messages

# Create your views here.
def index(request):
    print( request.POST.get('stockName'))
    if request.method == "POST":
        stockName = request.POST.get('stockName')
        qty = request.POST.get('qty')
        stock = Stock(stockName=stockName, qty=qty)
        stock.save()
        messages.success(request, 'Details Successfully Added!')
    return render(request,"index.html")
def StockDetails(request):
    print(request)
    if request.method == "POST":
        stockName = request.POST.get('stockName')
        qty = request.POST.get('qty')
        stock = Stock(stockName=stockName, qty=qty)
        stock.save()
        messages.success(request, 'Details Successfully Added!')
    return render(request, 'index.html')
    
 