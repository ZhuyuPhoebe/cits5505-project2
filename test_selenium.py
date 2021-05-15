import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def login(self):
    driver = self.driver
    driver.get("http://127.0.0.1:5000/")

    # login
    driver.find_element_by_name('username').send_keys('root')
    driver.find_element_by_name('password').send_keys('root')

    # submit
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/div[4]/button').click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "banner"))
    )

class TestPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        login(self)

    def test_index_2_learn(self):
        login(self)
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="1"]/td[3]/a[1]').click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "learn_box"))
        )

    def test_index_2_quiz(self):
        login(self)
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="1"]/td[3]/a[2]').click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "quiz_box"))
        )

    def test_index_2_about_us(self):
        login(self)
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div[5]/div/a').click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "aboutus_box"))
        )

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()