num=int(input("Introduce el numero para el varemo las listas"))
lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
mayores=[]
menores=[]
for i in lista:
    if i>num:
        mayores.append(i)
    else:
        menores.append(i)
print(f"La lista de numeros menores que {num} es {menores}")
print(f"La lista de numeros mayores que {num} es {mayores}")