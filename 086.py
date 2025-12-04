txt = input("Introduce el texto que quieras: ")
dicc={}
for i in txt:
    if i != " ":
        if i in dicc:
            dicc[i] +=1
        else:
            dicc[i] =1
print(f"{dicc}")
        