import csv  # Módulo estándar para manejo de archivos CSV (texto separado por comas)
import json  # Módulo estándar para manejo de archivos JSON (texto estructurado tipo diccionario)
import os    # Módulo estándar para operaciones del sistema de archivos (rutas, existencia, etc)

# Rutas absolutas (relativas al proyecto) donde se guardarán los archivos de datos
# El archivo CSV se guardará en la carpeta 'data' con el nombre 'data.csv'
DATA_CSV = os.path.join('data', 'data.csv')    # Ejemplo de ruta: 'data/data.csv'
# El archivo JSON se guardará en la carpeta 'data' con el nombre 'data.json'
DATA_JSON = os.path.join('data', 'data.json')  # Ejemplo de ruta: 'data/data.json'


# =============================
# Funciones CRUD para archivos CSV
# =============================

def crear_registro_csv(diccionario):
    """
    Crea (si no existe) o agrega un registro al archivo CSV ubicado en la ruta DATA_CSV.
    Si el archivo no existe, lo crea y escribe la cabecera (los nombres de los campos).
    Si ya existe, solo agrega el nuevo registro al final.
    Parámetro:
        diccionario: dict con los datos del registro (las claves serán las columnas)
    """
    existe = os.path.isfile(DATA_CSV)  # Verifica si el archivo ya existe en la ruta
    with open(DATA_CSV, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=diccionario.keys())
        if not existe:
            writer.writeheader()  # Si el archivo es nuevo, escribe la cabecera (primera línea)
        writer.writerow(diccionario)  # Escribe el registro como una nueva fila

def leer_registros_csv():
    """
    Lee todos los registros del archivo CSV ubicado en la ruta DATA_CSV.
    Si el archivo no existe, retorna una lista vacía.
    Retorna:
        Lista de diccionarios, cada uno representa un registro/una fila del archivo CSV.
    """
    if not os.path.isfile(DATA_CSV):
        return []  # Si el archivo no existe, retorna lista vacía
    with open(DATA_CSV, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)  # Convierte el lector en una lista de diccionarios

def actualizar_registro_csv(id_valor, campo_id, nuevos_datos):
    """
    Busca y actualiza un registro en el archivo CSV (ruta DATA_CSV) según el valor de un campo identificador.
    Parámetros:
        id_valor: valor a buscar en el campo identificador (por ejemplo, 'id')
        campo_id: nombre del campo identificador (por ejemplo, 'id')
        nuevos_datos: diccionario con los nuevos datos para actualizar ese registro
    Retorna:
        True si se actualizó algún registro, False si no se encontró.
    """
    registros = leer_registros_csv()  # Lee todos los registros actuales
    actualizado = False
    for reg in registros:
        if reg[campo_id] == id_valor:
            reg.update(nuevos_datos)  # Actualiza los datos del registro encontrado
            actualizado = True
    if actualizado:
        # Sobrescribe el archivo con todos los registros (incluyendo el actualizado)
        with open(DATA_CSV, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=registros[0].keys())
            writer.writeheader()
            writer.writerows(registros)
            
    return actualizado

def eliminar_registro_csv(id_valor, campo_id):
    """
    Elimina un registro del archivo CSV (ruta DATA_CSV) según el valor de un campo identificador.
    Parámetros:
        id_valor: valor a buscar en el campo identificador
        campo_id: nombre del campo identificador
    Retorna:
        True si se eliminó algún registro, False si no se encontró.
    """
    registros = leer_registros_csv()
    nuevos = [reg for reg in registros if reg[campo_id] != id_valor]  # Filtra el registro a eliminar
    if len(nuevos) != len(registros):
        # Si se eliminó algún registro, sobrescribe el archivo con los registros restantes
        with open(DATA_CSV, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=registros[0].keys())
            writer.writeheader()
            writer.writerows(nuevos)
        return True
    return False

# =============================
# Funciones CRUD para archivos JSON
# =============================

def crear_registro_json(diccionario):
    """
    Crea (si no existe) o agrega un registro al archivo JSON ubicado en la ruta DATA_JSON.
    Si el archivo no existe, lo crea como una lista con el primer registro.
    Si ya existe, agrega el nuevo registro al final de la lista.
    Parámetro:
        diccionario: dict con los datos del registro
    """
    registros = leer_registros_json()  # Lee los registros existentes (o lista vacía)
    registros.append(diccionario)      # Agrega el nuevo registro
    with open(DATA_JSON, 'w', encoding='utf-8') as f:
        json.dump(registros, f, ensure_ascii=False, indent=2)  # Guarda la lista actualizada

def leer_registros_json():
    """
    Lee todos los registros del archivo JSON ubicado en la ruta DATA_JSON.
    Si el archivo no existe, retorna una lista vacía.
    Retorna:
        Lista de diccionarios, cada uno representa un registro.
    """
    if not os.path.isfile(DATA_JSON):
        return []  # Si el archivo no existe, retorna lista vacía
    with open(DATA_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)  # Carga la lista de registros desde el archivo JSON

def actualizar_registro_json(id_valor, campo_id, nuevos_datos):
    """
    Busca y actualiza un registro en el archivo JSON (ruta DATA_JSON) según el valor de un campo identificador.
    Parámetros:
        id_valor: valor a buscar en el campo identificador
        campo_id: nombre del campo identificador
        nuevos_datos: diccionario con los nuevos datos para actualizar ese registro
    Retorna:
        True si se actualizó algún registro, False si no se encontró.
    """
    registros = leer_registros_json()
    actualizado = False
    for reg in registros:
        if reg[campo_id] == id_valor:
            reg.update(nuevos_datos)  # Actualiza los datos del registro encontrado
            actualizado = True
    if actualizado:
        with open(DATA_JSON, 'w', encoding='utf-8') as f:
            json.dump(registros, f, ensure_ascii=False, indent=2)
    return actualizado

def eliminar_registro_json(id_valor, campo_id):
    """
    Elimina un registro del archivo JSON (ruta DATA_JSON) según el valor de un campo identificador.
    Parámetros:
        id_valor: valor a buscar en el campo identificador
        campo_id: nombre del campo identificador
    Retorna:
        True si se eliminó algún registro, False si no se encontró.
    """
    registros = leer_registros_json()
    nuevos = [reg for reg in registros if reg[campo_id] != id_valor]  # Filtra el registro a eliminar
    if len(nuevos) != len(registros):
        with open(DATA_JSON, 'w', encoding='utf-8') as f:
            json.dump(nuevos, f, ensure_ascii=False, indent=2)
        return True
    return False
