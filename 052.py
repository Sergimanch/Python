long = int(input("Introduce la longitud del array: "))
arr = []
inv = []
cont = 0
for i in range(long):
    arr.append(int(input("introduce un numero: ")))
print (arr)
while arr:
    inv.append(arr.pop())
print(inv)