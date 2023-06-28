'''
Modifique todos los ejercicios anteriores para que en lugar de permitir el
reintento de manera ilimitada, el programa permita sólo 10 reintentos. Si el
usuario supera el límite de reintentos, el programa debe terminar con el
mensaje “Usted está jugando conmigo, yo me retiro”.

'''
i=0

while i >= 0:
    seguir= True
    while seguir:
        temperatura=input("Ingrese la temperatura: ")
        i=i+1
        
        if i == 10:
            i=-1
            seguir=False
            print("Usted está jugando conmigo, yo me retiro")
        if temperatura.isalpha():
            print("Ingreso letras, debe ingresar solo numeros")
        if temperatura.isalnum() != temperatura.isalpha() and temperatura.isalnum() != temperatura.isdigit():
            print("Ingreso letras y numeros, debe ingresar solo numeros")
        if i < 10:
            if temperatura.isdigit():
                if int(temperatura)<-18 or int(temperatura)>50:
                    print("El rango permitido es de -18º hasta 50º,reingrese un datovalido")
                if int(temperatura)>-18 and int(temperatura)<=50:
                    print("La temperatura es: " + str(temperatura)+"º")
                    seguir=False



    