import getpass
password = getpass.getpass("Ingrese la clave secreta: ")

#la funcion getpass hace que el ingreso de la clave no sea visible
# En este caso definimos nuestro password como "hola mundo"
# En este caso, mientras la contraseña no sea hola mundo,
# seguirá solicitando la contraseña, pero esta vez con otro mensaje.

while password != "hola mundo":
    password = getpass.getpass("La clave secreta no es correcta. Intenta otra vez: ")
    
print("Fin del programa")
    

