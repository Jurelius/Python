import math

radio = input( "Ingrese el radio del paneta en Kilómetros\n")
radio = float(radio)
radio = radio*1000

kgravitacional=input("Ingrese la constante gravitacional en m/s^2\n")
kgravitacional=float(kgravitacional)

VelEscape = 2 * radio * kgravitacional
VelEscape = math.sqrt(VelEscape)

print(f"La velocidad de escape del planeta es igual a {VelEscape:.2f} [m/s]")

