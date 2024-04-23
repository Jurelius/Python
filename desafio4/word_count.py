# codigo para importar archivo lorem_ipsum.txt a python
with open("desafio4/lorem_ipsum.txt", "r") as file:
    #se lee el archivo
    texto= file.read()

#se define la funcion para contar los caracteres
def cuenta_caracteres_distintos(texto):
    #set toma la cadena de texto del archivo y crea el conjunto de los caracteres únicos que componen el texto (sin duplicados)
    caracteres_distintos = set(texto)
    #contamos los caracteres distintos
    return len(caracteres_distintos)

#se define función para contar las palabras
def cuenta_palabras_distintas(texto):
    #se realiza la misma acción que en la linea 8 pero agregando método .split() para formar palabras
    palabras_distintas = set(texto.split())
    #contamos palabras distintas
    return len(palabras_distintas)

# Se realiza cálculo de la cantidad de caracteres distintos
caracteres_distintos = cuenta_caracteres_distintos(texto)
print(f"Caracteres distintos: {caracteres_distintos}")

# Se realiza cálculo de la cantidad de palabras distintas
palabras_distintas = cuenta_palabras_distintas(texto)
print(f"Palabras distintas: {palabras_distintas}")
