kilogramos = float(input("Ingrese su peso en Kilógramos\n"))
estatura = float(input ("Ingrese su estatura en centímetros\n"))/100 #transforma centímetros a metros

if estatura >0: #impide división por cero   
    
    imc = kilogramos /(estatura * estatura)
    print(f"Tu IMC es de {round(imc,2)} [Kg/m2]")

    if imc < 18.5:
        print("Clasificación OMS : Bajo peso")
    elif imc < 25:
        print("Clasificación OMS : Adecuado")
    elif imc < 30:
        print("Clasificación OMS : Sobrepeso")
    elif imc < 35:
        print("Clasificación OMS : Obesidad grado I")
    elif imc < 40:
        print("Clasificación OMS : Obesidad grado II")
    else:
        print("Clasificación OMS : Obesidad grado III")
else:        
    print("La estatura no puede ser igual o menor que cero")    