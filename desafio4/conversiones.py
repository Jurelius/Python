"""
1. Crear un archivo conversiones.py y una estructura de datos apropiada que permita
ingresar tasas de conversión. Las distintas tasas de conversión se deben ingresar
mediante sys.argv en el siguiente orden: Sol, Peso Argentino, Dólar Americano.
(4 Puntos)
Para ello considere las siguientes tasas de conversión de Peso Chileno:
● a Sol peruano: 0.0046
● a Peso Argentino: 0.093
● a Dólar Americano: 0.00013
Además, ingrese un 4to argumento que sea el valor en peso chileno a convertir. El programa
debe devolver el valor en peso chileno convertido en las 3 divisas ingresadas.
Al ejecutar el programa se espera el siguiente output:
python conversiones.py 0.0046 0.093 0.0013 10000
Respuesta esperada:
Los 10000 pesos equivalen a:
46.0 Soles
930.0 Pesos Argentinos
13.0 Dólares
"""
#importamos módulo sys para poder ingresar valores coo argumentos a través de la términal
import sys

#se define la posición de ingreso de los argumentos de cada una de las divisas.
Sol_peruano = float(sys.argv[1])# argumento en posicion 1.
Peso_argentino = float(sys.argv[2])# argumento en posicion 2
Dolar_americano = float(sys.argv[3])# argumento en posicion 3
Peso_chileno = float(sys.argv[4])# argumento en posicion 4


Sol_peruano = float(sys.argv[4]) * float(sys.argv [1])#cálcula conversión de peso chileno a peso peruano. Se categoriza como float para poder realizar el cálculo matemático
Peso_argentino = float(sys.argv[4]) * float(sys.argv[2])#conversión del peso chileno a peso argentino
Dolar_americano = float(sys.argv[4]) * float(sys.argv[3])#conversión peso chileno a Dolar americano


print(f"los {sys.argv[4]} pesos equivalen a :")
print(f"{Sol_peruano} Soles")
print(f"{Peso_argentino}  Pesos Argentinos")
print(f"{Dolar_americano}  Dólares")

