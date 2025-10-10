palabras = ["sol", "luna", "cielo", "mar", "rio", "flor", "ave", "nube", "pez", "arbol","jardin", "peces"]
newPalabras = []
for i in palabras:
    if len(i)>=4:
        newPalabras.append(i)
print(f"Las palabras que tienen menos de 4 letras han sido eliminadas {newPalabras}")
