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
        self.assertEqual(self.new_user.username,"lucy") 
        self.assertEqual(self.new_user.password,"lucy1")

    def test_save_user(self):
        """
        test if a new user instance  has been  saved
        """

        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


    def test_delete_contact(self):
        """tests if a user has been deleted succesfuly"""
        self.new_user.save_user()
        test_user= User("lucy","lucy1") 
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

   


if __name__ == '__main__':
    unittest.main()
        