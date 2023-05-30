from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


driver = webdriver.Chrome()


class GoodLoginTests(unittest.TestCase):

    def login(self, user, parola):
        driver.find_element(By.ID, "user-name").send_keys(user)
        driver.find_element(By.NAME, "password").send_keys(parola)
        driver.find_element(By.ID, "login-button").click()

    def setUp(self):
        driver.get("https://www.saucedemo.com/")

    def tearDown(self):
        driver.quit()

    def test_login_standard(self):
        self.login("standard_user", "secret_sauce")

        expected = "https://www.saucedemo.com/inventory.html"
        actual = driver.current_url

        self.assertEqual(expected, actual, "Nu suntem pe pagina la care ne asteptam")
