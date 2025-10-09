import random

lim_inf= int(input("Introduce el limite inferior "))
lim_sup= int(input("Introduce el limite superior "))
intentos=int(input("Introduce la cantidad de numeros que quieres "))
for i in range(intentos):
    num_rand = random.randint(lim_inf, lim_sup)
    print(num_rand, end=" ")