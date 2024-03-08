nombre = "Cristian"
apellido1 ="Morales"
apellido2 ="Henriquez"
edad = "49"
año=2024

#python no permite concatenar (suma) letras con numeros

print("xxxxxxx    informacion  xxxxxxxxxxxx")
print("xxxxxx     "+ nombre    +"      xxxx")
print("xxxxxx     "+ apellido1 +"      xxxx")
print("xxxxxx     "+ apellido2 +"      xxxx")
print("xxxxxx     "+ edad      +"      xxxx")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("el año es", año)

#interpolacion de cadenas (otra forma de imprimir) print

mes = 3
dia = 7

print(f"Hola {nombre}, El año es {año} del mes {mes} y el dia {dia} ")