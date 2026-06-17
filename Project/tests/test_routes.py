import unittest
from app import app
class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_register_api(self):
        response = self.client.post("/register",
            json={"username":"apiuser","password":"123"})
        self.assertEqual(response.status_code,200)

    def test_login_api(self):
        response = self.client.post("/login",
            json={"username":"apiuser","password":"123"})
        
        self.assertEqual(response.status_code,200)

    def test_dashboard(self):
        response = self.client.get("/dashboard")
        self.assertEqual(response.status_code,200)

if __name__=="__main__":
    unittest.main()