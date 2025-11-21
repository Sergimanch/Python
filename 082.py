dicc = {"Andrea":111112232, "Sergio":222232232, "Quique":882234231, "Andreo": 23221111111, "Sapo": 2323232223}
try:
    nombre = input("De quien quieres saber el numero de telefono ")
    print(dicc[nombre]) 
except KeyError :
    print("No existe ese contacto en la agenda")
finally:
    print("Operacion completada")