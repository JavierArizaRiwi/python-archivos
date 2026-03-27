# CRUD con Archivos CSV y JSON

Este proyecto permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre registros almacenados en archivos CSV y JSON usando diccionarios en Python.

## Estructura
- main.py: Archivo principal para ejecutar el CRUD.
- crud.py: Lógica de operaciones CRUD.
- data/: Carpeta para almacenar los archivos de datos (data.csv, data.json).

## Requisitos
- Python 3.x

## Uso
Ejecuta el archivo main.py para iniciar el programa:

```bash
python main.py
```

Sigue las instrucciones en pantalla para gestionar los registros.

---

## Explicación de instrucciones importantes

### os.path.join(carpeta, archivo)
Sirve para juntar el nombre de una carpeta y el de un archivo, así la compu sabe exactamente dónde está guardado el archivo. Es como decir: “Busca el cuaderno dentro de la caja”.

### os.path.exists(ruta)
Esto pregunta: “¿Ya existe esta caja o este cuaderno?” Si existe, responde True (sí), si no, responde False (no).

### os.makedirs(ruta)
Le dice a la compu: “Crea una caja (carpeta) con este nombre”. Si ya existe, no pasa nada. Si no existe, la crea para que puedas guardar cosas.

### with open(ARCHIVO_JSON, "r", encoding="utf-8") as archivo:
Es como abrir un cuaderno para leerlo. "r" significa que solo lo vas a leer. "utf-8" es el idioma para leer letras y acentos. Cuando terminas, la compu cierra el cuaderno sola.

### json.dump(registros, archivo, ensure_ascii=False, indent=4)
Sirve para escribir muchos papelitos (registros) dentro del cuaderno (archivo) en formato JSON. `ensure_ascii=False` deja guardar letras con acentos y ñ. `indent=4` hace que todo quede ordenado y bonito, con espacios para que sea fácil de leer.

### escritor = csv.DictWriter(archivo, fieldnames=registro.keys())
Esto crea un "escritor" especial para archivos CSV. Imagina que tienes una hoja de cálculo (como Excel) y quieres escribir filas nuevas. 
- `archivo` es la hoja donde vas a escribir.
- `fieldnames=registro.keys()` le dice qué columnas va a tener la hoja (por ejemplo: nombre, edad, id). Así, cada vez que escribas una fila, sabrá en qué columna va cada dato.

### Diferencia entre csv.DictWriter y json.dump
- **csv.DictWriter** escribe los datos como si fueran filas y columnas en una tabla. Cada registro es una fila, y cada campo (nombre, edad, etc.) es una columna. Es ideal para datos simples, como listas de personas.
- **json.dump** escribe los datos como una lista de papelitos (diccionarios), donde cada papelito puede tener información diferente y hasta cosas dentro de cosas (listas, otros diccionarios). Es más flexible y sirve para guardar datos más complejos.

### Ejemplo visual:
- **CSV:**
  | id  | nombre | edad |
  |-----|--------|------|
  | juan| Juan   | 10   |
  | ana | Ana    | 12   |

- **JSON:**
  [
    {"id": "juan", "nombre": "Juan", "edad": "10"},
    {"id": "ana", "nombre": "Ana", "edad": "12"}
  ]

En resumen: usa CSV si quieres algo como una tabla de Excel, y usa JSON si quieres guardar cosas más variadas o complejas.

---

¡Así, si alguien más ve tu código, sabrá para qué sirve cada cosa importante!
