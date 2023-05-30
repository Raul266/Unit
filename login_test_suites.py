import unittest
from unittest import TestSuite, TestLoader

from HTMLTestRunner import HTMLTestRunner

from bad_login_tests import BadLoginTests
from good_login_tests import GoodLoginTests


class LoginTestsSuite(unittest.TestCase):
    """
    De instalat: pip install HTMLTestRunner-rv
    Documentatie: https://ravikiranb36.github.io/htmltestrunner-rv.github.io/
    Exemplu clasa de test suite - gruparea a mai multor clase de test + report html
    Dupa rulare, se va crea un folder in proiectul curent cu raportul in format html, care se poate deschide in orice browser
    """

    def tests_suite(self):
        login_tests = TestSuite()

        login_tests.addTests([
            TestLoader().loadTestsFromTestCase(BadLoginTests),
            TestLoader().loadTestsFromTestCase(GoodLoginTests)
        ])

        runner = HTMLTestRunner(
            title="All Login Tests",
            verbosity=1,
            description="Good and bad login tests",
            tested_by="Raul",
            report_name="LoginTests"
        )

        runner.run(login_tests)
