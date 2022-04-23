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


    

    

    

   
   

