letra = input("Introduce una letra ")
palabras = ["sol", "luna", "mar", "estrella", "cielo"]  
new =[]
for i in palabras:
    if (i.startswith(letra)):
        new.append(i)
print(new)