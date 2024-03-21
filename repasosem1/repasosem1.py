#print("Hola Mundo")
#print(20*40.5)
#print("Carlos "+"Santana")
#print("Santana".upper())
#print(len("carlos santana"))
#print("-".join(["a","b","c"]))
#print("hola\na\ntodos")
""""
a =4
a =a + 1
print(a)

nombre = "Carlos"
apellido ="Santana"
print (nombre +" "+apellido)
"""
"""
nombre = 'Carlos'
apellido = 'Santana'
# Interpolación
print("Mi nombre es {} {}".format(nombre,
apellido))

nombre = 'Carlos'
apellido = 'Santana'
# Interpolación
print(f"Mi nombre es {nombre} {apellido}")
"""
prefijo = ['La','El','La','El']
frutas = ['manzana', 'platano','frutilla','tomate']
colores = ['verde','amarillo','roja','rojo']
for p, fruta, color in zip(prefijo, frutas, colores):
    print(f'{p} {fruta} es de color {color}')



