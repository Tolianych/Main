from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class NewBackupTask(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://172.20.60.237/"
        self.verificationErrors = []
    
    def test_new_backup_task(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id=\"viewport-header\"]/div[2]/div/div/div[2]/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/em/button").click()
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "/html/body/div/div/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr[2]/td[2]/div/div/div/div/ul/div/li/ul/li[3]/ul/li[2]/div/a/span"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick]]
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "/html/body/div/div/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr[2]/td[2]/div/div/div/div/ul/div/li/ul/li[3]/ul/li[2]/ul/li/div/a/span"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick]]
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "/html/body/div/div/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr[2]/td[2]/div/div/div/div/ul/div/li/ul/li[3]/ul/li[2]/ul/li/ul/li/div/a/span"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("/html/body/div/div/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr[2]/td[2]/div/div/div/div/ul/div/li/ul/li[3]/ul/li[2]/ul/li/ul/li/div/a/span").click()
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "/html/body/div/div/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr[2]/td[3]/div/div[2]/div/div/div/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/em"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("/html/body/div/div/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr[2]/td[3]/div/div[2]/div/div/div/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/em").click()
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "/html/body/div/div/div/div/div[3]/div/div/div[2]/div/div/div/div/div[3]/div/div/table/tbody/tr[2]/td[2]/em/button"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("/html/body/div/div/div/div/div[3]/div/div/div[2]/div/div/div/div/div[3]/div/div/table/tbody/tr[2]/td[2]/em/button").click()
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "/html/body/div/div/div/div/div[3]/div/div[2]/div[2]/div/div/div/div/div[3]/div/div/table/tbody/tr[2]/td[2]/em/button"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("/html/body/div/div/div/div/div[3]/div/div[2]/div[2]/div/div/div/div/div[3]/div/div/table/tbody/tr[2]/td[2]/em/button").click()
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "/html/body/div/div/div/div/div[3]/div/div[3]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div/form/div/div/div/div/table/tbody/tr[2]/td[2]/em/button"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("/html/body/div/div/div/div/div[3]/div/div[3]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div/form/div/div/div/div/table/tbody/tr[2]/td[2]/em/button").click()
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "//*[@id=\"window-browse-archive-path\"]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//*[@id=\"window-browse-archive-path\"]").clear()
        driver.find_element_by_xpath("//*[@id=\"window-browse-archive-path\"]").send_keys("\\\\172.20.60.202\\free\\SmokeAut")
        driver.find_element_by_xpath("//table[@id='window-browse-go']/tbody/tr[2]/td[2]/em/button").click()
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "//*[@id=\"window-browse-form-auth-name\"]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//*[@id=\"window-browse-form-auth-name\"]").clear()
        driver.find_element_by_xpath("//*[@id=\"window-browse-form-auth-name\"]").send_keys("Administrator")
        driver.find_element_by_xpath("//*[@id=\"window-browse-form-auth-pass\"]").clear()
        driver.find_element_by_xpath("//*[@id=\"window-browse-form-auth-pass\"]").send_keys("qwaszx21")
        driver.find_element_by_xpath("//*[@id=\"window-browse-form-auth\"]/div/div/form/table/tbody/tr[2]/td[2]/em/button").click()
        for i in range(60):
            try:
                if not self.is_element_present(By.XPATH, "//*[@id=\"window-browse-ok-btn\"]/tbody/tr[2]/td[2]/em/button[contains(@disabled,?)]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//*[@id=\"window-browse-ok-btn\"]/tbody/tr[2]/td[2]/em/button").click()
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "//*[@id=\"where-to-backup-btn-next\"]/tbody/tr[2]/td[2]/em/button"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//*[@id=\"where-to-backup-btn-next\"]/tbody/tr[2]/td[2]/em/button").click()
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "//*[@id=\"viewport-content\"]/div/div[4]/div[2]/div/div/div/div/div[3]/div/div/table[2]/tbody/tr[2]/td[2]/em/button"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//*[@id=\"viewport-content\"]/div/div[4]/div[2]/div/div/div/div/div[3]/div/div/table[2]/tbody/tr[2]/td[2]/em/button").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
