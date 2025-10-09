import random
num = random.randint(0,10)
print(num)
contador = 6
intro = int(input("Introduce un numero: "))
while (num!=intro and contador >0):
    intro = int(input("Error, prueba otra vez:"))
    contador =- 1
if (num == intro):
    "Has encontrado el numero"
else :
    "No has encontrado el numero"
