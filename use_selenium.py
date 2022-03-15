from xml.dom.minidom import Element
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By ## 4버전
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("./chromedriver")
BASE_URL = 'https://comtrade.un.org/Data/'
driver.get(BASE_URL)
driver.implicitly_wait(3)

## 검색값 고르기
# 연도
year = driver.find_element(By.ID,'s2id_periods')
# year_select = driver.find_element(By.ID,'periods')
# select = Select(year_select)
# select.select_by_visible_text('2015')
'''
soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup.text,'파싱하기')
'''
## find_element_~가 구형문법
# find_element(value,속성)식으로 바꿔야 됌
# 참고 https://goodthings4me.tistory.com/567

#xpath로 접근해보기
# https://wkdtjsgur100.github.io/selenium-xpath/
year_path = driver.find_element(By.XPATH, "//div[@id='s2id_periods']/ul[@class='select2-choices']/li[@class='select2-search-choice']")
# year_path.send_keys('2016')
print(year_path.text)
driver.find_element(By.XPATH, '//*[@id="s2id_periods"]/ul').click()
time.sleep(1)
# 옵션을 찾아서 직접 선택하는법
# driver.find_element(By.XPATH, '//*[@id="select2-drop"]/ul/li[6]/div').click() # 2020
# time.sleep(1)

## input 가져오기
input1 = driver.find_element(By.XPATH, '//*[@id="periods"]').get_attribute('value')
input1 = '2010,2011'
# content = Element.getAttribute('innerHTML')
driver.execute_script("document.getElementById('periods').value='2010'", input1)

#정중앙클릭이되어버린다
# driver.find_element(By.XPATH, '//*[@id="s2id_periods"]/ul').click()
# driver.find_element(By.XPATH, '//*[@id="s2id_periods"]/ul').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//*[@id="select2-drop"]/ul/li[10]/div').click() # 2020
# time.sleep(1)
#


print(year.text,'연도')

# year_textbox = driver.find_element(By.CLASS_NAME,'select2-sizer')
# year_textbox.send_keys('2016')
# time.sleep(1)
# year_textbox.send_keys(Keys.ENTER)
# time.sleep(1)
# print(year.text,'연도')


# year_select.clear()
# time.sleep(3)
# year_input = driver.find_element(By.ID, 'periods')
# year_list = ['2005','2006','2007','2008','2009']
# year_input.send_keys('2010')
# print(year_input)
# time.sleep(3)
# year_select.send_keys('value','2015')
# year_select.send_keys(Keys.RETURN)
time.sleep(3)
# print(year_select)
# for i in year_list:
#     year_input.v
#     year_input.send_keys(i)
#     time.sleep(1)


##input = periods

# Reporters 
# s2id_reporters
## input = reporters

# Partners
# s2id_partners
## input = partners

# Trade Flows
# s2id_tradeFlow
##input = s2id_autogen4

# HS Commodity codes
# s2id_itemCodes
##input = itemCodes