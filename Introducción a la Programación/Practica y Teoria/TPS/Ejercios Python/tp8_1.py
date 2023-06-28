'''
Cree un script que le pida al usuario ingresar palabras, una a una, hasta que el
usuario ingrese la palabra “parar”. A medida que se van ingresando las
palabras, el programa simplemente debe mostrarlas en pantalla. Al detectar la
palabra para detenerse, debe mostrar el mensaje “--- TERMINADO ---”

'''
seguir=True

while seguir:
    palabra=input("Ingrese una palabra: ")

    if palabra != "parar":
        print(palabra)
    if palabra == "parar":
        seguir=False
        print("--- TERMINADO ---")