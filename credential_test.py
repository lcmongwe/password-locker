
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

        
    def test_save_multiple_credentials(self):
        """tests if a new credentials has been created and saved correctly"""
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

def test_find_credential(self):
        """
        test to check if we can find a credential by appname and display the details of the credential
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("tiktok","lucy","123",) 
        test_credentials.save_credentials()

        this_credential = Credentials.find_credential("tiktok")

        self.assertEqual(this_credential.app_name,test_credentials.app_name)


if __name__ == '__main__':
    unittest.main()