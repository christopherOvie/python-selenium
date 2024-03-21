import time

from selenium import webdriver
import timeit
driver=webdriver.Chrome(executable_path="C:\\MyDriver\\chromedriver-win64\\chromedriver.exe")
time.sleep(2)
driver.get('https://demoqa.com/text-box')
time.sleep(2)
driver.maximize_window()
#time.sleep(5)
#driver.close()
#write code to start selenium and close
fullname=driver.find_element_by_id('userName')
fullname.send_keys('chris')

email=driver.find_element_by_id('userEmail')
email.send_keys('chris@gmail.com')

currentAddress =driver.find_element_by_id('currentAddress')
currentAddress.send_keys('3  test street')

permanentAddress =driver.find_element_by_id('permanentAddress')
permanentAddress.send_keys('3 test street usa')

submit =driver.find_element_by_id('submit')
submit.click()


#//button[text()='Submit']    #//input[contains(@id,'userN')]
#//label[@id='userName-label']/following::input[1]
#//label[@id='userEmail-label']/preceeding::input[2]
#//label[@id='userEmail-label']/preceeding::input[2]
#//input[@id='yesRadio']/following-sibling::label
#//label[@for='yesRadio']/preceding-sibling::input   radio button
