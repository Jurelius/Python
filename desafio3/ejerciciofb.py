def comparar_listas(lista1, lista2):
    intentos = 0
    i, j = 0, 0

    while i < len(lista1) and j < len(lista2):
        if lista1[i] != lista2[j]:
            intentos += 1
            j += 1
        else: 
            i += 1
            j = 0
    return intentos

# Definir las dos listas
lista1 = ['d' ,'c']

lista2 = ['a', 'b', 'c', 'd', 'e']


# Realizar la comparación
total_intentos = comparar_listas(lista1, lista2)


# Mostrar el resultado
print(f"Total de intentos requeridos: {total_intentos}")
