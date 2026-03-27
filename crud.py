import csv  # Esto sirve para trabajar con archivos tipo Excel (CSV)
import json  # Esto sirve para trabajar con archivos tipo texto ordenado (JSON)
import os    # Esto sirve para manejar carpetas y archivos en la compu

# Aquí decimos dónde se van a guardar los archivos de datos
CARPETA_DATA = "data"  # Carpeta donde van los archivos
ARCHIVO_CSV = os.path.join(CARPETA_DATA, "data.csv")  # Archivo para guardar en formato tabla
ARCHIVO_JSON = os.path.join(CARPETA_DATA, "data.json")  # Archivo para guardar en formato lista

# Esta función revisa si la carpeta existe. Si no existe, la crea.
def crear_carpeta_si_no_existe():
    if not os.path.exists(CARPETA_DATA):
        os.makedirs(CARPETA_DATA)

# ========== PARTE DE JSON ==========
# JSON es como una caja donde guardamos muchos papelitos (diccionarios)
# Cada papelito tiene información de una persona, por ejemplo.

def leer_registros_json():
    # Lee todos los papelitos de la caja (archivo JSON)
    if not os.path.exists(ARCHIVO_JSON):
        return []  # Si la caja no existe, regresamos una caja vacía
    with open(ARCHIVO_JSON, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def guardar_registros_json(registros):
    # Guarda todos los papelitos en la caja (archivo JSON)
    crear_carpeta_si_no_existe()  # Asegúrate de que la caja existe
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as archivo:
        json.dump(registros, archivo, ensure_ascii=False, indent=4)

def crear_registro_json(registro):
    # Agrega un nuevo papelito a la caja
    registros = leer_registros_json()  # Saca todos los papelitos
    registros.append(registro)         # Mete el nuevo papelito
    guardar_registros_json(registros)  # Guarda la caja de nuevo

def actualizar_registro_json(id_valor, campo_id, nuevos_datos):
    # Busca un papelito por su nombre (o lo que le digas) y lo cambia
    registros = leer_registros_json()
    for registro in registros:
        if registro.get(campo_id) == id_valor:
            registro.update(nuevos_datos)  # Cambia los datos del papelito
            guardar_registros_json(registros)  # Guarda la caja de nuevo
            return True  # Sí lo encontró y lo cambió
    return False  # No encontró ningún papelito con ese nombre

def eliminar_registro_json(id_valor, campo_id):
    # Saca un papelito de la caja si coincide con el nombre (o lo que le digas)
    registros = leer_registros_json()
    nuevos_registros = []
    eliminado = False
    for registro in registros:
        if registro.get(campo_id) == id_valor:
            eliminado = True  # Encontró el papelito y no lo mete de nuevo
        else:
            nuevos_registros.append(registro)  # Mete los demás papelitos
    if eliminado:
        guardar_registros_json(nuevos_registros)  # Guarda la caja sin ese papelito
    return eliminado

# ========== PARTE DE CSV ==========
# CSV es como una hoja de cálculo (tipo Excel) donde cada fila es una persona

def leer_registros_csv():
    # Lee todas las filas de la hoja (archivo CSV)
    if not os.path.exists(ARCHIVO_CSV):
        return []  # Si la hoja no existe, regresamos una hoja vacía
    with open(ARCHIVO_CSV, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)

def crear_registro_csv(registro):
    # Agrega una nueva fila a la hoja (archivo CSV)
    crear_carpeta_si_no_existe()  # Asegúrate de que la hoja existe
    archivo_existe = os.path.exists(ARCHIVO_CSV)
    with open(ARCHIVO_CSV, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=registro.keys())
        if not archivo_existe:
            escritor.writeheader()  # Si es la primera vez, escribe los títulos de las columnas
        escritor.writerow(registro)  # Escribe la nueva fila

def actualizar_registro_csv(id_valor, campo_id, nuevos_datos):
    # Busca una fila por su nombre (o lo que le digas) y la cambia
    registros = leer_registros_csv()
    if len(registros) == 0:
        return False  # Si no hay filas, no hay nada que cambiar
    actualizado = False
    for registro in registros:
        if registro.get(campo_id) == id_valor:
            registro.update(nuevos_datos)  # Cambia los datos de la fila
            actualizado = True
            break
    if actualizado:
        with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=registros[0].keys())
            escritor.writeheader()
            escritor.writerows(registros)  # Escribe todas las filas de nuevo
    return actualizado

def eliminar_registro_csv(id_valor, campo_id):
    # Saca una fila de la hoja si coincide con el nombre (o lo que le digas)
    registros = leer_registros_csv()
    if len(registros) == 0:
        return False  # Si no hay filas, no hay nada que borrar
    nuevos_registros = []
    eliminado = False
    for registro in registros:
        if registro.get(campo_id) == id_valor:
            eliminado = True  # Encontró la fila y no la mete de nuevo
        else:
            nuevos_registros.append(registro)  # Mete las demás filas
    if eliminado:
        with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=registros[0].keys())
            escritor.writeheader()
            escritor.writerows(nuevos_registros)  # Escribe todas las filas menos la borrada
    return eliminado