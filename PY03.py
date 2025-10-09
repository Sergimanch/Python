fig = input("Introduce de que quieres calcular el area y el perimetro: ").lower()
match fig:
    case "cuadrado":
        lad= int(input("Introduce el lado "))
        print(f"El area es {lad*lad} y el perimetro es {lad*4}")
    case "rectangulo":
        lad1 = int(input("Introduce el lado 1 "))
        lad2 = int(input("Introduce el lado 2 "))
        print(f"El area es {lad1*lad2} y el perimetro es {lad1*2 + lad2*2}")
    case "triangulo":
            lad1 = int(input("Introduce el lado "))
            lad2 = int(input("Introduce la altura "))
            print(f"El area es {lad1*lad2/2} y el perimetro es {lad1*3}")
    case "rombo":
        lad1 = int(input("Introduce el lado "))
        diag1 = int(input("Introduce la diago larga "))
        diag2= int(input("Introduce la diago corta "))
        print(f"El area es {diag1*diag2/2} y el perimetro es {lad1*4}")
    case "pentagono":
        lad1 = int(input("Introduce el lado "))
        ap1 = int(input("Introduce la apotema "))
        print(f"El area es {lad1*5*ap1/2} y el perimetro es {lad1*5}")
    case "hexagono":
        lad1 = int(input("Introduce el lado "))
        ap1 = int(input("Introduce la apotema "))
        print(f"El area es {lad1*6*ap1/2} y el perimetro es {lad1*6}")
        
        




