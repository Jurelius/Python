#for each
"""
for variable in iterable    
"""
#funcion range()
#valor de inicio es el cero
"""
for i in range(10):
    print(i)#0,1,2,3,4,5,6,7,8,9
    
for i in range(4,10):
    print(i)#4,5,6,7,8,9
"""    
diccionario = {
    "Nombre": "Carlos",
    "Apellido": "Santana",
    "Ocupacion": "Guitarrista"
}


print("---------diccionario----------------") 

for clave in diccionario:
    print(clave)
print("") 
for clave in diccionario:
    print(f"clave {clave} - valor {diccionario[clave]}")
    
print("")    
for valor in diccionario.values():
    print(f" el valor es {valor}")
    
print("") 
for clave, valor in diccionario.items():
    print(f"clave {clave} - valor {valor}")