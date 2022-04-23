class Credentials:
    """
    this class generate credentials for a user
    """

    credentials_list=[]

    def __init__(self,app_name, user_name,password):
        self.app_name=app_name
        self.user_name=user_name
        self.password=password
        
    """method that saves credetials"""

    def save_credentials(self): 
        Credentials.credentials_list.append(self)

    # def delete_contact(self):
    #      Contact.contact_list.remove(self)

    # @classmethod
    # def find_by_number(cls,number):
    #     for contact in cls.contact_list:
    #         if contact.phone_number == number:
    #             return contact

    # @classmethod
    # def contact_exist(cls,number):
    #         for contact in cls.contact_list:
    #             if contact.phone_number == number:
    #                 return True

    #         return False

    # @classmethod
    # def display_contacts(cls):
    #     '''
    #     method that returns the contact list
    #     '''
    #     return cls.contact_list

