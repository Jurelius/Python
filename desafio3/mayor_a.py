"""
    Actividad 1 - Filtrado compacto
    Se solicita devolver un informe resumido que exponga los meses que superan un cierto
    umbral. El programa mayor_a.py debe retornar un diccionario con el mes y el valor asociado
    siempre y cuando superen el umbral especificado. 
"""
#ejemplo : python mayor_a.py 40000. Solicita ingresar valores a través del argumento
import sys

#umbral, los valores serán números desde la posición 1 
umbral =int(sys.argv[1])

#diccionario 
ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}
#se crea nuevo diccionario vacio en el que se mostraran valores que superen el umbral indicado

mayores_umbral={}

#debemos recorrer el diccionario. Usamos .items para ocupar tanto clave como valor 
for clave, valor in ventas.items():

#Establecemos la condición, si el valor es mayor al umbral ingresado este se agrega al nuevo diccionario. 
#En caso contrario no lo considera y vuelve a recorrer el diccionario    
    
    if valor > umbral :
        mayores_umbral[clave] = valor
        
#Al terminar de recorrer todos los items del diccionario ventas imprimirá en el nuevo diccionario aquellos items que cumpan con la condición.        
print(f"Los items con valor mayor al umbral ingresado son : {mayores_umbral}")        
        
        
        
        
