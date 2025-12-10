def analizar(texto):
    palabras = texto.split()
    caracteres = len(texto)
    cantidad_palabras = len(palabras)

    print("\n=== Análisis del texto ===")
    print("Cantidad de palabras:", cantidad_palabras)
    print("Cantidad de caracteres:", caracteres)
    print("Primera palabra:", palabras[0] if palabras else "N/A")
    print("Última palabra:", palabras[-1] if palabras else "N/A")

def main():
    print("=== Analizador de Texto ===")
    texto = input("Ingresa un texto: ")
    analizar(texto)

if __name__ == "__main__":
    main()

