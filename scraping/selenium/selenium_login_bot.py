from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os

actual_dir = os.getcwd()
driver = webdriver.Chrome(f'{actual_dir}/vendors/chromedriver.exe')
#driver.set_window_size(400,400)

driver.get(input('Ingrese url: '))
#assert "Python" in driver.title
elem = driver.find_element_by_name("username")
elem.clear()
elem.send_keys(input('Ingrese usuario: '))
elem = driver.find_element_by_name("password")
elem.clear()
elem.send_keys(input('Ingrese Clave: '))
elem.send_keys(Keys.RETURN)
#driver.close()