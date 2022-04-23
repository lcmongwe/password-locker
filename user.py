class User:
    """
    this class generates a new user for the password locker account
    """

    user_list=[]

    def __init__(self, locker_username,locker_password):
        self.locker_username=locker_username
        self.locker_password=locker_password
        
    