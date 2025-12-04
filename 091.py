lista1 = [
    "Sergio",
    "Andrea",
    "Hugo",
    "María",
    "Luis"
]
lista2 = [
    "612345678",
    "623456789",
    "634567890",
    "645678901",
    "656789012"
]
dicc = {}
i = 0
while i<len(lista1):
    dicc[lista1[i]]= lista2[i]
    i+=1
print(dicc)