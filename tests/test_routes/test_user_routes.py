import unittest
from flask import Flask
from Backend.api.v1.app import app
from Backend.models import db
from Backend.models.user import User
from Backend.api.v1.users import user_bp
from flask_jwt_extended import JWTManager
from flask import json

class TestUserRoutes(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use SQLite for testing
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['JWT_SECRET_KEY'] = 'osama_nazar'
        db.init_app(self.app)
        self.jwt = JWTManager(self.app)
        self.app.register_blueprint(user_bp, url_prefix='/api')

        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()  # Create the database tables

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()  # Drop all tables after each test

    def test_register_user(self):
        response = self.client.post('/api/register', json={
            'name': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('User registered successfully', response.get_data(as_text=True))

    def test_login_user(self):
        with self.app.app_context():
            user = User(name='testuser')
            user.set_password('testpassword')
            db.session.add(user)
            db.session.commit()

        response = self.client.post('/api/login', json={
            'name': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('access_token', data)

    def test_get_users(self):
        with self.app.app_context():
            user = User(name='testuser')
            user.set_password('testpassword')
            db.session.add(user)
            db.session.commit()

        response = self.client.get('/api/users', headers={
            'Authorization': f'Bearer {self.get_access_token()}'
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertTrue(len(data) > 0)

    def test_get_user_by_id(self):
        with self.app.app_context():
            user = User(name='testuser')
            user.set_password('testpassword')
            db.session.add(user)
            db.session.commit()
            user_id = user.id

        response = self.client.get(f'/api/users/{user_id}', headers={
            'Authorization': f'Bearer {self.get_access_token()}'
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['id'], str(user_id))

    def test_update_user(self):
        with self.app.app_context():
            user = User(name='testuser')
            user.set_password('testpassword')
            db.session.add(user)
            db.session.commit()
            user_id = user.id

        updated_data = {
            'name': 'updateduser',
            'password': 'updatedpassword'
        }

        response = self.client.put(f'/api/users/{user_id}', json=updated_data, headers={
            'Authorization': f'Bearer {self.get_access_token()}'
        })
        self.assertEqual(response.status_code, 200)

        # Verify the update in the database
        with self.app.app_context():
            updated_user = db.session.get(User, user_id)
            self.assertEqual(updated_user.name, 'updateduser')


    def test_delete_user(self):
        with self.app.app_context():
            user = User(name='testuser')
            user.set_password('testpassword')
            db.session.add(user)
            db.session.commit()
            user_id = user.id

        access_token = self.get_access_token()

        response = self.client.delete(f'/api/users/{user_id}', headers={'Authorization': f'Bearer {access_token}'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))

    def get_access_token(self):
        response = self.client.post('/api/login', json={
            'name': 'testuser',
            'password': 'testpassword'
        })
        data = json.loads(response.get_data(as_text=True))
        return data['access_token']

if __name__ == '__main__':
    unittest.main()
