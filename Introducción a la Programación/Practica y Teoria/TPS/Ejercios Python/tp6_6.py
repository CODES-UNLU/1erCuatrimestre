parcial1=float(input("Ingrese la nota de su primer parcial: "))
parcial2=float(input("Ingrese la nota de su segundo parcial: "))
promedio=(parcial1+parcial2)/2
if promedio >=8:
    print("Felicitaciones, usted a promovido la materia")
if promedio > 4 and promedio <8:
    print("Usted se encuentra en condicion regular, y debe rendir el examen final")
if promedio < 4: 
    print("Su promedio no alcanzo para regularizar, por lo que debe rendir un final extendido o recursar")