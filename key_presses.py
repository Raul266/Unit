import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()


class KeyPresses(unittest.TestCase):

    def test_key_press(self):
        """
        Exemplu de key presses (actiuni diferite de la tastatura/mouse: Backspace, Delete, CTRL, etc)
        """
        chrome.get("https://the-internet.herokuapp.com/key_presses?")
        text_field = chrome.find_element(By.ID, "target")
        text_field.send_keys("Vreau sa sterg ultimele 3 litere")
        text_field.send_keys(Keys.BACKSPACE * 10)
        sleep(5)
