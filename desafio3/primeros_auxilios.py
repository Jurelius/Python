estimulo = input("Responde a estimulos? [s/n]: ").lower()#s; n; S; N;

if estimulo == "s":
    print("llevar al hospital mas cercano")
else:
    print("Abrir la via Aérea")
    
    respira = input("Respira? [s/n]: ").lower()

    if respira == "s":
        print("Permitirle posición de suficiente ventilación")
    else:
        print("Administrar 5 ventilaciones y llamar a ambulancia")
        
        ambulancia= "n"
        while ambulancia == "n":
            signos_vida = input("¿Tiene signos de vida?[s/n]:").lower()

            if signos_vida == "s":
                print("Reevaluar a la espera de la ambulancia")
            else:
                print("Administrar compresiones toracicas hasta que llegue la ambulancia")

            ambulancia= input("¿Llego al ambulancia? [s/n]:").lower()
            
        
print("Fin del programa")

