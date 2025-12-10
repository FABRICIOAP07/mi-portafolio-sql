def usd_a_pen(usd):
    tipo_cambio = 3.75
    return usd * tipo_cambio

def pen_a_usd(pen):
    tipo_cambio = 3.75
    return pen / tipo_cambio

def conversor():
    print("Conversor USD ↔ PEN ")
    print("1. USD a PEN")
    print("2. PEN a USD")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        monto = float(input("Monto en USD: "))
        print("Equivalente en PEN:", usd_a_pen(monto))
    elif opcion == "2":
        monto = float(input("Monto en PEN: "))
        print("Equivalente en USD:", pen_a_usd(monto))
    else:
        print("Opción inválida.")

if __name__ == "__main__":
    conversor()
