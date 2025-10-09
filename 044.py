numeros = []
num = 0
long = int(input("Introduce la cantidad de numeros que quieres en tu array "))
for i in range(0, long):
    num = int(input("Introduce un numero: "))
    if (num > 0 ):
        numeros.append(num)
print(numeros)