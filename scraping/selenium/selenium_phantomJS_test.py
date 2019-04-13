from selenium import webdriver
 
import time
import os

actual_dir = os.getcwd()

browser = webdriver.PhantomJS(f'{actual_dir}/vendors/phantomjs.exe')
 
browser.get("https://www.w3schools.com/xml/ajax_intro.asp")
 
browser.find_element_by_tag_name("button").click()
 
time.sleep(2)     #Explicit wait
 
browser.get_screenshot_as_file("image.png")
 
browser.close()