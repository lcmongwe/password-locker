
import unittest
from credential import Credentials


class TestCredentials(unittest.TestCase):
    def setUp(self):

        self.new_credentials=Credentials("twitter","lcmongwe","xyz",)
    def tearDown(self):
        Credentials.credentials_list=[]

    def test_init(self):
        self.assertEqual(self.new_credentials.app_name,"twitter") 
        self.assertEqual(self.new_credentials.user_name,"lcmongwe") 
        self.assertEqual(self.new_credentials.password,"xyz") 
          
    def test_save_credential(self):
        self.new_credentials.save_contact()
        self.assertEqual(len(Contact.contact_list),1)