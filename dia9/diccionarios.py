"""
DICCIONARIOS
PAR--> {CLAVE:VALOR}
La clave debe ser UNICA, en el caso que esta esté repetida, 
el prin arrojará el ultimo valor asociado a la clave
"""

#diccionario vacio

notas = {}
notas = {
    "Camila": 7,
    "Antonio":7,
    "Felipe": 6,
    "Antonia": 7,
    }

#Acceder a los valores del diccionario


print(notas["Camila"])
print(notas["Antonio"])
print(notas["Felipe"])
print(notas["Antonia"])


#Agregar par clve:valor al diccionario
#diccionario[clave] = Valor

notas["Mijail"] = 7
print(notas)#{'Camila': 7, 'Antonio': 7, 'Felipe': 6, 'Antonia': 7, 'Mijail': 7}

notas["Julio"] = 7
print(notas)#{'Camila': 7, 'Antonio': 7, 'Felipe': 6, 'Antonia': 7, 'Mijail': 7, 'Julio': 7} 

#Cambiar el valor a una clave
notas ["Felipe"] = 7#{'Camila': 7, 'Antonio': 7, 'Felipe': 7, 'Antonia': 7, 'Mijail': 7, 'Julio': 7}
print(notas)

#Eliminar elementos
del notas["Antonia"]#{'Camila': 7, 'Antonio': 7, 'Felipe': 7, 'Mijail': 7, 'Julio': 7}
print(notas)

#pop --> al eliminar, permite capturar el elemento
eliminado =notas.pop("Antonio")
print(eliminado)# 7
print(notas)#{'Camila': 7, 'Felipe': 7, 'Mijail': 7, 'Julio': 7}

notas2 ={
    "Alexis":6,
    "Yasna": 6,
    "Camila": 3,
}

#Union de diccionarios
#notas.update(notas2)
#print(notas)#{'Camila': 7, 'Felipe': 7, 'Mijail': 7, 'Julio': 7, 'Alexis': 6, 'Yasna': 6}
#Cuidado colisión de igualdad de llaves, cuando se ingresa una clve ya existente esta queda con el ultimo valor
#{'Camila': 3, 'Felipe': 7, 'Mijail': 7, 'Julio': 7, 'Alexis': 6, 'Yasna': 6} 

notas2.update(notas)
print(notas2)
