array = []
long = int(input("Introduce la cantidad de numeros que quieres en tu array "))
sum = 0
array1 = []
for i in range(0,long):
    array.append(int(input("Introduce un numero ")))
    long -=1
    sum += array[i]
print(array)
print(sum)
