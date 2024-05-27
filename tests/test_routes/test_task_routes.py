import unittest
from flask import Flask, json
from flask_jwt_extended import create_access_token, JWTManager
from Backend.models import db
from Backend.models.user import User
from Backend.api.v1.users import user_bp
from Backend.models.task import Task
from Backend.api.v1.tasks import task_bp
from datetime import datetime


class TestTaskRoutes(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['JWT_SECRET_KEY'] = 'osama_nazar'
        db.init_app(self.app)
        self.jwt = JWTManager(self.app)
        self.app.register_blueprint(user_bp, url_prefix='/api')
        self.app.register_blueprint(task_bp, url_prefix='/api')

        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            self.user = User(name='testuser')
            self.user.set_password('testpassword')
            db.session.add(self.user)
            db.session.commit()
            self.user_id = self.user.id
            self.access_token = create_access_token(identity={'id': self.user_id, 'name': 'testuser'})

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_tasks(self):
        with self.app.app_context():
            task = Task(title='Test Task', description='Task description', due_date=datetime(2024, 12, 31), user_id=self.user_id)
            db.session.add(task)
            db.session.commit()
        response = self.client.get(f'/api/users/{self.user_id}/tasks', headers={
            'Authorization': f'Bearer {self.access_token}'
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertTrue(len(data) > 0)

    def test_create_task(self):
        task_data = {
            'title': 'New Task',
            'description': 'New Task description',
            'due_date': datetime.now().isoformat(),
        }
        response = self.client.post(f'/api/users/{self.user_id}/tasks', json=task_data, headers={
            'Authorization': f'Bearer {self.access_token}'
        })
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['title'], 'New Task')

    def test_get_task(self):
        with self.app.app_context():
            task = Task(title='Test Task', description='Task description', due_date=datetime(2024, 12, 31), user_id=self.user_id)
            db.session.add(task)
            db.session.commit()
            task_id = task.id
        response = self.client.get(f'/api/users/{self.user_id}/tasks/{task_id}', headers={
            'Authorization': f'Bearer {self.access_token}'
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['title'], 'Test Task')

    def test_update_task(self):
        with self.app.app_context():
            task = Task(title='Test Task', description='Task description', due_date=datetime(2024, 12, 31), user_id=self.user_id)
            db.session.add(task)
            db.session.commit()
            task_id = task.id
        updated_task_data = {
            'title': 'Updated Task',
            'description': 'Updated description',
            'due_date': datetime.now().isoformat()
        }
        response = self.client.put(f'/api/users/{self.user_id}/tasks/{task_id}', json=updated_task_data, headers={
            'Authorization': f'Bearer {self.access_token}'
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['title'], 'Updated Task')
        self.assertEqual(data['description'], 'Updated description')

    def test_delete_task(self):
        with self.app.app_context():
            task = Task(title='Test Task', description='Task description', due_date=datetime(2024, 12, 31), user_id=self.user_id)
            db.session.add(task)
            db.session.commit()
            task_id = task.id
        response = self.client.delete(f'/api/users/{self.user_id}/tasks/{task_id}', headers={
            'Authorization': f'Bearer {self.access_token}'
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['message'], 'Task deleted successfully')

if __name__ == '__main__':
    unittest.main()
