"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppRodriguez.views import index, Venta_minorista, Venta_mayorista, Stock_form, buscar_minorista, agregar_minorista, agregar_mayorista, agregar_stock, buscar_mayorista, buscar_stock

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"), 
    path("Venta_minorista/", Venta_minorista, name = "Venta_minorista"),
    path("Venta_minorista/agregar", agregar_minorista, name = "agregar_minorista"),
    path("Venta_mayorista/", Venta_mayorista, name = "Venta_mayorista"),
    path("Venta_mayorista/agregar", agregar_mayorista, name = "agregar_mayorista"),
    path("stock/", Stock_form, name = "stock"),
    path("stock/agregar", agregar_stock, name = "agregar_stock"),
    path("buscar/", buscar_minorista, name = "buscar_minorista"),
    path("buscar/", buscar_stock, name = "buscar_stock"),
    path("buscar/", buscar_mayorista, name = "buscar_mayorista"),
    
]