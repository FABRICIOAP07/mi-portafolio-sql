tareas = []

def mostrar_tareas():
    print("\n=== Lista de tareas ===")
    if not tareas:
        print("No hay tareas registradas.")
    else:
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")

def agregar_tarea():
    nueva = input("Ingresa la nueva tarea: ")
    tareas.append(nueva)
    print("Tarea agregada.")

def editar_tarea():
    mostrar_tareas()
    num = int(input("Número de tarea a editar: "))
    if 1 <= num <= len(tareas):
        nueva_desc = input("Nueva descripción: ")
        tareas[num - 1] = nueva_desc
        print("Tarea actualizada.")
    else:
        print("Número inválido.")

def eliminar_tarea():
    mostrar_tareas()
    num = int(input("Número de tarea a eliminar: "))
    if 1 <= num <= len(tareas):
        tareas.pop(num - 1)
        print("Tarea eliminada.")
    else:
        print("Número inválido.")

def menu():
    while True:
        print("\n=== CRUD de Tareas ===")
        print("1. Mostrar tareas")
        print("2. Agregar tarea")
        print("3. Editar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_tareas()
        elif opcion == "2":
            agregar_tarea()
        elif opcion == "3":
            editar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
