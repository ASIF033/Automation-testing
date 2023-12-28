# import web-driver
from selenium import webdriver

driver = webdriver.Edge()

driver.get("http://sqa.deepchainlabs.com/login")
while True:
    pass
    title = driver.find_element_by_id("emailField")
    title.send_keys("admindcl@gmail.com")



