import unittest
from Backend.models.task import Task
from datetime import datetime

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = Task()

    def test_initialization(self):
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))
        self.assertTrue(hasattr(self.model, "title"))
        self.assertTrue(hasattr(self.model, "description"))
        self.assertTrue(hasattr(self.model, "due_date"))
        self.assertTrue(hasattr(self.model, "user_id"))
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        # Testing initialization with a specific values
        model = Task(title="Test Task", description="Test Description", due_date=datetime(2024, 6, 30), user_id="123")
        self.assertEqual(model.title, "Test Task")
        self.assertEqual(model.description, "Test Description")
        self.assertEqual(model.due_date, datetime(2024, 6, 30))
        self.assertEqual(model.user_id, "123")

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["__class__"], self.model.__class__.__name__)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    def test_edge_cases(self):
        # Test edge cases for attribute values
        model = Task(title="", description="", due_date=datetime(1970, 1, 1), user_id="")
        self.assertEqual(model.title, "")
        self.assertEqual(model.description, "")
        self.assertEqual(model.due_date, datetime(1970, 1, 1))
        self.assertEqual(model.user_id, "")

if __name__ == '__main__':
    unittest.main()
