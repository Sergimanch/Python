numeros = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]
contados = []  

for i in range(len(numeros)):
    if numeros[i] not in contados:  
        cont = 0
        for j in range(i, len(numeros)):  
            if numeros[i] == numeros[j]:
                cont += 1
        print(f"{numeros[i]}:{cont}")
        contados.append(numeros[i])  