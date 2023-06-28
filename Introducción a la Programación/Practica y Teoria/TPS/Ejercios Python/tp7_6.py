mayor=0
menor=0
for i in range(1,10+1):

    numero=int(input("Nº: "))
    if numero > mayor:
        mayor=numero
        pos= i
    
print("El numero mayor ingresado es ",mayor," y lo ingreso en la posicion",pos)