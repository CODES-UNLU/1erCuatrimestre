import os
'''
********* MI PROGRAMA *********
1. Saludar.
2. Informar temperatura.
3. Mostrar nombre de materia.
4. Salir.
Seleccione una opción [1-4]:

'''
seguir=True
while seguir:
    print("********* MI PROGRAMA *********")
    print("1. Saludarn")
    print("2. Informar temperatura")
    print("3. Mostrar nombre de materia")
    print("4. Salir")
    opcion=int(input("Ingrese la opcion: "))
    if opcion == 1:
        print("Hola humano\n")
        input("Presione para continuar")
        os.system('cls')        
    if opcion == 2:
        print("Hoy esta nublado\n")
        input("Precione para continuar")
        os.system('cls')
    if opcion == 3:        
        print("Introduccion a la programacion\n")
        input("Precione para continuar")
        os.system('cls')
    if opcion == 4:
        os.system('cls')
        seguir= False
    if opcion <=0 or opcion >4:
        print("Esta opcion no esta disponible\n")
        input("Precione para continuar")
        os.system('cls')