import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user=User("lucy","lucy1")

    def tearDown(self):
        User.user_list=[]

        """
        tests if an user instance has been created correctly
        """

    def test_init(self):
        self.assertEqual(self.new_user.locker_username,"lucy") 
        self.assertEqual(self.new_user.locker_password,"lucy1")




if __name__ == '__main__':
    unittest.main()
        