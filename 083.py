dicc = {"Andrea": 6, "Andreo": 9, "Quique":3, "Sergio":10, "Bianca":4}
max = ["", 0]
for i in dicc:
    if dicc[i]>max[1]:
        max[0] = i
        max[1] = dicc[i]
print(f"Nota mayor de: {max}")