op1 = input("Introduce(piedra/papel/tijera) ")
op2 = input("Introduce(piedra/papel/tijera) ")
print(f"La opcion 1 es: {op1} y la opcion 2 es: {op2}")
match op1:
    case "piedra": 
        if(op2 == "papel"):
            print("Gana la opcion 2")
        elif(op2 == "piedra"):
            print("Empate")
        elif(op2 == "tijera"):
            print("Gana la opcion 1")
    case "papel":
        if(op2 == "tijera"):
            print("Gana la opcion 2")
        elif(op2 == "papel"):
            print("Empate")
        elif(op2 == "piedra"):
            print("Gana la opcion 1")
    case "tijera":
        if(op2 == "piedra"):
            print("Gana la opcion 2")
        elif(op2 == "tijera"):
            print("Empate")
        elif(op2 == "papel"):
            print("Gana la opcion 1")
    case _:
        print("Introduce una opcion correcta")