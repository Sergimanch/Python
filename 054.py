num = int(input("Introduce un numero: "))

es_primo = True
if num<2:
    es_primo= False
else:
    for i in range(2, int(num**0.5 + 1)):
        if num % i== 0:
            es_primo = False
if es_primo:
    print(f"{num} es un número primo")
else:
    print(f"{num} no es un numero primo")
    