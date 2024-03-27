PrecioSus = input("Ingresa el precio de suscripción pesos($)\n")
PrecioSus = float(PrecioSus)

Usuarios = input(" Ingresa el número de usuarios\n")
Usuarios= float(Usuarios)

gastotales = input(" Ingresa los gastos totales pesos($)\n")
gastotales = float(gastotales)

utilidades = PrecioSus * Usuarios - gastotales

print (f"las utilidades de proyecto son ${utilidades}")
