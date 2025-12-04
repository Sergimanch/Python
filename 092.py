alumnos = {
    "Wassim": {"nota1": 7.5, "nota2": 8.0, "nota3": 6.5},
    "Juan": {"nota1": 5.0, "nota2": 6.0, "nota3": 7.0},
    "Emily": {"nota1": 9.0, "nota2": 8.5, "nota3": 9.5},
    "Raúl": {"nota1": 4.0, "nota2": 3.5, "nota3": 3.0}
}
def media(dicc):
    for n in range(1, 4):
        key = f"nota{n}"
        total = 0.0
        sumatorio = 0
        for notas in dicc.values():
            if key in notas:
                total += notas[key]
                sumatorio += 1
        if sumatorio:
            avg = total / sumatorio
            print(f"La nota media de {key} es {avg:.2f}")
        else:
            print(f"No hay datos para {key}")
media(alumnos)

def notaAlta(notas):
    