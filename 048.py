frase = input("Introduce una frase: ")

palabras = []
for i in frase:
    if i == " ":
        palabras = frase.split(i)
print(f"Tu frase tiene {len(palabras)} palabras")
