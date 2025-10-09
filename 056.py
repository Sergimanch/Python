numeros = [3, 7, 12, 18, 21, 7, 31, 42, 18, 63, 7, 85, 18, 97, 3]
moda=0
maximo=0
for i in numeros:
    cont=0
    for j in range(len(numeros)-1):
        if i==numeros[j]:
            cont+=1
            if maximo<cont:
                maximo=cont
                moda=i
            
    
    
print(f"El numero más repetido es el {moda} con {maximo} repeticiones")
        
