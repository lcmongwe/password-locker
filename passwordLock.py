#!/usr/bin/env python3.8
import random
import string
from user import User
from credential import Credentials

def create_new_user(username,password):
    """
    function creates a new user with username and password
    """
    new_user=User(username,password)
    return new_user

def save_user(user):
    """
    function saves a new user
    """
    user.save_user()

def display_user():
    """
    function displays existing user
    """
    return User.dispaly_user()

def login_user(username,password):
    """
    function checks if a user exists and logs them in if username an password match
    """
    check_user=User.verify_user(username,password)
    return check_user

def create_new_credentials(app_name,user_name,password):
    """
    function creates new credentials for given user account
    """
    new_credential=Credentials(app_name,user_name,password)
    return new_credential

def save_credentials(credentials):
    """
    function saves credentials to the list
    """
    Credentials.save_credentials(credentials)

def display_credentials():
    """
    function displays all saved credentials
    """
    return Credentials.display_credentials()

def delete_credentials(credentials):
    """
    function deletes saved credentials
    """
    Credentials.delete_credentials()

def find_credentials(app_name):
    """
    finds credentials by searching the app_name
    """
    return Credentials.find_credential(app_name)

def check_credentials(app_name):
    """
    function cehcks if credentials exist
    """
    return Credentials.if_credential_exist(app_name)

def generate_password():
    auto_password=Credentials.generatePassword()
    return auto_password

def locker():
    print("Hello Welcome to passwordlocker...\n  Enter one of the codes to proceed.\n CA ---  Create New Account  \n LI ---  Have An Account  \n")
    short_code=input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('*' * 50)
        username = input("User_name: ")
        while True:
            print(" TP -  Type your own pasword:\n GP -  Generate random Password")
            choice = input().lower().strip()
            if choice == 'tp':
                password = input("Enter Password\n")
                break
            elif choice == 'gp':
                password = generate_password()
                break
            else:
                print("Invalid password please try again")
        save_user(create_new_user(username,password))
        print("*"*60)
        print(f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
        print("*"*60)
    elif short_code == "li":
        print("*"*50)
        print("Enter your User name and your Password to log in:")
        print('*' * 50)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hi! {username}.Welcome To PassWord Locker ")  
            print('\n')
    while True:
        print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("."*20)
            print("Account name ....")
            app_name = input().lower()
            print("Your Account username")
            user_name = input()
            while True:
                print(" TP - To type your own pasword if you already have an account:\n GP - To generate random Password")
                choice = input().lower().strip()
                if choice == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
                elif choice == 'gp':
                    password = generate_password()
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_new_credentials(app_name,user_name,password))
            print('\n')
            print(f"Account Credential for: {app_name} - UserName: {user_name} - Password:{password} created succesfully")
            print('\n')
        elif short_code == "dc":
            if display_credentials():
                print("Here's your list of accounts: ")
                 
                print('*' * 30)
                
                for account in display_credentials():
                    print(f" Account:{account.app_name} \n User Name:{account.user_name}\n Password:{account.password}")
                    
                print('*' * 30)
            else:
                print("You don't have any credentials saved yet..........")
        elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credentials(search_name):
                search_credential = find_credentials(search_name)
                print(f"Account Name : {search_credential.app_name}")
                print('-' * 50)
                print(f"User Name: {search_credential.user_name} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print("That Credential does not exist")
                print('\n')
        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credentials(search_name):
                search_credential = find_credentials(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.app_name} successfully deleted!!!")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")

        elif short_code == 'gp':

            password = generate_password()
            print(f" {password} Has been generated succesfull. You can proceed to use it to your account")
        elif short_code == 'ex':
            print("Thanks for using passwords store manager.. See you next time!")
            break
        else:
            print("Wrong entry... Check your entry again and let it match those in the menu")
    else:
        print("Please enter a valid input to continue")

if __name__ == '__main__':
    locker()