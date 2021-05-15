import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def login(self):
    driver = self.driver
    driver.get("http://127.0.0.1:5000/")

    driver.find_element_by_name('username').send_keys('root')
    driver.find_element_by_name('password').send_keys('root')

    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/div[4]/button').click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "banner"))
    )

class TestPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_learn_2_learn_sections(self):
        login(self)
        driver = self.driver
        # to learn
        driver.find_element_by_xpath('//*[@id="1"]/td[3]/a[1]').click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "quiz-btn"))
        )
        # to section
        driver.find_element_by_xpath('//*[@id="1"]/td[3]/a').click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "section_box"))
        )

    def test_learn_2_quiz(self):
        login(self)
        driver = self.driver
        # to learn
        driver.find_element_by_xpath('//*[@id="1"]/td[3]/a[1]').click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "quiz-btn"))
        )
        # to quiz
        driver.find_element_by_class_name('quiz-btn').click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "quiz"))
        )

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()