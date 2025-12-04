elecciones = {
    "Andrea":0,
    "Misael":0,
    "Hugo":0,
    "Wassim":0,
    "Sergio":0,
    "Fermin":0
}
resp = input("Introduce el nombre de tu voto ")
while resp != "Fin":
    if resp in elecciones:
        elecciones[resp] +=1
    resp = input("Introduce el nombre de tu voto ")
print(elecciones)