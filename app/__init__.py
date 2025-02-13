from flask import Flask
from flask_cors import CORS
import logging

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['JSON_AS_ASCII'] = False

    logging.basicConfig(filename='log/agentes.log', level=logging.INFO, format='%(asctime)s %(message)s')
    logging.info("Aplicação iniciada e logging configurado.")

    with app.app_context():
        from . import routes
        app.register_blueprint(routes.bp)

    return app
