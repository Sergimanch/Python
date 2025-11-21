prod = input("Introduce un producto ")
prec = float(input("Introduce el precio "))
dicc = {prod:prec}
while (prod != "fin"):
    prod = input("Introduce un nuevo producto ")
    prec = float(input("Introduce su precio "))
    dicc[prod]=prec
    if "fin" in dicc:
        dicc.pop("fin")
print (dicc)    