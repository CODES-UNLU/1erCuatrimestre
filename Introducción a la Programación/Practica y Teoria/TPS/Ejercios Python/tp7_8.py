'''
Un cliente ha solicitado un programa que le permita ingresar los mililitros de
lluvia caídos diariamente en una semana, para que el programa le informe en
pantalla el promedio de precipitación de esa semana. El cliente también desea
saber cuál fue el día en que más llovió en la semana.
A modo ilustrativo, un reporte generado por el programa debería verse como
sigue, luego de haber leído las precipitaciones de los 7 días de la semana:
El promedio de precipitaciones fue de XX mls. diarios.
El día de más precipitaciones fue el xxxxxx (nombre del día).
Tenga en cuenta que la numeración de los días de la semana comienza con el 1
para el día domingo.
Codifique el programa para dar solución a lo solicitado por el cliente.
'''
suma_dato=0
promedio=0
max_precipitacion=0
dia=0


for i in range(1,7+1):
    dato=float(input("Ingrese la precipitacion registrada: "))
    suma_dato+=dato
    promedio= suma_dato/7
    if dato>max_precipitacion:
        max_precipitacion=dato
        dia=i


    if dia == 1:
        dia="Domingo"
    if dia == 2:
        dia="Lunes"
    if dia == 3:
        dia="Martes"
    if dia == 4:
        dia="Miercoles"
    if dia == 5:
        dia="Jueves"
    if dia == 6:
        dia="Viernes"
    if dia == 7:
        dia="Sabado"

print("acumulado: ", suma_dato)
print("Promedio: ", promedio)
print("Dia de mayor precipitacion: ",dia)

