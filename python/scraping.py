# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 09:34:17 2020

@author: Home
"""


from selenium import webdriver

from selenium.webdriver.common.keys import Keys

# dir = os.path.dirname(__file__)
# chrome_driver_path = dir + "\chromedriver.exe"

browser = webdriver.Chrome()

browser.get('http://www.yahoo.com')

assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)