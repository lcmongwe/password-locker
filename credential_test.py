
import unittest
from credential import Credentials


class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_credentials=Credentials("twitter","lcmongwe","xyz",)

    def tearDown(self):
        Credentials.credentials_list=[]

        """tests if an object instance has been created correctly"""

    def test_init(self):
        self.assertEqual(self.new_credentials.app_name,"twitter") 
        self.assertEqual(self.new_credentials.user_name,"lcmongwe") 
        self.assertEqual(self.new_credentials.password,"xyz") 

           
    def test_save_credential(self):
        """tests if a new credential has been created and saved correctly"""
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

        
    def test_save_new_credentials(self):
        """tests if a new credential has been created and saved correctly"""
        self.new_credentials.save_credentials()
        test_credentilas = Credentials("tiktok","lucy","123") 
        test_credentilas.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)   

    def test_display_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
    
    def test_delete_credentials(self):
        self.new_credentials.save_credentials()
        test_credentials = Credentials("tiktok","lucy","123",) 
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)



if __name__ == '__main__':
    unittest.main()