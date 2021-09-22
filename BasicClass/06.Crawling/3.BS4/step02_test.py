html='''<!DOCTYPE html>
<html lang="ko">
<body>
  <div id="main-goods" role="page">
      <h1>과일과 야채</h1>
      <ul id="fr-list">
        <li class="red green" data-lo="ko">사과</li>
        <li class="purple" data-lo="us">포도</li>
        <li class="yellow" data-lo="us">레몬</li>
        <li class="yellow" data-lo="ko">오렌지</li>
      </ul>

      <ul id="ve-list">
        <li class="white green" data-lo="ko">무</li>
        <li class="red green" data-lo="us">파프리카</li>
        <li class="black" data-lo="ko">가지</li>
        <li class="black" data-lo="us">아보카도</li>
        <li class="white" data-lo="cn">연근</li>
      </ul>
  </div>
<body>
</html>'''

''' 결과창
레몬
아보카도
파프리카
아보카도
아보카도
아보카도
'''


from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')

# print(soup)

print(soup.html.select('#fr-list > .yellow'))   # [<li class="yellow" data-lo="us">레몬</li>, <li class="yellow" data-lo="ko">오렌지</li>]
print(soup.html.select('#fr-list > .yellow')[0].string) # 레몬

print(soup.html.select('#ve-list > .black'))   # [<li class="black" data-lo="ko">가지</li>, <li class="black" data-lo="us">아보카도</li>]
print(soup.html.select('#ve-list > .black')[1].string)   # 아보카도


print('=============================================')
print(soup.html.select('li'))

mission = []

for data in soup.html.select('li'):
    # if data.string == '아보카도' or data.string == '레몬' or data.string == '파프리카':
        print(data.string)
        mission.append(data.string)


print(mission)

print(mission[2])
print(mission[7])
print(mission[5])
print(mission[7])
print(mission[7])
print(mission[7])


''' 강사님 답안지
soup = BeautifulSoup(html, "html.parser")

# step01 : css 선택자로 데이터 추출하기 
# string 
# CSS Selector
# https://www.w3schools.com/cssref/css_selectors.asp

nth-of-type() : parameter값에 해당하는 순번의 자식

# soup.select_one("li:nth-of-type(3)").string
# 해당 tag의 하위 자식 text를 의미하되, text인 경우에만 데이터 착출
print(soup.select_one("li:nth-of-type(3)").string)              # 레몬

# #ve-list >  li:nth-of-type(4)
#ve-list  : id가 ve-list
# > : 하위 자식
# li:nth-of-type(4) : li tag의 4번째

print(soup.select_one("#ve-list > li:nth-of-type(4)").string)   # 아보카도


[data-lo='us'] : data-lo='us'라는 속성을 의미
#ve-list > li[data-lo='us'] : id가 ve-list하위의 모든 li tag 중에서 속성명이 data-lo, 단 data-lo의 값이 us인 모든 tag를 list(배열 반환)
# 배열 또는 list로 반환 되었으니 선별해서 지정해서 사용, 여러개가 반환 따라서 고유한 index로 구분해서 사용
print(soup.select("#ve-list > li[data-lo='us']")[0].string)     # 파프리카


# li tag의 class 속성 의미 : . -class 속성 의미
print(soup.select("#ve-list > li.black")[1].string)             # 아보카도


# step02 : find() 함수로 추출하기
# 속성이 하나 이상인 경우 적용하는 기술 : class="black" data_lo="us"
attDatas = {"data-lo":"us", "class":"black"}

# 두가지 속성을 보유하고 있는 li라는 tag : soup.find("li", attDatas)
# soup.find("li", attDatas).string : 하위 text 자식
print(soup.find("li", attDatas).string) # 아보카도


# step03 : find() 함수로 연속적으로 추출하기
# 메소드 또는 함수의 체이닝 기술
print(soup.find(id="ve-list").find("li", attDatas).string)  #아보카도


'''
attDatas = {"data-lo":"us", "class":"black"}
# attDatas = {"class":"black"}
print(soup.find(id="ve-list").find("li", attDatas))

    