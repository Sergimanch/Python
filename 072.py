num=int(input("Introduce un numero de 1 a 3 digitos "))
divisores =[]
divisible= num
es_primo = True
if num<2:
    es_primo= False
else:
    for i in range(2, int(num**0.5 + 1)):
        if num % i== 0:
            es_primo = False
if es_primo:
    print(f"{num} es un número primo, no se puede descomponer")
else:
    j=2
    while j<=(divisible/2) and num>=1:
        if num%j==0:
            num=num/j
            divisores.append(j)
        else:
            j+=1
print(f"Los divisores de {divisible} son {divisores}")
            


