mayor=0
menor=0
negativo=0
for i in range(1,10+1):

    numero=int(input("Nº: "))
    if numero >= mayor:
        mayor=numero
        pos1= i
    
        
    if numero <= menor:
        menor=numero
        pos= i
        
print("El mayor numero ingresado es ",mayor," y lo ingreso en la posicion",pos1)

print("El menor numero ingresado es ",menor," y lo ingreso en la posicion",pos)
