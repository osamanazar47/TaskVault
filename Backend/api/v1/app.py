#!/usr/bin/python3
""" Flask application """
from flask import Flask
from Backend.config import Config
from Backend.models import db
from Backend.api.v1.users import user_bp
from Backend.api.v1.tasks import task_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(task_bp, url_prefix='/api')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
