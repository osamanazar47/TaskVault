import unittest
from Backend.models.user import User
from Backend.models.task import Task
from datetime import datetime

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = User(name="Test User", password_hash="testpassword")

    def test_initialization(self):
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))
        self.assertTrue(hasattr(self.model, "name"))
        self.assertTrue(hasattr(self.model, "password_hash"))
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        # Testing initialization with a specific values
        self.assertEqual(self.model.name, "Test User")
        self.assertEqual(self.model.password_hash, "testpassword")

    # Check if the pasword will hashed
    def test_set_password(self):
        user = User(name="Test User", password_hash="testpassword")
        user.set_password("newpassword")
        self.assertNotEqual(user.password_hash, "newpassword")  # Password should be hashed

    def test_check_password(self):
        user = User(name="Test User", password_hash="testpassword")
        user.set_password("newpassword")
        self.assertTrue(user.check_password("newpassword"))
        self.assertFalse(user.check_password("wrongpassword"))

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["__class__"], self.model.__class__.__name__)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    def test_edge_cases(self):
        # Test edge cases for attribute values
        model = User(name="", password_hash="")
        self.assertEqual(model.name, "")
        self.assertEqual(model.password_hash, "")


if __name__ == '__main__':
    unittest.main()