precioSus = input("Ingresa el precio de suscripción pesos($)\n")
precioSus = float(precioSus)

usuarios = input(" Ingresa el número de usuarios\n")
usuarios= float(usuarios)

gastotales = input(" Ingresa los gastos totales pesos($)\n")
gastotales = float(gastotales)

utilanterior = input(" Ingresa las utilidades del año pasado en pesos ($)\n")
utilanterior = float(utilanterior)

utilidades = precioSus * usuarios - gastotales

if utilanterior > 0 :

    print (f"Las utilidades actuales de proyecto son ${utilidades:.0f}, las cuales representan un {utilidades/utilanterior:.2f} de las utilidades del año pasado")
    
else:
    
    print ("Las utilidades deben ser mayores a cero")