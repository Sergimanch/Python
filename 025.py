num = int(input("Introduce un numero: "))
cont = 1
for i in range(num, 1, -1):
    cont *= (i)
print(f"El factorial de {num} es {cont}")