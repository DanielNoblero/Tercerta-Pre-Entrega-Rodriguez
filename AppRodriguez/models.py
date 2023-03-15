from django.db import models

class Mayorista(models.Model):

    NombreEmpresa= models.CharField(max_length=30)
    Telefono= models.CharField(max_length=15)
    Email = models.CharField(max_length=30)
    Dni = models.CharField(max_length=10)
    Direccion= models.CharField(max_length=50)
    

    def __str__(self):
        return f"""Datos del cliente: 
        Nombre: {self.NombreEmpresa} 
        Telefono: {self.Telefono} 
        Email:{self.Email} 
        Dni: {self.Dni} 
        Direccion: {self.Direccion}"""

class Minorista(models.Model):
    Nombre = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)
    Telefono= models.CharField(max_length=15)
    Email = models.CharField(max_length=30)
    Dni = models.CharField(max_length=10)
    Direccion= models.CharField(max_length=50)
    

    def __str__(self):
        return f"""Datos del cliente: 
        Nombre: {self.Nombre} 
        Apellido: {self.Apellido} 
        Telefono: {self.Telefono} 
        Email:{self.Email} 
        Dni: {self.Dni} 
        Direccion: {self.Direccion}"""

class Stock(models.Model):
    Articulo = models.CharField(max_length=30)
    Cantidad = models.CharField(max_length=30)
    Precio = models.CharField(max_length=15)
    
    

    def __str__(self):
        return f"""Datos del cliente: 
        Articulo: {self.Articulo} 
        Cantidad: {self.Cantidad} 
        Precio: {self.Precio}"""


    
    