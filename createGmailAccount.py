from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import date

mydriver = webdriver.Chrome()
mydriver.maximize_window()


mydriver.implicitly_wait(20)
#to go to URL
mydriver.get("https://www.google.com/gmail/about/")

#to click the button
mydriver.get_screenshot_as_file("SS_"+date.currenttime()+".png")

button_clickF = mydriver.find_element(By.XPATH, "/html/body/main/div[1]/div/div/div/div/div[1]/div[3]/div[1]/a/span[2]")
button_clickWF = mydriver.find_element(By.XPATH, "/html/body/header/div/div/div/a[4]/span[1]")

if(button_clickF):
    button_clickF.click()
else:
    button_clickWF.click()

first_name = mydriver.find_element(By.ID, "firstName")
first_name.send_keys("micky")
mydriver.get_screenshot_as_file("SS_"+date.currenttime()+".png")

last_name = mydriver.find_element(By.ID, "lastName")
last_name.send_keys("mouse")

submit = mydriver.find_element(By.XPATH, '//*[@id="collectNameNext"]/div/button/span')
submit.click() 

drp = Select(mydriver.find_element(By.ID, "month"))
drp.select_by_visible_text('August') 

B_day = mydriver.find_element(By.ID, "day")
B_day.send_keys(24)

B_year = mydriver.find_element(By.ID, "year")
B_year.send_keys(1997)


drop=Select(mydriver.find_element(By.ID, "gender"))
drop.select_by_visible_text('Female') 

submit = mydriver.find_element(By.XPATH, '//*[@id="birthdaygenderNext"]/div/button/span')
mydriver.get_screenshot_as_file("SS_"+date.currenttime()+".png")
submit.click() 

try:
    email = mydriver.find_element(By.ID, "selectioni3")
    email.click()
    enter_email = mydriver.find_element(By.NAME, "Username")
    enter_email.send_keys("mickymousetest0304")
except:
    enter_email = mydriver.find_element(By.NAME, "Username")
    enter_email.send_keys("mickymousetest0304")

next = mydriver.find_element(By.XPATH, '//*[@id="next"]/div/button/span')
mydriver.get_screenshot_as_file("SS_"+date.currenttime()+".png")
next.click() 

pwd = mydriver.find_element(By.NAME, "Passwd")
pwd.send_keys("@Minihouse34") 

cnpwd = mydriver.find_element(By.NAME, "PasswdAgain")
cnpwd.send_keys("@Minihouse34")  

chkbx = mydriver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div[3]/div/div[1]/div/div/div[1]/div/input')
chkbx.click()
mydriver.get_screenshot_as_file("SS_"+date.currenttime()+".png")

time.sleep(2) 

chkbx.click() 
mydriver.get_screenshot_as_file("SS_"+date.currenttime()+".png")

pwnext = mydriver.find_element(By.XPATH, '//*[@id="createpasswordNext"]/div/button/span')
pwnext.click()
mydriver.get_screenshot_as_file("SS_"+date.currenttime()+".png")
        


time.sleep(5)