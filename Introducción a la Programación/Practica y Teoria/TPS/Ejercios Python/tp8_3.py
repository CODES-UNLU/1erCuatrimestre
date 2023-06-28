'''
Cree un script que le solicite al usuario leer un número entero entre 1 y 100. El
programa debe ser capaz de solicitarle al usuario que reingrese el número
cuantas veces sea necesario, hasta que el usuario provea un dato válido. Cada
vez que detecte un error de validación, informele al usuario cuál fue el error, con
los mensajes “El dato ingresado no es numérico.”, o “El número ingresado está
fuera del rango permitido.”. Finalmente, cuando el usuario ingrese un dato
válido, muestre el mensaje “[NÚMERO] es válido. Gracias!”.
'''
seguir= True

while seguir:
    numero=input("Nº: ")
    if numero.isalpha():
        print("El dato ingresado es alfabetico")
    if numero.isalnum() != numero.isalpha() == numero.isdigit():
        print("El dato ingresado es alfanumerico")
    if numero.isdigit():
        if int(numero)<0:
            print("El numero ingresado esta fuera de rango")
        if int(numero) <=0 or int(numero) >100:
            print("El numero ingresado esta fuera de rango")
        if int(numero) >=1 and int(numero) <=100:
            print(numero,"es válido. Gracias!")
            seguir= False