frase = "Hola que tal estas que has hecho hoy en tu día a día"
dicc = {}
palabra = ""
for ch in frase:
    if ch != " ":
        palabra += ch
    else:
        if palabra:
            dicc[palabra] = dicc.get(palabra, 0) + 1
            palabra = ""
if palabra:
    dicc[palabra] = dicc.get(palabra, 0) + 1

print(dicc)