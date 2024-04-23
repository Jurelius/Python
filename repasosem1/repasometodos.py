"""
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
print(lista_de_numeros.__dir__())

colores = ['verde', 'rojo', 'rosa', 'azul']
colores.append("celeste")
print(colores)

lista_de_numeros.insert(5, 20)
print(lista_de_numeros)
colores.pop(2)
print(colores)
colores=colores.pop(0)
print(colores)
colores = ['rojo', 'rosa']
colores.remove("rojo")
print(colores)
"""

animales = ['Gato', 'Perro', 'Tortuga']
animales_2 = ['Hurón', 'Hamster', 'Erizo de Tierra']

mascotas = animales + animales_2
"""
print(animales)
print(len(animales))
print(animales_2)
print(len(animales_2))
print(mascotas)
print(len(mascotas))
"""
animales_actualizados = animales * 4
mascotas = animales_actualizados + animales_2
# Veamos algunas características
print(animales_actualizados)
print(len(animales_actualizados))
print(animales_2)
print(len(animales_2))
print(mascotas)
print(len(mascotas))

lista = [25, 31, "hola"]
lista[2] # "hola"
print(lista[2])
# En un diccionario usamos la clave, y se deben definir de forma explícita
diccionario = {"a": 25, "b": 31, "c": "hola"}
diccionario["c"] 
print (diccionario["c"])

notas = {
"Camila": 7,
"Antonio": 5,
"Felipe": 6,
"Daniela": 5,
"Vicente": 7,
}

notas["Felipe"]
print(notas["Felipe"])

diccionario = {"celular": 140000, "notebook": 489990, "tablet": 120000, "cargador": 12400}
del diccionario["celular"]
print(diccionario)

eliminado = diccionario.pop("tablet")
print(eliminado)
print(diccionario)

diccionario_a = {"nombre": "Alejandra", "apellido": "López", "edad": 33, "altura": 1.55}
print(diccionario_a)
diccionario_b = { "mascota":"miti", "ejercicio":"bicicleta"}
print(diccionario_b)

diccionario_a.update(diccionario_b)
print(diccionario_a)

computador = {'notebook': 489990, 'tablet': 120000, 'cargador': 12400}
computador.keys()
print(computador.keys())
