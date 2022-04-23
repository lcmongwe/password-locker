
import unittest
from credential import Credentials


class TestCredentials(unittest.TestCase):
    def setUp(self):

        self.new_credentials=Credentials("twitter","lcmongwe","xyz",)
    def tearDown(self):
        Credentials.credentials_list=[]