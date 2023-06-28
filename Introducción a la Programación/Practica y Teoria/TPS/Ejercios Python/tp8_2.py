'''
Cree un script que le solicite al usuario ingresar notas de parciales por teclado,
hasta que el usuario ingrese el valor -1, indicando que ya no hay más notas para
cargar. Una vez ingresadas las notas, el programa debe informar la nota
promedio (tenga cuidado de no incluir al -1 dentro del promedio).

'''
promedio=0
suma_notas=0
cantidad=0
i=0
while i>=0:
    nota=float(input("Ingrese la nota: "))
    suma_notas+=nota
    i+=1
    cantidad=i
    if nota == -1:
        suma_notas=suma_notas+1
        cantidad=cantidad-1
        promedio=suma_notas/cantidad
        i=-1       
        print("El promedio de notas es de: ",promedio)



