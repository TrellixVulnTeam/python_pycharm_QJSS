import time

from selenium import webdriver

'''
driver = webdriver.Chrome()
driver.get("http://op-product-test.tangees.com/doncus/advanced-filter/industry-model")
time.sleep(5)
search_tab =driver.find_element_by_xpath('//*[@id="icon"]/div[2]/i/svg')
search_tab.click()
#time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/div[1]/div/div/span/input').send_keys('17806533496')
driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/div[2]/div/div/span/div/div[1]/input').send_keys('111')
time.sleep(2)
for i in range(5):
     driver.find_element_by_xpath('//*[@id="app-content"]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr[3]/td[11]/div/span[3]').click()
driver.quit()

'''
driver = webdriver.Chrome()
driver.get('http://www.baicu.com')
time.sleep(2)
driver.find_element_by_id('kw').send_keys('百度')
driver.find_element_by_id('su').click()
driver.quit()