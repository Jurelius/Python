import string
import getpass

def validar_clave(clave):
    # Verificar si la clave contiene solo letras
    return clave.isalpha()

# Pedir al usuario que ingrese la clave

clave_correcta = getpass.getpass("Ingrese la clave (solo letras): ").lower()

# Mientras la clave ingresada no sea válida
while not validar_clave(clave_correcta):
    print("La clave ingresada no es válida. Por favor, inténtelo de nuevo.")
    clave_correcta = getpass.getpass("Ingrese la clave (solo letras): ")

# Generar la cadena de letras minúsculas ASCII
abecedario = string.ascii_lowercase

# Comparar letra por letra
def comparar_listas(clave_correcta, abecedario):
    intentos = 0
    i, j = 0, 0

    while i < len(clave_correcta) and j < len(abecedario):
        if clave_correcta[i] != abecedario[j]:
            intentos += 1
            j += 1
        else: 
            i += 1
            j = 0
        return intentos

total_intentos = comparar_listas(clave_correcta, abecedario)