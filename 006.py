peso=float(input("Introduce tu peso en kg: "))
altura=float(input("Introduce tu altura en metros: "))
imc=peso/(altura**2)
print("Tu índice de masa corporal (IMC) es: ", imc)
if imc<18.5:
    print("Tienes bajo peso")
elif imc>=18.5 and imc<24.9:
    print("Tienes un peso normal")
elif imc>=25 and imc<29.9:
    print("Tienes sobrepeso")
else:
    print("Tienes obesidad")