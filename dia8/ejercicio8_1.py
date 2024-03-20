import sys
"""
# solicitamos el número de pares a generar
n = 10
# generamos una lista vacía para almacenar los pares
lista_par = []
for i in range(n):
    
# podemos hacer append de los valores generados
    # en este caso partimos desde el 2
    lista_par.append(2*i + 2)
# mostramos el resultado
print(lista_par)


valores = [0,4,5,6,7,8,9]
divisibles = []
for valor in valores:
    if valor % 2 == 0:
        divisibles.append('Divisible')
    else:
        divisibles.append('No Divisible')
print(f"divisibles {divisibles}")

divisibles2 = ['Divisible' if valor % 2 == 0 else 'No Divisible' for valor in valores ]
print(divisibles2)


#####
print("")
lista = ['Lechugas', 'Tomates', 5, 10, True, False, True, 'Papas',5.1, 45.2, 1, 2, 0]
count_str = 0
lista_str= []
for elemento in lista:
    if type(elemento) is str:
        count_str += 1
        lista_str.append(elemento)
        
        print(f" cantidad de string {count_str}")
        print(f" cantidad de string {len(lista_str)}")
        
        #Tarea crear el list comprehension
print()    
"""
a = [100, 200, 1000, 5000, 10000, 10, 5000]
n = len(a)
filtered_array = []
for i in range(n):
    if a[i] >= 1000:
        filtered_array.append(a[i])
        print(filtered_array)


