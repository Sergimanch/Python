num = input("Introduce un numero de 3 digitos ")
if len(num)<3:
    print("No es un numero de 3 digitos")
else:
    print(f"Centenas: {num[0]}, Decenas: {num[1]}, Unidades: {num[2]}")