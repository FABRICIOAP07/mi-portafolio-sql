import random

def juego():
    secreto = random.randint(1, 20)
    intentos = 0

    print("Adivina el número2")
    print("Estoy pensando en un número del 1 al 20.")

    while True:
        num = int(input("Tu número: "))
        intentos += 1

        if num == secreto:
            print(f"¡Correcto! Lo adivinaste en {intentos} intentos.")
            break
        elif num < secreto:
            print("Muy bajo.")
        else:
            print("Muy alto.")

if __name__ == "__main__":
    juego()
