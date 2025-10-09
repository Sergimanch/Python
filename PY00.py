palabra = input("Introduce una palabra ")
contador = 0
for i in palabra:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        contador +=1
print (contador)