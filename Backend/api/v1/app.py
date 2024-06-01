#!/usr/bin/python3
""" Flask application """
from flask import Flask
from Backend.config import Config
from Backend.models import db
from Backend.api.v1.users import user_bp
from Backend.api.v1.tasks import task_bp
from Backend.models.task import Task
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(task_bp, url_prefix='/api')


# Route for landing page
@app.route('/', strict_slashes=False)
def landing():
    return render_template('Frontend/templates/landing_page.html')

# Route for user tasks page
@app.route('/tasks', strict_slashes=False)
def tasks():
    tasks = Task.query.all()
    return render_template('Frontend/templates/user_tasks.html', tasks=tasks)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
