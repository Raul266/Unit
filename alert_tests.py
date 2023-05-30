import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()


class AlertTests(unittest.TestCase):

    def test_context_menu_alert(self):
        """
        Exemplu de context menu + alert
        Context menu - element pe care actionam cu right-click, folosind ActionChains
        ActionsChains - ne ajuta sa executam diferite actiuni cum ar fi: right-click, double-click, drag and drop, etc
        Alert simplu - element creat de javascript care are doar un buton Ok
        """
        chrome.get("https://the-internet.herokuapp.com/context_menu")
        action = ActionChains(chrome)
        action.context_click(chrome.find_element(By.ID, "hot-spot")).perform()

        alert = chrome.switch_to.alert

        self.assertEqual(alert.text, "You selected a context menu")

        alert.accept()

    def test_confirm_box(self):
        """
        Exemplu de confirm box
        Confirm box - element creat de javascript care are doua butoane: Cancel/Ok
        """
        chrome.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
        chrome.find_element(By.ID, "confirmexample").click()

        chrome.switch_to.alert.dismiss()

        actual = chrome.find_element(By.ID, "confirmreturn").text
        expected = "false"

        self.assertEqual(actual, expected)

    def test_prompt_box(self):
        """
        Exemplu de prompt box
        Prompt box - element creat de javascript care are un camp de text si doua butoane: Cancel/Ok
        """
        chrome.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
        chrome.find_element(By.XPATH, "//*[@id='promptexample']").click()

        alert = chrome.switch_to.alert
        alert.send_keys("Nume")
        alert.accept()

        self.assertEqual("Nume", chrome.find_element(By.ID, "promptreturn").text)
