# html의 필수 표현법
'''
1. html 문서의 tree 구조로 특정 tag 및 text data를 찾아가는 형식은 DOM 기반
2. DOM
    -Document Object Model
    - html 모든요소(tag, 속성, text, ..)를 객체로 관리
    - 실시간 가변적인 동적 화면 구성에 필수 핵심 기술
    - 화면을 변경시키는 기술셋
    - 스펙 : w3c에서 제시, 이 dom 기술을 지원하는 개발 언어들은 모든 언어가 다 지원
    - 수업시간엔 js 기반의 dom 처리 학습중
    - id로 특정 tag 검색 : document.getElementById('고유한 id')
    - next_sibling : 현 위치상에서 다음 동생 검색
    - 해킹 필수 기술

    . : class 속성
    # : id 속성
    이름 : tag 명

'''


html='''
<html>
    <body>
        <h1>스크래핑이란?</h1>
        <h1>스크래핑이란????????????</h1>
        <p id="one">웹페이지 1</p>
        <p id="two">웹페이지 2</p>
        <span class="redColor">
            <p>웹페이지3</p>
        </span>
        <ul>
            <li><a href="www.daum.net">다음</a></li>
            <li><a href="www.naver.com">네이버</a></li>
        </ul>        
    </body>
</html>
'''

# bs4 - html 문서를 tag 속성, css 등으로 섬세하게 관리 가능한 API
from bs4 import BeautifulSoup

# 크롤링 대상의 데이터와 구문해석, 문법체크, 변환가능한 parser 설정
soup = BeautifulSoup(html, 'html.parser')
print(soup)
print('----- 1 ------')

print(soup.html.h1)   # <h1>스크래핑이란?</h1>
print(type(soup.html.p))   # <class 'bs4.element.Tag'>

# html(XML) 문서는 족보구조 즉 tree 구조
# html 상에서 new line(br tag)은 text 자식으로 간주
# next_sibling :  현 위치상에서 다음 내 형제
'''
    <p id="one">웹페이지 1</p>
    <p id="two">웹페이지 2</p>
'''
print(soup.html.p)   # <p id="one">웹페이지 1</p>
print(soup.html.p.next_sibling)   # new line 즉 text 동생
print(soup.html.p.next_sibling.next_sibling)   # <p id="two">웹페이지 2</p>

print(soup.html.span.p)   # <p>웹페이지3</p>

# text 데이터들은 string 속성명과 get_text() 함수로 착출
# html 문서의 span tag 하위의 p tag 하위의 text 데이터
print(soup.html.span.p.string)   # 웹페이지3
print(soup.html.span.p.get_text())   # 웹페이지3


print([text for text in soup.stripped_strings])   # ['스크래핑이란?', '스크래핑이란????????????', '웹페이지 1', '웹페이지 2', '웹페이지3', '다음', '네이버']


print('------ 2 : find()함수------')
print(soup.find(id='one'))   # <p id="one">웹페이지 1</p>
print(soup.find(id='one').string)   # 웹페이지 1
print(soup.select('.redColor'))   
'''
[<span class="redColor">
<p>웹페이지3</p>
</span>]

'''


'''
html css 속성은 중복 표현 : 이름을 동일하게 적용해서 공통 ui
.redColor : class 속성이 redColor인 것들을 찾음
    하나이상일 가능성이 있음 따라서 list 반환

.redColor p
    여백을 기준으로 p는 class 속성값이 redColor인 tag의 자식인 p tag
    하위 tag가 하나만? 보장불가 즉 여러개 존재가능
    따라서 list 타입으로 반환

 ('.redColor p')[0]
    첫번째 해당하는 p tag 반환

('.redColor p')[0].srting
    하위 text 데이터

'''

# print(soup.select('.redColor p'))에 string / get_text()는 바로 사용 불가능
print(soup.select('.redColor p'))    # [<p>웹페이지3</p>]
print(soup.select('.redColor p')[0])    # <p>웹페이지3</p>
print(soup.select('.redColor p')[0].string)    # 웹페이지3

print(soup.find_all('h1'))   # [<h1>스크래핑이란?</h1>, <h1>스크래핑이란????????????</h1>]