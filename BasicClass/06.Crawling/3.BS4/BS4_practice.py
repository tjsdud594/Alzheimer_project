from bs4 import BeautifulSoup
from urllib.request import urlopen
from html import unescape

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


html = fetch('https://movie.naver.com/movie/running/current.nhn#')
soup = BeautifulSoup(html, 'html.parser')
# soup = BeautifulSoup(html, 'lxml')  # 더효율적임!!
print(soup)
# print(type(soup))

# print(soup.find_all('.tit'))

