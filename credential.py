import random
import string

class Credentials:
    """
    this class generate credentials for a user
    """

    credentials_list=[]

    def __init__(self,app_name, user_name,password):
        self.app_name=app_name
        self.user_name=user_name
        self.password=password
        
    

    def save_credentials(self): 
        """
        method that saves credetials
        """
        Credentials.credentials_list.append(self)

       
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list

    def delete_credentials(self):
        """
        method deletes credentials
        """
        Credentials.credentials_list.remove(self)


    @classmethod
    def find_credential(cls, app_name):
        """
        Method that takes in a app_name and returns a credential that app.
        """
        for credential in cls.credentials_list:
            if credential.app_name == app_name:
                return credential
    
    @classmethod
    def if_credential_exist(cls, app_name):
        """
        Method that checks if a credential exists from the credential list and returns true or false.
        """
        for credential in cls.credentials_list:
            if credential.app_name == app_name:
                return True
            return False
    
    def generatePassword(stringLength=8):
        """Generate a random password string of letters and digits and special characters"""
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "&*"
        return ''.join(random.choice(password) for i in range(stringLength))

    

    

   
   

