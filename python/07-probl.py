import math
import matplotlib.pyplot as plt

# --- Función recursiva para verificar si un número es primo ---
def es_primo(n, divisor=None):
    if n <= 1:
        return False
    if divisor is None:
        divisor = n // 2
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return es_primo(n, divisor - 1)

# --- Función recursiva para calcular factorial ---
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# --- Definición de f(n) ---
def f(n):
    if es_primo(n):
        return 1
    else:
        return math.log(factorial(n))

# --- Función recursiva para la suma de los n primeros términos ---
def suma_f(n):
    if n == 1:
        return f(1)
    return f(n) + suma_f(n - 1)

# --- Programa principal ---
n = int(input("Ingrese un número n: "))

# Calcular el término y la suma
termino = f(n)
suma = suma_f(n)

print(f"f({n}) = {termino}")
print(f"Suma de los {n} primeros términos = {suma}")

# --- Parte del gráfico ---
n_values = list(range(1, 21))
f_values = [f(i) for i in n_values]

plt.plot(n_values, f_values, marker='o', color='blue')
plt.title("Gráfico de f(n) vs n")
plt.xlabel("n")
plt.ylabel("f(n)")
plt.grid(True)
plt.show()
