productos = {
    "manzana": 0.75,
    "leche": 1.20,
    "pan": 0.95,
    "docena de huevos": 2.50,
    "arroz": 1.80
}
prodDesc = {

}
porcentaje = int(input("Introduce un porcentaje de descuento entre 0 y 100: "))
for i in productos:
    prodDesc[i] = round((productos[i] * (1-porcentaje/100)),2)
print(productos)
print(prodDesc)