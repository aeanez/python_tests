from selenium import webdriver
import os

actual_dir = os.getcwd()

browser = webdriver.PhantomJS(f'{actual_dir}/vendors/phantomjs.exe')

browser.get("https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe")
 
iframe = browser.find_element_by_tag_name("iframe")
 
browser.switch_to.default_content()
 
browser.switch_to.frame(iframe)
 
iframe_source = browser.page_source

print(iframe_source) #returns iframe source
print(browser.current_url) #returns iframe URL