from flask import request, jsonify, render_template, request, current_app, redirect, url_for
from datetime import datetime
from PyPDF2 import PdfReader
import sqlite3, os, re
from . import invoices_bp

HOY = datetime.today().strftime('%Y-%m-%d')

@invoices_bp.route('/capture', methods=['GET','POST'])
def capture_invoices():
    '''
    Captura y guarda en SQLite las facturas de formato PDF
    '''

    if request.method == 'POST':

        try:
        
            pdf_folder = os.path.join(os.getcwd(), 'public')
            pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf') or f.endswith('.PDF')]

            db = sqlite3.connect(current_app.config['DATABASE'])
            cursor = db.cursor()
            #print("HOLAAAA__22222: ", pdf_folder, " ____ " , pdf_files)


             # Verificar si la tabla 'invoices' existe
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='invoices'")
            table_exists = cursor.fetchone()
            if not table_exists:
                print("🔴 La tabla 'invoices' no existe. Creándola...")
                with current_app.open_resource('../schema.sql', mode='r') as f:
                    db.cursor().executescript(f.read())
                db.commit()


            for pdf_file in pdf_files:
                pdf_path = os.path.join(pdf_folder, pdf_file)
                reader = PdfReader(pdf_path)
                num_pages = len(reader.pages)

                cufe = ""
                cufe = extract_cufe_from_pdf(pdf_path)
                if not cufe:
                    print("🔴No se encontró el CUFE en el PDF.")
                    continue
                
                file_size = os.path.getsize(pdf_path) / 1024  # Peso en KB

                #print("PDF: ", pdf_file, num_pages, cufe, file_size)

                cursor.execute('''
                    INSERT INTO invoices (nombre_archivo, numero_paginas, CUFE, peso_archivo)
                    VALUES (?, ?, ?, ?)
                ''', (pdf_file, num_pages, cufe, file_size))

            db.commit()
            db.close()

        except Exception as e:
            print(f"🔴 Error al capturar facturas: {e}")


    return redirect(url_for('invoices.list_invoices'))
    


def extract_cufe_from_pdf(pdf_path):
    '''
    Extraer CUFE del PDF
    '''
    reader = PdfReader(pdf_path)
    text = ""


    for page in reader.pages:
        text += page.extract_text()

    cufe_pattern = r"(\b([0-9a-fA-F]\n*){95,100}\b)"
    match = re.search(cufe_pattern, text)
    
    if match:
        return match.group(1)
    else:
        return None




@invoices_bp.route('/list', methods=['GET'])
def list_invoices():
    '''
    Listado de facturas capturadas
    '''
    try:
        db = sqlite3.connect(current_app.config['DATABASE'])
        cursor = db.cursor()
        cursor.execute('SELECT * FROM invoices')
        invoices = cursor.fetchall()
        #print("Invoices: ", invoices)
        db.close()

        return render_template('index.html', invoices=invoices)
    
    except Exception as e:
        print(f"Error al listar las facturas: {e}")
        return render_template('index.html', invoices=[])