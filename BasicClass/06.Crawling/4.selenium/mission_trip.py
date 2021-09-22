from selenium import webdriver
import time # 실행을 잠시 중지(sleep(초단위))
from bs4 import BeautifulSoup
import requests

driver = webdriver.Chrome("c:/driver/chromedriver")

driver.get("http://tour.interpark.com/")
# 화면이동까지 하면서 동적으로 데이터를 크롤링시에는 가급적 화면에 출력하는(렌더링) 시점등을 고려해서 실행로직도 잠시 중지
# 크롬브라우저 드라아버도 잠시 쉬게 해주는 설정
# 화면에 렌더링(화면출력, 브라우징)되는 시간에 대한 배려

time.sleep(3)
driver.implicitly_wait(3) # seconds

# input tag를 포함하고 있는 form tag가 있으나 action 속성 없음 즉 submit()의미 없음
# submit() : form action 속성에 설정된 서버 프로그램으로 전송
# trip.submit
trip = driver.find_element_by_name("SearchGNBText")

# 검색버튼 찾기<button class="search-btn" type="button" onclick="searchBarModule.ClickForSearch();">검색</button>
btn = driver.find_element_by_class_name("search-btn")

trip.send_keys("부산") 

btn.click()

driver.implicitly_wait(3) # seconds


trip_course = driver.find_element_by_id("li_T")
trip_course.click()

# driver.


print(driver.current_url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(soup)

for page in range(1, 6):
    print("============================== ", page)

    # 자바스크립트 실행
    driver.execute_script(
        "searchModule.SetCategoryList({}, '')".format(page))
    driver.implicitly_wait(15)
    print("{} 페이지로 이동!!!".format(page))

    '''
    <ul>
        <li class="active" role="button" tabindex="1">1</li>
        <li role="button" tabindex="2" onclick="searchModule.SetCategoryList(2, '')">2</li>
        <li role="button" tabindex="3" onclick="searchModule.SetCategoryList(3, '')">3</li>
        <li role="button" tabindex="4" onclick="searchModule.SetCategoryList(4, '')">4</li>
        <li role="button" tabindex="5" onclick="searchModule.SetCategoryList(5, '')">5</li>
    </ul>
    '''


    soup = BeautifulSoup(driver.page_source, "lxml")

    
    for trip_info in soup.select('li.boxItem'):
        print(trip_info.find('img')['src'])
        print(trip_info.find('h5').string)
        print(trip_info.find('h5')['onclick'])
        print(trip_info.select('.proInfo')[1].string)
        print(trip_info.select('.proInfo')[0].string)
        print(trip_info.select('.proInfo')[2].string)
        print('='*10)

time.sleep(10)
driver.quit()

