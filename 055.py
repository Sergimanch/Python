num = int(input("Introduce un numero: "))
lista = []

for i in range(2, num + 1):
    es_primo=True
    j=2
    while j<=(i**0.5):
        if i%j==0:
            es_primo=False
        j+=1
    if es_primo:
        lista.append(i)
print(f"Números primos hasta {num}: {lista}")

            
