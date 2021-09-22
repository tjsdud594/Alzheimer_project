# 미션 : 구글에서 검색 가능하게 step01 처럼 작업 권장

from selenium import webdriver
import time # 실행을 잠시 중지(sleep(초단위))

driver = webdriver.Chrome("c:/driver/chromedriver")

driver.get("https://www.google.co.kr")

tag = driver.find_element_by_name("q")

tag.clear()

tag.send_keys("AI") 

tag.submit()

time.sleep(20)

driver.quit()