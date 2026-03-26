from crud import *

def menu():
    print("\n--- CRUD Archivos (CSV/JSON) ---")
    print("1. Crear registro")
    print("2. Leer registros")
    print("3. Actualizar registro")
    print("4. Eliminar registro")
    print("5. Salir")
    print("------------------------------")

def pedir_datos():
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    return {"id": nombre.lower(), "nombre": nombre, "edad": edad}

if __name__ == "__main__":
    while True:
        menu()
        op = input("Elige una opción: ")
        if op == '1':
            datos = pedir_datos()
            tipo = input("¿Guardar en (1) CSV o (2) JSON?: ")
            if tipo == '1':
                crear_registro_csv(datos)
                print("Registro guardado en CSV.")
            else:
                crear_registro_json(datos)
                print("Registro guardado en JSON.")
        elif op == '2':
            tipo = input("¿Leer de (1) CSV o (2) JSON?: ")
            if tipo == '1':
                registros = leer_registros_csv()
            else:
                registros = leer_registros_json()
            print("\nRegistros:")
            for r in registros:
                print(r)
        elif op == '3':
            id_valor = input("ID del registro a actualizar: ")
            nuevos = pedir_datos()
            tipo = input("¿Actualizar en (1) CSV o (2) JSON?: ")
            if tipo == '1':
                ok = actualizar_registro_csv(id_valor, 'id', nuevos)
            else:
                ok = actualizar_registro_json(id_valor, 'id', nuevos)
            print("Actualizado." if ok else "No encontrado.")
        elif op == '4':
            id_valor = input("ID del registro a eliminar: ")
            tipo = input("¿Eliminar en (1) CSV o (2) JSON?: ")
            if tipo == '1':
                ok = eliminar_registro_csv(id_valor, 'id')
            else:
                ok = eliminar_registro_json(id_valor, 'id')
            print("Eliminado." if ok else "No encontrado.")
        elif op == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")
