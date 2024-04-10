#importamos librería de tiempo para poder dar un poco de tiempo entre la acción y la siguiente respuesta del usuario
import time
#preguntar a usuario si el accidentado responde a estíulos. Utilizamos .lower para transformar en minuscula cualquier ingreso s; n; S; N;
estimulo = input("Responde a estimulos? [s/n]: ").lower()

#respuesta en si, llevar a hospital más cercano. termina el programa
if estimulo == "s":
    print("Valorar necesida de llevarlo al hospital mas cercano")
#respuesta es no, imprimir instrucción, esperar unos segundos y preguntar nuevamente si repira    
else:
    print("Abrir la via Aérea")
    time.sleep(3)    
    respira = input("Respira? [s/n]: ").lower()

    #si respira 
    if respira == "s":
        print("Permitirle posición de suficiente ventilación")
    #si no respira, imprimir instrucción y esperar unos segundos.
    else:
        print("Administrar 5 ventilaciones y llamar a la ambulancia")
        time.sleep(3)
        
        #Generar un ciclo hasta que llegue la ambulancia
        ambulancia= "n"
        while ambulancia == "n":
            signos_vida = input("¿Tiene signos de vida?[s/n]:").lower()

            if signos_vida == "s":
                print("Reevaluar a la espera de la ambulancia")
            else:
                print("Administrar compresiones torácicas hasta que llegue la ambulancia")
                time.sleep(3)

            ambulancia= input("¿Llego al ambulancia? [s/n]:").lower()
            
        
print("Fin del programa")
