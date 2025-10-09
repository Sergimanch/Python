opcion_elegida = int(input("Introduce tu nota: "))
match opcion_elegida:
    case 1|2: 
        print("Muy insuficiente")
    case 3|4:
        print("Insuficiente")
    case 5:
        print("Suficiente")
    case 6: 
        print("Bien")
    case 7|8:
        print("Notable")
    case 9:
        print("Sobresaliente")
    case 10:
        print("Matricula de honor")