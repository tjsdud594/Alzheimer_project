# 미션 : 구글에서 검색 가능하게 step01 처럼 작업 권장

from selenium import webdriver
import time # 실행을 잠시 중지(sleep(초단위))

driver = webdriver.Chrome("c:/driver/chromedriver")

driver.get("http://127.0.0.1:5500/4.selenium/step03mypage.html")


# input tag
search_box = driver.find_element_by_name("data")

# button tag

# 검색버튼 찾기
btn = driver.find_element_by_id("btn")  # id속성으로 찾는 함수

search_box.send_keys("encore") 
# search_box.send_keys("hihihi") 


# 검색버튼 클릭시에 실행되는 js 함수 호출 코드
btn.click()

time.sleep(10)

driver.quit()