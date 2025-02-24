import unittest
import os
import sys

# Agregar la ruta del proyecto al sistema para que Python encuentre el módulo `app`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db

class InvoicesTestCase(unittest.TestCase):
    def setUp(self):
        # Crear una instancia de la aplicación en modo de prueba
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        # Crear la base de datos de prueba
        db.create_all()

    def tearDown(self):
        # Limpiar la base de datos después de cada prueba
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_list_invoices(self):
        # Prueba para el endpoint /list
        response = self.client.get('/api/v1/invoices/list')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Listado de Facturas', response.data)

    def test_capture_invoices(self):
        # Prueba para el endpoint /capture
        response = self.client.post('/api/v1/invoices/capture')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Facturas capturadas exitosamente', response.data)

if __name__ == '__main__':
    unittest.main()