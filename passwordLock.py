#!/usr/bin/env python3.8
from user import User
from credential import Credentials

def create_new_user(username,password):
    """
    function creates a new user with username and password
    """
    new_user=User(username,password)
    return new_user