import time  # to use delay

from selenium import webdriver  # import web-driver
from selenium.webdriver.common.by import By   # Set of supported locator strategies.
from pynput.keyboard import Key, Controller  # for keyboard interaction

driver = webdriver.Edge()

driver.get("http://sqa.deepchainlabs.com/login")  # go to login page
driver.maximize_window()  # use full window
time.sleep(2)  # use delay
emailField = driver.find_element(By.ID, "emailField")  # locate email field using id
emailField.send_keys("admindcl@gmail.com")  # give input in the email field
time.sleep(2)

passwordField = driver.find_element(By.ID, "passwordField")  # locate password field using id
passwordField.send_keys("adminpassword")  # send input
time.sleep(2)

loginBtn = driver.find_element(By.XPATH,
                               "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[2]/div[3]/div[1]")
# locate login button using xpath
loginBtn.click()  # click login button
time.sleep(5)

createBlogBtn = driver.find_element(By.XPATH,
                                    "(//span[contains(@class,'t-bg-[#2B79D3] t-text-[#ffffff] t-px-6 t-py-1 t-rounded-[7px] t-cursor-pointer')])[1]")
# locate create blog button
createBlogBtn.click()

time.sleep(3)

title = driver.find_element(By.XPATH, "(//input[@id='inputField'])[1]")     # locate title field during blog creation
title.send_keys("test1")    # send input
time.sleep(3)        # use delay

tag = driver.find_element(By.XPATH, "(//input[@id='inputField'])[2]")    # locate tag field during blog creation
tag.send_keys("sample")     # send input
time.sleep(3)    # use delay

content = driver.find_element(By.XPATH, "//div[contains(@class,'ql-editor ql-blank')]//p")     # locate content field during blog creation
content.send_keys("test data")   # send input
time.sleep(2)

category = driver.find_element(By.XPATH, "(//input[@id='inputField'])[3]")  # locate category field
category.click()
time.sleep(2)

option = driver.find_element(By.XPATH, "//li[normalize-space()='Frontend']")    # select frontend option
option.click()
time.sleep(2)

read = driver.find_element(By.XPATH, "(//input[@id='inputField'])[4]")    # locate read field
read.send_keys("2")     # send input
time.sleep(2)

upload = driver.find_element(By.XPATH, "//label[@role='presentation']")    # locate file upload field
upload.click()
time.sleep(2)

keyboard = Controller()          # initializing keyboard variable
keyboard.type("C:\\p\\test.jpg")        # type file location path
keyboard.press(Key.enter)           # click enter
keyboard.release(Key.enter)         # release enter
time.sleep(2)

publish = driver.find_element(By.XPATH, "//button[normalize-space()='Publish']")     # locate publish button
publish.click()
time.sleep(10)

cancel = driver.find_element(By.XPATH,
                             "(//span[contains(@class,'t-px-6 t-py-1.5 t-rounded-[7px] t-cursor-pointer t-bg-[#DBECFF] t-text-[#2B79D3] t-font-[400]')])[1]")

cancel.click()
time.sleep(5)

driver.get("http://sqa.deepchainlabs.com/blogs")        # go to public blog page
time.sleep(5)        # delay
driver.get("http://sqa.deepchainlabs.com/admin/blogs")        # go to admin blog page
time.sleep(5)

activityBtn = driver.find_element(By.XPATH, "(//div)[47]")       # locate the activity button
activityBtn.click()
time.sleep(5)

driver.get("http://sqa.deepchainlabs.com/blogs")       # go to public blog again to check if the visibilty is changed or not

time.sleep(4)
