from credential import Credentials

class User:
    """
    this class generates a new user for the password locker account
    """

    user_list=[]

    def __init__(self, username,password):
        self.username=username
        self.password=password

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

    @classmethod
    def verify_user(cls,username, password):
        """
        method to verify whether the user is in our user_list or not
        """
        now_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                    now_user == user.username
        return now_user
    