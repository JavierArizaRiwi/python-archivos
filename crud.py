import csv
import json
import os

DATA_CSV = os.path.join('data', 'data.csv')
DATA_JSON = os.path.join('data', 'data.json')

# Funciones CRUD para CSV

def crear_registro_csv(diccionario):
    existe = os.path.isfile(DATA_CSV)
    with open(DATA_CSV, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=diccionario.keys())
        if not existe:
            writer.writeheader()
        writer.writerow(diccionario)

def leer_registros_csv():
    if not os.path.isfile(DATA_CSV):
        return []
    with open(DATA_CSV, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def actualizar_registro_csv(id_valor, campo_id, nuevos_datos):
    registros = leer_registros_csv()
    actualizado = False
    for reg in registros:
        if reg[campo_id] == id_valor:
            reg.update(nuevos_datos)
            actualizado = True
    if actualizado:
        with open(DATA_CSV, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=registros[0].keys())
            writer.writeheader()
            writer.writerows(registros)
    return actualizado

def eliminar_registro_csv(id_valor, campo_id):
    registros = leer_registros_csv()
    nuevos = [reg for reg in registros if reg[campo_id] != id_valor]
    if len(nuevos) != len(registros):
        with open(DATA_CSV, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=registros[0].keys())
            writer.writeheader()
            writer.writerows(nuevos)
        return True
    return False

# Funciones CRUD para JSON

def crear_registro_json(diccionario):
    registros = leer_registros_json()
    registros.append(diccionario)
    with open(DATA_JSON, 'w', encoding='utf-8') as f:
        json.dump(registros, f, ensure_ascii=False, indent=2)

def leer_registros_json():
    if not os.path.isfile(DATA_JSON):
        return []
    with open(DATA_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)

def actualizar_registro_json(id_valor, campo_id, nuevos_datos):
    registros = leer_registros_json()
    actualizado = False
    for reg in registros:
        if reg[campo_id] == id_valor:
            reg.update(nuevos_datos)
            actualizado = True
    if actualizado:
        with open(DATA_JSON, 'w', encoding='utf-8') as f:
            json.dump(registros, f, ensure_ascii=False, indent=2)
    return actualizado

def eliminar_registro_json(id_valor, campo_id):
    registros = leer_registros_json()
    nuevos = [reg for reg in registros if reg[campo_id] != id_valor]
    if len(nuevos) != len(registros):
        with open(DATA_JSON, 'w', encoding='utf-8') as f:
            json.dump(nuevos, f, ensure_ascii=False, indent=2)
        return True
    return False
