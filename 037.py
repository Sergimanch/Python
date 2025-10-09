colores = ["rojo", "verde", "azul", "amarillo"]
print(colores)
col = input("Introduce un color de la lista: ")
if col == "rojo" or col == "azul" or col == "verde" or col == "amarillo":
    colores.remove(col)
    print(f"El color {col} ha sido eliminado correctamente")
else:
    print(f"El color {col} no se ha podido eliminar")