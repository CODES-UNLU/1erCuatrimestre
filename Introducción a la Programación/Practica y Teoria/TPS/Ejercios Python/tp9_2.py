'''Cree un script que le solicite al usuario ingresar su edad. Verifique que el dato
ingresado sea válido, teniendo en cuenta que la edad es un número entero, y el
rango válido para este programa es de 18 a 60 años. El programa debe solicitar
el reingreso de manera indefinida, hasta que el dato sea correcto.
'''
seguir=True

while seguir:
    edad=int(input("Ingrese su edad: "))
    if edad <18 or edad >60:
        print("Dato invalido")
    if edad >=18 and edad <=60:
        print("Su edad es ", edad)
        seguir=False