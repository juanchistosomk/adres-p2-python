# ADRES Prueba Técnica: Python Flask - Captura y Listado de Facturas

## Por: JUAN CARLOS CASTILLO G.

Este proyecto es una aplicación web desarrollada con Flask que permite capturar y listar facturas a partir de archivos PDF. Las facturas se almacenan en una base de datos SQLite, y la aplicación incluye un endpoint para capturar los datos y una vista HTML para listarlos.

![Logo del proyecto](https://iili.io/3JHe8lt.md.png)

## Características

- Captura de datos de facturas desde archivos PDF.
- Almacenamiento en una base de datos SQLite.
- Vista HTML para listar las facturas capturadas.
- Pruebas unitarias para garantizar el correcto funcionamiento.

## Requisitos

- Python 3.7 o superior.
- Flask.
- PyPDF2.
- SQLite3.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/juanchistosomk/adres-p2-python.git
   cd prueba_tecnica_dos
   ```

### 2. Comandos crear entorno virtual python:

```bash
python -m venv env
```

```bash
.\env\Scripts\activate
```

### 3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el proyecto:

```bash
python run.py
```

### 5. Abrir URL:

http://localhost:5000
