#!/usr/bin/python3
""" Flask application """
from flask import Flask
from config import Config
from models import db
from users import users_bp
from tasks import tasks_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(users_blueprint, url_prefix='/api')
app.register_blueprint(tasks_blueprint, url_prefix='/api')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    