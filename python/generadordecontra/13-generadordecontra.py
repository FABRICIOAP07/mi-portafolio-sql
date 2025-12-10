
import random
import string

def generar(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(caracteres) for _ in range(longitud))

def main():
    print("Generador de Contraseñas")
    try:
        longitud = int(input("Longitud de contraseña: "))
    except:
        longitud = 12

    print("Contraseña generada:", generar(longitud))

if __name__ == "__main__":
    main()
