def division():
    numero1=int(input("Ingrese un numero: "))
    divisor=int(input("Ingrese un numero: "))
    if divisor == 0: 
        print("No se puede dividir por 0")
    if divisor !=0:
        print(numero1/divisor)

division()