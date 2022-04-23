class Credentials:
    """
    this class generate credentials for a user
    """

    Credentials_list=[]

    def __init__(self,app_name, user_name,password):
        self.app_name=app_name
        self.user_name=user_name
        self.password=password
        