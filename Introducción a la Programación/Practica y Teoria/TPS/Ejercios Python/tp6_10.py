def QueEs():
    algo=input("Ingrese lo que quiera: ")
    if algo.isdigit():
        return("Usted ingreso numeros")
    if algo.isalpha():
        return("Usted ingreso letras")
    if algo.isalnum():
        return("Usted ingreso una combinacion alfanumerica")
print(QueEs())