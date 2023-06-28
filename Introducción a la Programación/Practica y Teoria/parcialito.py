# ---------------INTRO PROG UNLU: EJEMPLO PARCIALITO ENUNCIADO------------------
# Completar con tus datos:
# Nombre:
# DNI:
# Entrega: por GitHub (preferentemente) o por mail a: introprog.unlu@gmail.com 

# A) Suponé que es necesario escribir un programa que procese la edad de los
# docentes de una universidad, y el programa debe terminar cuando el usuario
# ingresa -99 como edad. ¿Qué estructura repetitiva utilizarías para implementar
# el algoritmo? ¿Por qué?. 
# Usaria Ciclos ya que me permitiria verificar la edad de los docentes haciendo una 
# base de datos apopiada para que,al poner -99,
# este pueda sacar la edad de los profesores 
# Puntaje: 1/10

# B1) Programar la función suma_primeros_impares que recibe un número natural n
# como parámetro, y retorna la suma los primeros n números impares.
# Puntaje: 3/10

# B2) Programar la función test_suma_primeros_impares que testea la función
# suma_primeros_impares, con al menos 2 casos de test. Justifique por qué
# considera que esos casos de tests son relevantes para testear el programa.
# Puntaje: 0.5/10

# C1) Programar la función censo_mails que permita realizar una encuesta sobre
# cuántos emails diarios envían las personas. La función debe permitir hacer la
# encuesta para diez (10) personas, solicitando al usuario ingresar los datos
# por teclado. Además de la cantidad de emails diarios, se debe solicitar la
# edad del encuestado.
# Por ejemplo, una entrada válida del programa sería el valor 15 para la
# cantidad de emails diarios enviados, y 23 para la edad.

# Una vez procesadas las diez personas, la función debe informar por pantalla:
# 1) La edad de la persona que más emails envía por día.
# 2) Si la cantidad de emails del primer encuestado se repite al menos una vez.
# 3) El promedio total de emails diarios enviados entre todos los encuestados.
# Puntaje: 5/10

# C2) ¿Es posible testear que su programa funciona correctamente ingresando
# menos de 10 encuestas? Justifique su respuesta.
# Puntaje: 0.5/10
# ------------------------------------------------------------------------------

#################################################
# Funciones Principales y Auxiliares
#################################################

# Ponele a la función los parámetros que consideres necesarios
from typing_extensions import ParamSpec


def suma_primeros_impares():
    pass

     

# Ponele a la función los parámetros que consideres necesarios
def censo_mails():
    pass
        


#################################################
# Funciones de Test
#################################################


def test_suma_primeros_impares(x,n):
    print("Testeando suma_primeros_impares... ", end="")
    assert test_suma_primeros_impares(12) == "Numero par"
    assert test_suma_primeros_impares(5) == "Numero impar"
    print("Pasó!")

def censo_mails(x):
     print("Testeando censo_mails... ", end="")
     assert tests_censo_mails() == "cantidad de mails"



#################################################
# Principal
#################################################


test_suma_primeros_impares()
#censo_mails()
