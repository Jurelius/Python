#la separacion de los float es un punto (.)
#la division entre integers, el resultado es un float

print(4/2) #2.0
print(5/2) #2.5
print(5/3.5)#1.4285714285714286
print(2.4*4)#9.6

nombre = "Mijail"
año = "2024"
print(3*nombre)#MijailMijailMijail
print(año*2)#20242024
#print(nombre/2)#no se puede dividir un string

# Interpolacion de cadenas(otra forma de imprimir) print(f" {nombre_variable}")
mes = 3
dia = 7

print(f"Hola {nombre}, El año es {año} del mes {mes} y el dia {dia} ")

#string.format
#print("".format())bfs
print("Hola {}, El año es {} del mes {} y el dia {}".format(nombre,año,mes,dia))

#interpolacion con % (%s para string y %d para numeros)
print("Hola %s, El año es %s del mes %d y el dia %d" %(nombre, año, mes,dia))

#Metodo count -> busca y cuanta cuantas veces se encuentra un caracter en un string
print("Saitama".count("a"))
print(nombre.count("i"))
#Metodos upper-> todo el string a mayuscula y lower -> todo el string a miniscula
print("Saitama".upper())#SAITAMA
print("SaItAmA".lower())#saitama
print(nombre.upper())#MIJAIL
print(nombre.lower())#mijail
#Metodo title -> solo la primera "letra" a mayuscula
print("14564saItAmA".title())#14564Saitama

# len() -> contar los caracteres de una string
print(len(" israel palma 2024"))#18

#join -> unir string separados en un solo string
print(", ".join(["mijail","palma","loren"]))

#imprimir en mas de una linea (\n)
print("escribir\ncualquier\ncosas")
"""
escribir
cualquier
cosas
"""

mi_direccion = ""
miDireccion = ""
cantidad_alumnos= 30
peso = 85.5
verdadero= True

#Tipo de datos type(nombre_variable)
print(type(nombre))#<class 'str'>
print(type(año))#<class 'str'>
print(type(mes))#<class 'int'>
print(type(peso))#<class 'float'>
print(type(verdadero))#<class 'bool'>

type(verdadero) # no imprime el tipo de dato

#Manipulacion Variables

numero = 2
numero = numero + 3 #numero = 2 + 3
print(numero)#5

nombre = nombre + "Palma" # nombre = "Mijail"+"Palma"
print(nombre)#MijailPalma

#precision de datos 
print(5/9)#0.5555555555555556
print(f"resultado de la division {5/9:.2f}")
print("el resultado de la division",round(5/9,3))


nombre = input("Ingrese su Nombre:  ")
print("Tu nombre es",nombre)
print(f"Tu nombre es {nombre}")

edad = input("Ingrese su Edad:  ")
print("Tu tienes",edad,"años")
print(type(edad))#<class 'str'>



