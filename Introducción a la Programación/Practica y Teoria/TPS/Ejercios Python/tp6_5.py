dia=int(input("Ingrese un numero del 1 al 7 para saber el dia: "))
if dia==1:
    print("Domingo")
if dia ==2:
    print("Lunes")
if dia==3:
    print("Martes")
if dia==4:
    print("Miercoles")
if dia==5:
    print("Jueves")
if dia==6:
    print("Viernes")
if dia==7:
    print("Sabado")
if dia <1 or dia>7:
    print("El rango de numero es de 1 a 7")