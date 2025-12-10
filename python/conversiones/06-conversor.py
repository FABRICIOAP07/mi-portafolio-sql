#convertir temperatura
temperatura=float(input("Ingrese temperatura:"))

escala=input("Es Fahrengent(F) o es Celsius(C)?:").lower()
if escala == "f":
    celsius= (temperatura - 32) * 5/9
    print(celsius)
elif escala=="c":
    fahrengent = temperatura * 1.8 + 32
    print(fahrengent)
else:
    print("escala incorrecta")
    
