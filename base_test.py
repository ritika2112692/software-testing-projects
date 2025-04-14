import unittest
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseTest(unittest.TestCase):

    def setUp(self):
        service = Service("C:/Users/hp/Desktop/login/New folder (2)/msedgedriver.exe")
        self.driver = webdriver.Edge(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("file:///C:/Users/hp/Desktop/login/New%20folder%20(2)/enhanced_todo_list.html")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    def sign_up_if_needed(self):
        driver = self.driver
        try:
            driver.find_element(By.LINK_TEXT, "Sign up").click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "new-username")))
            driver.find_element(By.ID, "new-username").send_keys("testuser")
            driver.find_element(By.ID, "new-password").send_keys("test123")
            driver.find_element(By.ID, "confirm-password").send_keys("test123")
            driver.find_element(By.XPATH, "//button[contains(text(),'Sign Up')]").click()
        except Exception:
            print("Sign-up skipped (already done).")

    def login(self):
        driver = self.driver
        try:
            driver.find_element(By.LINK_TEXT, "Login").click()
        except:
            pass
        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "password").send_keys("test123")
        driver.find_element(By.TAG_NAME, "button").click()
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Welcome, testuser!")
        )