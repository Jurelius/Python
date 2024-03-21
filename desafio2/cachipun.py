

import random
import sys


jugada_usuario= sys.argv[1].lower()

if(jugada_usuario !="piedra" and jugada_usuario !="papel" and jugada_usuario !="tijeras"):
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
    
else:
    print(f"Tu jugaste {jugada_usuario}")
    

    jugada_pc = random.choice (["piedra","papel","tijeras"])
    #print(f"La jugada del Pc es: {jugada_pc}")

    if (jugada_usuario == (jugada_pc)):
        print(f"El pc jugó {jugada_pc}\nEs un empate")
        
    elif (jugada_usuario=="piedra" and jugada_pc=="tijeras") or (jugada_usuario =="papel" and jugada_pc =="piedra") or (jugada_usuario=="tijeras" and jugada_pc=="papel"):
        print(f"El PC jugó {jugada_pc}\nGanaste!!")
    else:
        print(f"El PC jugó {jugada_pc}\nPerdiste!!")
    
    