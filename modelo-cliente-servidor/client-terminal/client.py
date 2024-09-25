import requests

URL = "http://127.0.0.1:5000/tareas"

# Función para listar tareas
def listar_tareas():
    print("Ingreso a LISTADO DE TAREAS:")
    response = requests.get(URL)
    if response.status_code == 200 :
        print("Listado de tareas")
        print(response.json())
    else: 
        print("Ocurrio un error")  

# Función para crear una nueva tarea
def crear_tarea():
    nombre_tarea = input("Introduce el nombre de la tarea: ")
    data = {
        "tarea": nombre_tarea
    }
    response = requests.post(URL, json=data)
    
    if response.status_code == 200 :
        print(f"Tarea '{nombre_tarea}' creada.")
    else:
        print(f"Ocurrio un error")

# Función para eliminar una tarea
def eliminar_tarea():
    print("Elimin tus tareas")
    response = requests.delete(URL)
    
    if response.status_code == 200 :
        print("Tareas borradas con exito")     
    else: 
        print("No se borraron tareas")

# Función principal del menú
def mostrar_menu():
    while True:
        print("\n--- Menú ---")
        print("1. Listar tareas")
        print("2. Crear tarea")
        print("3. Eliminar tarea")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            listar_tareas()
        elif opcion == "2":
            crear_tarea()
        elif opcion == "3":
            eliminar_tarea()
        elif opcion == "4":
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar la aplicación
if __name__ == "__main__":
    mostrar_menu()
