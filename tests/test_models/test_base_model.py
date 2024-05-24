import unittest
from Backend.models.BaseModel import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()

    def test_initialization(self):
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["__class__"], self.model.__class__.__name__)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

if __name__ == '__main__':
    unittest.main()
