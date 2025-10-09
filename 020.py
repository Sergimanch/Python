opcion_elegida = input("Introduce un dia de la semana ")
match opcion_elegida:
    case "sabado"|"domingo": 
        print("Es fin de semana")
    case "lunes"|"martes"|"miercoles"|"jueves"|"viernes":
        print("Es laborable")
    case _:
        print("Introduce un dia correcto")