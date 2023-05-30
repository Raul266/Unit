from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()


class BadLoginTests(unittest.TestCase):

    def login(self, user, parola):
        driver.find_element(By.ID, "user-name").send_keys(user)
        driver.find_element(By.NAME, "password").send_keys(parola)
        driver.find_element(By.ID, "login-button").click()

    def setUp(self):
        driver.get("https://www.saucedemo.com/")

    def test_login_incorect(self):
        self.login("alabala", "alabala")

        actual = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        expected = "Epic sadface: Username and password do not match any user in this service"

        assert actual == expected, f"Mesajul de eroare nu e corect, ne asteptam la mesajul {expected}, " \
             f"dar a fost afisat {actual}"

        self.assertEqual(expected, actual, "Mesajul de eroare nu e corect")
        actual = driver.current_url
        expected = "https://www.saucedemo.com/"

        self.assertEqual(expected, actual, "Am reusit sa ne logam cu credentialele incorecte")


    def test_login_user_blocat(self):
        self.login("locked_out_user", "secret_sauce")

        actual = driver.find_element(By.TAG_NAME, "h3").text
        expected = "Epic sadface: Sorry, this user has been locked out."

        # assert actual == expected, f"Mesajul nu este cel pe care il asteptam: {expected}; mesajul afisat a fost {actual}"
        self.assertEqual(actual, expected, "Mesajul nu este cel pe care il asteptam")

    def test_login_parola_lipsa(self):
        self.login("standard_user", "")

        expected = "Epic sadface: Password is required"
        actual = driver.find_element(By.TAG_NAME, "h3").text

        self.assertEqual(expected, actual, "Mesajul de eroare nu e corect")
