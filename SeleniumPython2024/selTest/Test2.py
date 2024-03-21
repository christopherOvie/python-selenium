import time

from selenium import webdriver
import timeit
driver=webdriver.Chrome(executable_path="C:\\MyDriver\\chromedriver-win64\\chromedriver.exe")
time.sleep(2)
driver.get('https://demoqa.com/text-box')
time.sleep(2)
driver.maximize_window()
time.sleep(5)

fullname= driver.find_element_by_xpath("//input[@id='userName']")
fullname.send_keys('test')
# time.sleep(2)
email= driver.find_element_by_xpath("//input[@id='userEmail']")
email.send_keys('test@test.com')
# time.sleep(2)
# driver.close()
textarea= driver.find_element_by_xpath("//textarea[@id='permanentAddress'and @class='form-control']")
textarea.send_keys('testing and')


submit= driver.find_element_by_xpath("//button[text()='Submit']")
submit.click()

#//textarea[@id='permanentAddress'and @class='form-control']
# driver=webdriver.Chrome(executable_path="C:\\MyDriver\\chromedriver-win64\\chromedriver.exe")
# time.sleep(2)
# driver.get('https://demoqa.com/text-box')
# driver.find_element_by_id('userName').send_keys('mike')
# driver.find_element_by_id('userEmail').send_keys('tester')
# #write code to start selenium and close #selenium architecture
# #driver.find_element_by_id('W0wltc').click()