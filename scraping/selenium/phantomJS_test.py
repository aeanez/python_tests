from selenium import webdriver
import os

actual_dir = os.getcwd()

browser = webdriver.PhantomJS(f'{actual_dir}/vendors/phantomjs.exe')
browser.get("https://www.python.org/")
 
print(browser.find_element_by_class_name("introduction").text) 
browser.close()

#Recuperar varias etiquetas del mismo tipo

# from selenium import webdriver
# from bs4 import BeautifulSoup
# import os
 
# actual_dir = os.getcwd()

# browser = webdriver.PhantomJS(f'{actual_dir}/vendors/phantomjs.exe')

# browser.get("https://www.python.org/")
 
# page = BeautifulSoup(browser.page_source,"html5lib")
 
# links = page.findAll("a")
 
# for link in links:
 
#     print(link)
 
# browser.close()