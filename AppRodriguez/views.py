from django.shortcuts import render
from AppRodriguez.models import Mayorista, Minorista, Stock
from AppRodriguez.forms import MayoristaForm, MinoristaForm, StockForm

def index(request):
    return render(request, "AppRodriguez/index.html")

def Venta_mayorista(request):
    context = {
        "form": MayoristaForm(),
        "mayorista": Mayorista.objects.all(),
        }
    
    return render(request, "AppRodriguez/Venta_mayorista.html", context)

def agregar_mayorista(request):
    mayorista_form = MayoristaForm(request.POST)
    mayorista_form.save()
    context = {
        "form": MayoristaForm(),
        "mayorista": Mayorista.objects.all(),
        
        }
    return render(request, "AppRodriguez/Venta_mayorista.html", context)

def Venta_minorista(request):
    context = {        
        "form": MinoristaForm(),
        "minorista": Minorista.objects.all(),
        }
    
    return render(request, "AppRodriguez/Venta_minorista.html", context)

def agregar_minorista(request):
    minorista_form = MinoristaForm(request.POST)
    minorista_form.save()
    context = {
        "minorista": Stock.objects.all(),
        "form": MinoristaForm(),
        }
    
    return render(request, "AppRodriguez/Venta_minorista.html", context)

def Stock_form(request):
    context = {
        "form": StockForm(),
        "stock": Stock.objects.all(),
        }
    
    return render(request, "AppRodriguez/stock.html", context)

def stock(request):
    return render(request, "AppRodriguez/pedidos.html" )

def agregar_stock(request):
    stock_form = StockForm(request.POST)
    stock_form.save()
    context = {
        "stock": Stock.objects.all(),
        "form": StockForm(),
        }
    return render(request, "AppRodriguez/stock.html", context)


def buscar_minorista(request):
    criterio = request.GET.get("criterio")
    context = { "minorista": Minorista.objects.filter(Nombre__icontains=criterio).all(),
            }
    return render(request, "AppRodriguez/buscar.html", context)

def buscar_mayorista(request):
    criterio = request.GET.get("criterio")
    context = { "mayorista": Mayorista.objects.filter(NombreEmpresa__icontains=criterio).all(),
            }
    return render(request, "AppRodriguez/buscar.html", context)

def buscar_stock(request):
    criterio = request.GET.get("criterio")
    context = { "stock": Stock.objects.filter(Articulo__icontains=criterio).all(),
            }
    return render(request, "AppRodriguez/buscar.html", context)