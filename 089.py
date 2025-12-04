dicc = {
    "12345678Z":["Sergio", "Currante", 1300],
    "00000001R":["Andrea", "Chusa", 400],
    "87654321X":["Hugo", "Maleante", 2000],
    "23456789L":["Wassim", "Hacker", 5000],
    "34567890M":["Fermin", "Dormir", 200]
}
for i in dicc:
    print(f"El usuario con dni {i} es", end= " ")
    for j in dicc[i]:
        print(f"{j}")