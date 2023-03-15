from AppRodriguez.models import Mayorista, Minorista, Stock


for _ in range(0,5):
    Mayorista(NombreEmpresa="Nombre de empresa", 
    Telefono="Telefono",
    Email="Email",
    Dni="Dni",
    Direccion= "Direccion",
    ).save()

for _ in range(0,5):
    Minorista(Nombre ="Nombre", 
    Apellido="Apellido",
    Telefono="Telefono",
    Email="Email",
    Dni= "Dni",
    Direccion="Direccion",
    ).save()

for _ in range(0,5):
    Stock(Articulo="Articulo", 
    Cantidad ="Cantidad",
    Precio="Precio",
    ).save()