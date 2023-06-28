def mayor_nombre():
    nombre1=input("Ingrese un nombre: ")
    nombre2=input("Ingrese un nombre: ")
    letras_n1=len(nombre1)
    letras_n2=len(nombre2)
    if letras_n1>letras_n2:
        return True
    else:
        return False

print(mayor_nombre())