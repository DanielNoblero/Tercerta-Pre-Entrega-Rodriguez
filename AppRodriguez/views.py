from django.shortcuts import render

def index(request):
    return render(request, "AppRodriguez/index.html")

def Venta_minorista(request):
    return render (request, "ApprodRiguez/Venta minorista.html")

def Venta_mayorista(request):
    return render (request, "ApprodRiguez/Venta mayorista.html")

def stock(request):
    return render (request, "ApprodRiguez/stock.html")