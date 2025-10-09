num = int(input("Introduce un numero: "))
numeros = [3, 7, 12, 18, 25, 31, 37, 44, 50, 57, 63, 70, 77, 83, 90, 96, 15, 41, 68, 99]
mayores = []
max = -999999999999
for i in numeros:
    if i>num and i not in mayores:
        mayores.append(i)
for i in mayores:
    if max<i:
        max = i
print(f"El mayor numero del array es: {max}")
temp = mayores
asc=[]
while temp:
    min = temp[0]
    for i in temp:
        if i<min:
            min = i
    asc.append(min)
    temp.remove(min)
print (asc)