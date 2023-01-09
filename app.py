import os
from flask import Flask, jsonify
from flask_cors import CORS
from models import db

app = Flask(__name__, static_url_path='/static')
app.config.from_object('config')


#API Controllers
from controller.api_project_controller import mod_api_project
app.register_blueprint(mod_api_project)
db.app = app
db.init_app(app)
# Crear base de datos
with app.app_context():
	db.create_all()

basedir = os.path.abspath(os.path.dirname(__file__))

@app.errorhandler(500)
def internal_server_error(error):
	app.logger.error('Server Error: %s', (error))
	return jsonify({"Error": ["500 - Error de Servidor"]}), 500

@app.errorhandler(AttributeError)
def internal_server_error(error):
	app.logger.error('AttributeError: %s', (error))
	return jsonify({"Error": ["AttributeError: "+error]}), 500


#if __name__ == '__main__':
#    app.run()
