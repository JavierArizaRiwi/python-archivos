from crud import *


def mostrar_menu():
    print("\n--- CRUD de Archivos (CSV / JSON) ---")
    print("1. Crear registro")
    print("2. Leer registros")
    print("3. Actualizar registro")
    print("4. Eliminar registro")
    print("5. Salir")


def pedir_datos():
    nombre = input("Ingrese el nombre: ")
    edad = input("Ingrese la edad: ")
    rol = input("Ingrese el rol: ")

    return {
        "id": nombre.lower(),
        "nombre": nombre,
        "edad": edad,
        "role": {
            "id": 1,
            "name": rol
        }
    }


def pedir_tipo_archivo(mensaje):
    print(mensaje)
    print("1. CSV")
    print("2. JSON")
    return input("Seleccione una opción: ")


if __name__ == "__main__":
    opcion = ""

    while opcion != "5":
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            datos = pedir_datos()
            tipo = pedir_tipo_archivo("¿Dónde deseas guardar el registro?")

            if tipo == "1":
                crear_registro_csv(datos)
                print("Registro guardado en CSV.")
            elif tipo == "2":
                crear_registro_json(datos)
                print("Registro guardado en JSON.")
            else:
                print("Tipo de archivo no válido.")

        elif opcion == "2":
            tipo = pedir_tipo_archivo("¿Desde dónde deseas leer los registros?")

            if tipo == "1":
                registros = leer_registros_csv()
            elif tipo == "2":
                registros = leer_registros_json()
            else:
                print("Tipo de archivo no válido.")
                registros = []

            print("\n--- Registros encontrados ---")
            if len(registros) == 0:
                print("No hay registros guardados.")
            else:
                for registro in registros:
                    print(registro)

        elif opcion == "3":
            id_valor = input("Ingrese el ID del registro a actualizar: ")
            nuevos_datos = pedir_datos()
            tipo = pedir_tipo_archivo("¿En qué archivo deseas actualizar el registro?")

            if tipo == "1":
                actualizado = actualizar_registro_csv(id_valor, "id", nuevos_datos)
            elif tipo == "2":
                actualizado = actualizar_registro_json(id_valor, "id", nuevos_datos)
            else:
                actualizado = False
                print("Tipo de archivo no válido.")

            if actualizado:
                print("Registro actualizado correctamente.")
            else:
                print("No se encontró el registro.")

        elif opcion == "4":
            id_valor = input("Ingrese el ID del registro a eliminar: ")
            tipo = pedir_tipo_archivo("¿De qué archivo deseas eliminar el registro?")

            if tipo == "1":
                eliminado = eliminar_registro_csv(id_valor, "id")
            elif tipo == "2":
                eliminado = eliminar_registro_json(id_valor, "id")
            else:
                eliminado = False
                print("Tipo de archivo no válido.")

            if eliminado:
                print("Registro eliminado correctamente.")
            else:
                print("No se encontró el registro.")

        elif opcion == "5":
            print("¡Hasta luego!")

        else:
            print("Opción inválida. Intenta de nuevo.")