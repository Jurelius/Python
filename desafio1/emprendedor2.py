precioSus = input("Ingresa el precio de suscripción en pesos($)\n")
precioSus = float(precioSus)

usuariosP = input(" Ingresa el número de usuarios premiun\n")
usuariosP= float(usuariosP)

usuariosN = input(" Ingresa el número de usuarios normales\n")
usuariosN= float(usuariosN)


gastotales = input(" Ingresa los gastos totales en pesos($)\n")
gastotales = float(gastotales)

utilidades = ((precioSus * usuariosN) + (precioSus*1.5*usuariosP)) - gastotales

print (f"las utilidades de proyecto son ${utilidades:.0f}")

