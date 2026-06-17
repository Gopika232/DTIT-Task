import unittest
import os
from models.model import model

class TestFaceModel(unittest.TestCase):
    def test_model_exists(self):
        self.assertIsNotNone(model.face_cascade)

    def test_invalid_image(self):
        result = model.detect_face("wrong.jpg")
        self.assertEqual(result,"Image not found")
        
if __name__=="__main__":
    unittest.main()