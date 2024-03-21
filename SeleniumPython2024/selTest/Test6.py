import time

from selenium import webdriver
import timeit
driver=webdriver.Chrome(executable_path="C:\\MyDriver\\chromedriver-win64\\chromedriver.exe")
time.sleep(2)
driver.get('https://demoqa.com/alerts')
time.sleep(2)
driver.maximize_window()

prompytButton= driver.find_element_by_xpath("//button[@id='promtButton']")
prompytButton.click()
#time.sleep(5)
#driver.close()
#write code to start selenium and close
# fullname=driver.find_element_by_id('userName')
# fullname.send_keys('chris')



#//button[text()='Submit']    #//input[contains(@id,'userN')]
#//label[@id='userName-label']/following::input[1]
#//label[@id='userEmail-label']/preceeding::input[2]
#//label[@id='userEmail-label']/preceeding::input[2]
#//input[@id='yesRadio']/following-sibling::label
#//label[@for='yesRadio']/preceding-sibling::input   radio button
