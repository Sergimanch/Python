long = int(input("Introduce la longitud del array "))
lista =[]
suma=0
while long>0:
    num = int(input("Introduce un numero "))
    if num %2 !=0:
        lista.append(num)
        suma+=num
    long -=1
print(f"Los numeros impares son {lista} y suman {suma}")