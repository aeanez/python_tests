from selenium import webdriver
import os

actual_dir = os.getcwd()

browser = webdriver.Chrome(f'{actual_dir}/vendors/chromedriver.exe')
 
browser.get("https://www.python.org/")
 
nav = browser.find_element_by_id("mainnav")
 
print(nav.text)