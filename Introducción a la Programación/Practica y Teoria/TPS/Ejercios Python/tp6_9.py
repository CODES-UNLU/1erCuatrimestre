def factorial(numero):
    if numero == 0:
        resultado= 1
    if numero<0:
        resultado= "Debe ingresar un numero entero positivo"
    if numero>=1:
        resultado= numero * factorial(numero-1)
    return resultado
numero=int(input("Ingrese un numero para conocer su factorial: "))
print(factorial(numero))