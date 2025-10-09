num1 = int(input("Introduce un numero "))
num2 = int(input("Introduce otro numero "))
opcion_elegida = input("Introduce que operacion quieres realizar(+/-/*/:) ")
match opcion_elegida:
    case ":": 
        if(num2>num1):
            print("Error el 1er numero es más pequeño que el segundo numero")
        else:
            print(num1/num2)
    case "*":
        print(num1 * num2)
    case "+":
        print(num1 +  num2)
    case "-":
        print(num1 - num2)
    case _:
        print("Introduce una opcion correcta")