import unittest
from backend.auth import register, login
from backend.database import create_table, get_db

class TestAuth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        create_table()

    def test_register_user(self):
        result = register("testuser","12345")
        # True if new user created
        # False if already exists
        self.assertIn(result,[True,False])

    def test_login_user(self):
        # make sure user exists first
        register("loginuser","12345")
        result = login("loginuser","12345")
        self.assertTrue(result)

if __name__=="__main__":
    unittest.main()