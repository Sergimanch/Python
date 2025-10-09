numeros = [-10, -5, -3, -1, 0, 1, 3, 5, 7, 10]
contador = 0
for i in numeros:
    if i < 0:
        print(i)
        contador +=1
print(f"Hay un total de {contador} numeros")