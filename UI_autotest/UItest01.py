import time

from selenium import webdriver


# driver = webdriver.Chrome()
# driver.get("http://op-product-test.tangees.com/doncus/advanced-filter/industry-model")
# time.sleep(5)
# search_tab =driver.find_element_by_xpath('//*[@id=\"icon\"]/div[2]/i/svg')
# search_tab.click()
# #time.sleep(1)
# driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/div[1]/div/div/span/input').send_keys('17806533496')
# driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/div[2]/div/div/span/div/div[1]/input').send_keys('111')
# time.sleep(2)
# for i in range(5):
#      driver.find_element_by_xpath('//*[@id="app-content"]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr[3]/td[11]/div/span[3]').click()
# driver.quit()


# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# time.sleep(2)
# driver.find_element_by_id('kw').send_keys('百度')
# driver.find_element_by_id('su').click()
# time.sleep(3)
# driver.quit()






#python(AppDynamics)
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class AppDynamicsJob(unittest.TestCase):
     def setUp(self):
          # AppDynamics will automatically override this web driver
          # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
          self.driver = webdriver.Firefox()
          self.driver.implicitly_wait(30)
          self.base_url = "https://www.google.com/"
          self.verificationErrors = []
          self.accept_next_alert = True

     def test_app_dynamics_job(self):
          driver = self.driver
          driver.get("https://user-test.tangees.com/users/sign-in")
          driver.get("https://user-test.tangees.com/users/sign-in")
          driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div[2]").click()
          driver.find_element_by_xpath("//input[@value='']").click()
          driver.find_element_by_xpath("//input[@value='17806533496']").clear()
          driver.find_element_by_xpath("//input[@value='17806533496']").send_keys("17806533496")
          driver.find_element_by_xpath("//input[@type='password']").click()
          driver.find_element_by_xpath("//input[@value='Jiahu.456']").clear()
          driver.find_element_by_xpath("//input[@value='Jiahu.456']").send_keys("Jiahu.456")
          driver.find_element_by_xpath("//button[@type='button']").click()
          driver.find_element_by_xpath("//main[@id='app-content']/div/div[2]/div/div/div/div/div[2]/a/span").click()

     def is_element_present(self, how, what):
          try:
               self.driver.find_element(by=how, value=what)
          except NoSuchElementException as e:
               return False
          return True

     def is_alert_present(self):
          try:
               self.driver.switch_to_alert()
          except NoAlertPresentException as e:
               return False
          return True

     def close_alert_and_get_its_text(self):
          try:
               alert = self.driver.switch_to_alert()
               alert_text = alert.text
               if self.accept_next_alert:
                    alert.accept()
               else:
                    alert.dismiss()
               return alert_text
          finally:
               self.accept_next_alert = True

     def tearDown(self):
          # To know more about the difference between verify and assert,
          # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
          self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
     unittest.main()

#python2(WebDriver + unittest)
# -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
# import unittest, time, re
#
#
# class UntitledTestCase(unittest.TestCase):
#      def setUp(self):
#           self.driver = webdriver.Firefox()
#           self.driver.implicitly_wait(30)
#           self.base_url = "https://www.google.com/"
#           self.verificationErrors = []
#           self.accept_next_alert = True
#
#      def test_untitled_test_case(self):
#           driver = self.driver
#           driver.get("https://user-test.tangees.com/users/sign-in")
#           driver.get("https://user-test.tangees.com/users/sign-in")
#           driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div[2]").click()
#           driver.find_element_by_xpath("//input[@value='']").click()
#           driver.find_element_by_xpath("//input[@value='17806533496']").clear()
#           driver.find_element_by_xpath("//input[@value='17806533496']").send_keys("17806533496")
#           driver.find_element_by_xpath("//input[@type='password']").click()
#           driver.find_element_by_xpath("//input[@value='Jiahu.456']").clear()
#           driver.find_element_by_xpath("//input[@value='Jiahu.456']").send_keys("Jiahu.456")
#           driver.find_element_by_xpath("//button[@type='button']").click()
#           driver.find_element_by_xpath("//main[@id='app-content']/div/div[2]/div/div/div/div/div[2]/a/span").click()
#
#      def is_element_present(self, how, what):
#           try:
#                self.driver.find_element(by=how, value=what)
#           except NoSuchElementException as e:
#                return False
#           return True
#
#      def is_alert_present(self):
#           try:
#                self.driver.switch_to_alert()
#           except NoAlertPresentException as e:
#                return False
#           return True
#
#      def close_alert_and_get_its_text(self):
#           try:
#                alert = self.driver.switch_to_alert()
#                alert_text = alert.text
#                if self.accept_next_alert:
#                     alert.accept()
#                else:
#                     alert.dismiss()
#                return alert_text
#           finally:
#                self.accept_next_alert = True
#
#      def tearDown(self):
#           self.driver.quit()
#           self.assertEqual([], self.verificationErrors)
#
#
# if __name__ == "__main__":
#      unittest.main()

