from credential import Credentials

class User:
    """
    this class generates a new user for the password locker account
    """

    user_list=[]

    def __init__(self, locker_username,locker_password):
        self.locker_username=locker_username
        self.locker_password=locker_password

    def save_user(self): 
        """
        method that saves a new user
        """
        User.user_list.append(self)

    
    @classmethod
    def dispaly_user(cls):
        '''
        method that returns user details
        '''
        return cls.user_list

    def delete_user(self):
        """
        method deletes a saved account
        """
        User.user_list.remove(self)

    