product = {
    "Nombre": "Movil",
    "Precio": 200,
    "Stock": 3
    
}
print(product)
precioNuevo=int(input("Introduce el nuevo precio "))

product.update({"Precio":precioNuevo})
print(product)