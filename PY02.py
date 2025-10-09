mes = int(input("Introduce el numero del mes en el que naciste "))
num = int(input("Introduce el dia en el que naciste "))
match mes :
    case 1:
        if num<20 :
            print(f"Eres capricornio")
        elif(num<31&num>21):
            print(f"Eres Acuario")
    case 2:
        if num<20 :
            print(f"Eres Acuario")
        elif(num<31&num>21):
            print(f"Eres Piscis")
    case 3:
        if num<21 :
            print(f"Eres Piscis")
        elif(num<31&num>21):
            print(f"Eres Aries")
    case 4:
        if num<21 :
            print(f"Eres Aries")
        elif(num<31&num>21):
            print(f"Eres Tauro")
    case 5:
        if num<21 :
            print(f"Eres Tauro")
        elif(num<31&num>21):
            print(f"Eres Geminis")
    case 6:
        if num<22 :
            print(f"Eres Geminis")
        elif(num<31&num>21):
            print(f"Eres Cancer")
    case 7:
        if num<23 :
            print(f"Eres Cancer")
        elif(num<31&num>21):
            print(f"Eres Leo")
    case 8:
        if num<24 :
            print(f"Eres Leo")
        elif(num<31&num>21):
            print(f"Eres Virgo")
    case 9: 
        if num<23 :
            print(f"Eres Virgo")
        elif(num<31&num>21):
            print(f"Eres Libra")
    case 10:
        if num<24 :
            print(f"Eres Libra")
        elif(num<31&num>21):
            print(f"Eres Escorpio")
    case 11:
        if num<23 :
            print(f"Eres Escorpio")
        elif(num<31&num>21):
            print(f"Eres Sagitario")
    case 12:
        if num<22 :
            print(f"Eres sagitario")
        elif(num<31&num>21):
            print(f"Eres capricornio")

        

# Aries: 21 de marzo – 20 de abril
# Tauro: 21 de abril – 20 de mayo
# Géminis: 21 de mayo – 21 de junio
# Cáncer: 22 de junio – 22 de julio
# Leo: 23 de julio – 23 de agosto
# Virgo: 24 de agosto – 22 de septiembre
# Libra: 23 de septiembre – 23 de octubre
# Escorpio: 24 de octubre – 22 de noviembre
# Sagitario: 23 de noviembre – 21 de diciembre
# Capricornio: 22 de diciembre – 20 de enero
# Acuario: 21 de enero – 19 de febrero
# Piscis: 20 de febrero – 20 de marzo