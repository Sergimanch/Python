numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16]
numeros.sort()
mediana=0
if(len(numeros)%2==0):
    mediana=((numeros[(len(numeros)-1)//2] + (numeros[len(numeros)//2]))/2)
else:
    mediana=numeros[len(numeros)//2]
print(f"La mediana de la lista es {mediana}")