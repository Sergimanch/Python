lista = [5, 2, 9, 1, 5, 6]
temp = lista
asc=[]
desc=[]
while temp:
    min = temp[0]
    for i in temp:
        if i<min:
            min = i
    asc.append(min)
    temp.remove(min)

print(asc)   
desc = asc[::-1]
print(desc)     
# n = len(lista)
# for i in range(n):
#     for j in range(0,n-i-1):
#         if lista[j]>lista[j+1]:
#             lista[j], lista[j+1] = lista[j+1], lista[j]