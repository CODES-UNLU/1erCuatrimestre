lado_a=float(input("Ingrese un valor: "))
lado_b=float(input("Ingrese un valor: "))
lado_c=float(input("Ingrese un valor: "))

if lado_a==lado_b==lado_c:
    print("Su triangulo es Equilatero")
if lado_a==lado_b!=lado_c or lado_a==lado_c!=lado_b or lado_b==lado_c!=lado_a:
    print("Su triangulo es Isoseles")
if lado_a!=lado_b!=lado_c:
    print("Su triangulo es Escaleno")
    