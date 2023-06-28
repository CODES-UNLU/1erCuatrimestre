'''
Cree un script que le solicite al usuario ingresar una temperatura en grados
Celsius, y valide que la entrada es correcta, teniendo en cuenta que la
temperatura debe ser un valor numérico, y el rango válido está entre -18 y 50. El
programa debe permitir reingresar el dato cuantas veces sea necesario, hasta
que el usuario provea un dato válido. Procure informar al usuario cuando su
dato es inválido, y cuáles son los valores aceptados.
'''
seguir= True

while seguir:
    temperatura=input("Ingrese la temperatura: ")
    if temperatura.isalpha():
        print("Ingreso letras, debe ingresar solo numeros")
    if temperatura.isalnum() != temperatura.isalpha() and temperatura.isalnum() != temperatura.isdigit():
        print("Ingreso letras y numeros, debe ingresar solo numeros")
    if temperatura.isdigit():
        if int(temperatura)<-18 or int(temperatura)>50:
            print("El rango permitido es de -18º hasta 50º,reingrese un datovalido")
        if int(temperatura)>-18 and int(temperatura)<=50:
            print("La temperatura es: " + str(temperatura)+"º")
            seguir=False