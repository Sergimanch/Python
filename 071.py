char = input("Introduce un caracter: ").lower()
match char:
    case "a"|"e"|"i"|"o"|"u":
        print("Es una vocal")
    case"%"|"/"|"@"|"#"|"&"|"+"|"?":
        print("Es un caracter especial")
    case"":
        print("Está vacío")
    case _:
        print("Es una consonante")

