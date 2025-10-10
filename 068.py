numeros = [0, 1, 0, 3, 12, 0, 5]
ceros=[]
reals=[]
for i in numeros:
    if i==0:
        ceros.append(i)
    else:
        reals.append(i)
print(f"El resultado de la ordenacion es {reals+ceros}")