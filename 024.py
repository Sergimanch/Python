unidades = input("Introduce en que unidad vas a meter los datos: ")
medida = int(input(f"¿Cuantos {unidades}s?"))
match unidades:
    case "km":
        print(f"El resultado en metros es {medida*1000}m")
    case "hm":
        print(f"El resultado en metros es {medida*100}m")
    case "dam":
        print(f"El resultado en metros es {medida*10}m")
    case "m":
        print(f"El resultado en metros es {medida}m")
    case "dm":
        print(f"El resultado en metros es {medida/10}m")
    case "cm":
        print(f"El resultado en metros es {medida/100}m")
    case "mm":
        print(f"El resultado en metros es {medida/1000}m")

