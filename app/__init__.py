from flask import Flask
from flask_restx import Api  # documentation for flask_restplus
import sqlite3, os

def create_app():

    app = Flask(__name__)
      
    # Configuracion de app
    app.config.from_object('config.Config')


    # Conexión base de datos
    def get_db():
        db = sqlite3.connect(app.config['DATABASE'])
        db.row_factory = sqlite3.Row
        return db

    def init_db():
        with app.app_context():
            db = get_db()            
            with app.open_resource('../schema.sql', mode='r') as f:
                db.cursor().executescript(f.read())
            db.commit()
                  

    ## Crea la BD si no existe
    if not os.path.exists(app.config['DATABASE']):
        init_db()


    # Blueprints
    from .routes.main import main_bp
    app.register_blueprint(main_bp)  

    from .api.v1.invoices import invoices_bp   
    app.register_blueprint(invoices_bp, url_prefix='/api/v1/invoices')

    # # Registro de namespaces con la API
    # from .api.v1.linkedin import linkedin_ns
    # api.add_namespace(linkedin_ns, path='/api/v1/linkedin')

    return app


