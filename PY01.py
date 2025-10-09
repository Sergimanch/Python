num = int(input("Introduce un numero para el que comprobar sus divisores: "))
i = 1
for i in range(1,num+1):
    if(num % i == 0):
        print(i, end=" ")
