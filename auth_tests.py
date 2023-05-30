import unittest
from time import sleep

from selenium import webdriver

chrome = webdriver.Chrome()


class AuthTests(unittest.TestCase):

    def test_basic_auth(self):
        '''
        Exemplu de autentificare basic
        '''
        chrome.get("https://utilizator:parola@the-internet.herokuapp.com/basic_auth")
        sleep(2)
