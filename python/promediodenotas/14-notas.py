def calcular_promedio(notas):
    return sum(notas) / len(notas) if notas else 0

def main():
    print("Sistema de Notas")
    notas = []

    while True:
        entrada = input("Ingrese una nota (o 'x' para terminar): ")

        if entrada.lower() == 'x':
            break

        try:
            nota = float(entrada)
            notas.append(nota)
        except:
            print("Nota inválida.")

    print("Notas ingresadas:", notas)
    print("Promedio:", calcular_promedio(notas))

if __name__ == "__main__":
    main()
