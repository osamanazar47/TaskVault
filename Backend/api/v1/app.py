#!/usr/bin/python3
""" Flask application """
from flask import Flask
from config import Config
from models import db
from flask_migrate import Migrate
from api.v1.users import user_bp
from api.v1.tasks import task_bp
from models.task import Task
from flask_jwt_extended import JWTManager
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,
            template_folder='../../../Frontend/templates',
            static_folder='../../../Frontend/static')
app.config.from_object(Config)
db.init_app(app)
jwt = JWTManager(app)

migrate = Migrate(app, db)

app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(task_bp, url_prefix='/api')


# Route for landing page
@app.route('/', strict_slashes=False)
def landing():
    return render_template('landing_page.html')

# Route for user tasks page
@app.route('/tasks/<user_id>', strict_slashes=False)
def tasks(user_id):
    tasks = Task.query.filter_by(user_id=user_id).all()
    return render_template('user_tasks.html', tasks=tasks ,user_id=user_id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
