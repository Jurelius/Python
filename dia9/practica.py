"""
1. Crea un diccionario
1. Agrega un elemento
1. Cambia un elemento
1. Elimina un elemento
"""

Banda_Musical = {
    "cantante": "Paula",
    "guitarrista":"Alejandro",
    "bajista":"Mauricio",
    "baterista":"Patricio",
    "tecladista":"Claudio",    
}
print(Banda_Musical)

Banda_Musical ["percusionista"] ="Andrea"
print(Banda_Musical)

Banda_Musical["baterista"] ="Rodrigo"
print(Banda_Musical)

del Banda_Musical["tecladista"]
print(Banda_Musical)



