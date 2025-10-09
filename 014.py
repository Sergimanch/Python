contraseña = "pepe"
cont = 3
introduce = input("Introduce la contraseña :")
while (cont>0 and introduce != contraseña):
    introduce = input("Te quedan 2 intentos /n Introducela de nuevo: ")
    cont -=1