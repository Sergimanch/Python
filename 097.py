dicc = {
    "España": ["Madrid", "Barcelona", "Valencia", "Sevilla", "Zaragoza", "Málaga"],
    "Francia": ["París", "Marsella", "Lyon", "Toulouse", "Niza", "Nantes"],
    "Italia": ["Roma", "Milán", "Nápoles", "Turín", "Palermo", "Génova"],
    "Alemania": ["Berlín", "Hamburgo", "Múnich", "Colonia", "Fráncfort", "Stuttgart"],
    "Estados Unidos": ["Nueva York", "Los Ángeles", "Chicago", "Houston", "Phoenix", "Filadelfia"]
}
resp = input("Introduce una ciudad o un pais correctamente ")

if resp in dicc:
    for i in dicc[resp]:
        print(f"{i} ,")
else:
    pais_encontrado = None
    while pais_encontrado == None:
        for pais, ciudades in dicc.items():
            if resp in ciudades:
                pais_encontrado = pais
    if pais_encontrado:
        print(f"{resp} está en {pais_encontrado}")
    else:
        print("No se encontró esa ciudad ni ese país en el diccionario.")