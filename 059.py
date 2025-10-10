num=int(input("Introduce el numero a reemplazar: "))
cambio=int(input("Introduce el numero para reemplazar: "))
numeros = [3, 7, 2, 7, 1, 3, 8, 2, 5, 3, 7, 9]
newnumeros=[]
for i in numeros:
    if i == num:
        newnumeros.append(cambio)
    else:
        newnumeros.append(i)
print(numeros)
print(f"El valor a cambiar es el {num} y se cambia por {cambio}")
print(newnumeros)
