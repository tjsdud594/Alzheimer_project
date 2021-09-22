from typing_extensions import runtime
from selenium import webdriver
import time # 실행을 잠시 중지(sleep(초단위))
from bs4 import BeautifulSoup
import json

class Crawling():
    def interparkcrawling(word):
        driver = webdriver.Chrome("c:/driver/chromedriver")

        driver.get("http://tour.interpark.com/")


        # time.sleep(3)
        # driver.implicitly_wait(3) # seconds


        trip = driver.find_element_by_name("SearchGNBText")

        btn = driver.find_element_by_class_name("search-btn")

        trip.send_keys(word) 

        btn.click()

        driver.implicitly_wait(3) # seconds


        trip_course = driver.find_element_by_id("li_T")
        trip_course.click()


        print(driver.current_url)
        driver.implicitly_wait(3) # seconds

        # soup = BeautifulSoup(driver.page_source, 'html.parser')
        # print(soup)

        # for page in range(1, 6):
        #     print("============================== ", page)

        #     driver.execute_script(
        #         "searchModule.SetCategoryList({}, '')".format(page))
        #     # driver.implicitly_wait(15)
        #     print("{} 페이지로 이동!!!".format(page))


        soup = BeautifulSoup(driver.page_source, "lxml")

        Trip_Info = []
        for trip_info in soup.select('li.boxItem'):
            img_url = trip_info.find('img')['src']
            trip_name = trip_info.find('h5').string
            trip_page = trip_info.find('h5')['onclick']
            # trip_departure =trip_info.select('.proInfo')[1].string
            # trip_date = trip_info.select('.proInfo')[0].string
            # trip_score = trip_info.select('.proInfo')[2].string
            # Trip_Info.append({'img_url':img_url, 'trip_name':trip_name, 'trip_page':trip_page, 'trip_departure':trip_departure, 'trip_date':trip_date, 'trip_score':trip_score})
            Trip_Info.append({'img_url':img_url, 'trip_name':trip_name, 'trip_page':trip_page})
        print(Trip_Info)
        print(len(Trip_Info))
                
        driver.implicitly_wait(3)
        # time.sleep(10)
        driver.quit()

        print(json.dumps(Trip_Info, ensure_ascii=False))
        return json.dumps(Trip_Info, ensure_ascii=False)

    # print(interparkcrawling('부산'))

