diccNotas = {"Mates":[4,8,10], "Lengua":[5,9,6], "Inglés":[3,7,8], "Fornite":[6,6,9]}
for i in diccNotas:
    media = 0
    for j in diccNotas[i]:
        media+=j
    print(f"Media de {i} : {media/len(diccNotas[i])}")