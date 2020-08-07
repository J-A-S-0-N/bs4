from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import os

url = "http://kanview.ks.gov/PayRates/PayRates_Agency.aspx"
driver = webdriver.Chrome("C:\\Users\\jason\\Desktop\\_\\all programs\\programs\\chromedriver")
driver.implicitly_wait(30)
driver.get(url)


driver.get(url)

python_button = driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_33') #FHSU
python_button.click()


driver.quit()
