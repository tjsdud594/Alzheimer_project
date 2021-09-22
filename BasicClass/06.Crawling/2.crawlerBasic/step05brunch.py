import re

# 웹크롤링 지원 API
from urllib.request import urlopen
from html import unescape

import cx_Oracle
import os



# 크롤링 막혀있음.......
def main():
    """
    호출 순서
        fetch(), scrape(), save() 순으로 호출
    """
    html = fetch('https://brunch.co.kr')
    # print(html)


    books = scraping(html)
    # save(books)


def fetch(url):  
    f = urlopen(url) # url에 해당하는 web page를 통으로 크롤링
    
    # HTTP 헤더를 기반으로 인코딩 형식을 추출
    encoding = f.info().get_content_charset(failobj="utf-8")
    print("--- 1. 인코딩 정보 : ", encoding)    # utf-8

    
    # 추출한 인코딩 형식을 기반으로 문자열을 디코딩, 정보로 디코딩 안 할 경우 한글 깨짐 현상이 발생 가능
    # 왜? 특정사이트는 encoding 정보가 utf-8으로 되어 있기도 함, 해당 사이트가 구현되어있는 정보로 디코딩 수행
    # f 변수가 보유한 페이지의 모든 정보를 utf-8 포멧으로 복원 
    html = f.read().decode(encoding)

    #print("--- 2. 모든 문서 내용 추출 ", html)
    return html


def crawling(url):
    f = urlopen(url) # url에 해당하는 web page를 통으로 크롤링
    
    # HTTP 헤더를 기반으로 인코딩 형식을 추출
    encoding = f.info().get_content_charset(failobj="utf-8")
    print("--- 1. 인코딩 정보 : ", encoding)    # utf-8

    
    # 추출한 인코딩 형식을 기반으로 문자열을 디코딩, 정보로 디코딩 안 할 경우 한글 깨짐 현상이 발생 가능
    # 왜? 특정사이트는 encoding 정보가 utf-8으로 되어 있기도 함, 해당 사이트가 구현되어있는 정보로 디코딩 수행
    # f 변수가 보유한 페이지의 모든 정보를 utf-8 포멧으로 복원 
    html = f.read().decode(encoding)

    #print("--- 2. 모든 문서 내용 추출 ", html)
    return html



def scraping(html):
    """
    매개변수 html로 받은 HTML 문서의 내용을 정규 표현식을 사용해서 도서 정보를 추출
    반환값: 도서(dict) 리스트
    """
    books = []

    # title과 link url 착출
    # 반복문의 in 연산자에 html에서 특정 영역을 도출
    '''
    <a class="keyword_item brunch_keyword_item" href="/keyword/지구한바퀴_세계여행?q=g" target="_blank" style="left: 0px; top: 0px;">
    for data in re.findall (r'<td class="left"><a href="(.*?)">(.*?)</a></td>', html):
    '''
    # for data in re.findall(r'<td class="left"><a href="(.*?)">(.*?)</a></td>', html):
    for data in re.findall(r'<a class="keyword_item brunch_keyword_item" href=".*?" target="_blank" style="left: 0px; top: 0px;">', html):
        print(data)
        # link = re.search(r'<a href="(.*?)">', data)
        # # print(link.group(1))
        # url = 'https://www.hanbit.co.kr' + link.group(1)
        # title = re.sub(r'<.*?>', '', data)
        # print(title)

        # books.append({'url':url, 'title':title})
        # print(books)
    
        # return books



# def save(books):
#     # 접속
#     con = cx_Oracle.connect("SCOTT/TIGER@localhost:1521/xe")
#     # 커서를 추출
#     cur = con.cursor()
#     # cur.execute('''DROP TABLE books''')   # 에러 발생시 다음 로직 실행 불가
#     # books 테이블을 생성 - 
#     cur.execute('''
#         CREATE TABLE books (
#             title varchar2(200),
#             url varchar2(200)
#         )
#     ''')
#     # executemany() 메서드를 사용하면 매개변수로 리스트를 지정할 수 있음
#     cur.executemany('INSERT INTO books VALUES (:title, :url)', books)
#     con.commit()
#     cur.close()
#     con.close()

if __name__=='__main__':
    main()
