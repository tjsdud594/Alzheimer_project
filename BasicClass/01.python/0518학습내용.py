%s : python 변수로 해당 위치의 값들을 대체하는 기술
# 예제1
    data = '값'
    print('value %s playdata' % data)
# 예제2
    d1 = '값1'
    d2 = '값2'
    print('value %s playdata %s' % (d2, d1))

.find() : 문자열에 포함된 철자의 첫번째 index값 반환
# 예제1
    data = 'abcd Defg'
    print(data.find('a'))

.strip() : 문자열의 앞뒤 잉여 여백 제거 / 데이터 전처리에 필수
.strip('표기') : 표기가 구분자
.strip('표기1 표기2') : 두가지 모두 구분자
# 예제1
    data = ' 봄 여름 가을 겨울 '
    print(data)
    print(len(data))
    print(data.strip())
    print(len(data.strip()))
    print(data.lstrip())
    print(len(data.lstrip()))   
    print(data.rstrip())
    print(len(data.rstrip()))
    
''.join() : list 내의 모든 문자열을 뽑아서 하나의 문자열로 가공
# 예제1
    s1 = ['사과', '귤', '오렌지']
    print(s1, type(s1))

    s2 = ', '.join(s1)  
    print(s2, type(s2))

'문자열'.split(t, n) : 문자열에서 t를 기준으로 구분자로 사용, 정수 n만큼 분리한 문자열 리스트 반환
# 예제1
    s3 = '사과*귤*포도*오렌지'
    print(s3)
    print(s3.split('*'))
    print(s3.split('*', 1))
    print(s3.split('*', 3))

.strip('B') : 문자열 앞뒤의 B 문자열 제거
# 예제1
    actors = '로미오&줄리엣1010'
    print(actors.strip('10'))
    actors2 = '111로미오11&줄리엣1111'
    print(actors2.strip('11'))
    actors3 = '121로미오&줄리엣12121'
    print(actors3.strip('12'))
    print(actors3.strip('1'))

.format() : 문자열을 추가하거나 형식화 하는데 사용
# 예제1
    '{} {} {}'.format('A', 'B', 'C')

%d / %s / %f : 정수표현 / 문자표현 / 부동소수표현
# 예제1
    intValue = 30   #정수
    floatValue = 20.36589    #실수
    print('%d %s %f' % (intValue, 'playdata', floatValue))
    print('%d %s %f' % (floatValue, 'playdata', intValue))

f'...{변수명}...' : f-strings, %나 .format 방식에 비해 간결하고 직관적이며 속도도 빠름
# 예제1
    v1 = 'abcd'
    v2 = 2
    print(f'data야 {v1}-{v2}')

reversed(변수) : 변수에 존재하는 문자열을 역으로 변환한 객체가 저장된 메모리 주소
                메모리 주소이므로 문자열로 반환하기 위해서는 ''.join()을 사용
  = [::-1]
# 예제1
    v = 'encore playdata'
    print(reversed(v), type(reversed(v)))
    print(list(reversed(v)))
    print(''.join(reversed(v)))
    print('#'.join(reversed(v)))
    print(v[::-1])

list.append(데이터) : list의 가장 마지막에 데이터를 추가 저장하는 함수

## 미션 : 문자열 전체 반전하기
    str1 = '안녕 세상!'
    str2 = revert(str1)

    def revert(string):
        return string[::-1]
        or return ''.join(reversed(string))

    print(str1)
    print(str2)

## 미션 : 문자열 단위로 반전하기

    def reversing_words_slice(word):
        new_word = []
        words = word.split(' ')
        for w in words[::-1]:
            new_word.append(w)
        return ' '.join(new_word)
        
    str1 = '엔코아 플레이데이터 openpose'
    str2 = reversing_words_slice(str1)
    print(str2)

## 미션 : 반복문 없이 리스트와 문자열 메소드만으로 문자열 단위로 반전하기

    def reversing_words(str1):
        #print(str1.split(' '))
        #print(reversed(str1.split(' ')))
        #print(' '.join(reversed(str1.split(' '))))
        return ' '.join(reversed(str1.split(' ')))
    
    def reversing_words2(str1):
        words = str1.split(' ')  # 하나의 문자열을 ' '기준으로 list로 변환
        words.reverse()          # list 내의 데이터순서를 반전시킴
        return ' '.join(words)
    
    str1 = '엔코아 플레이데이터 openpose'
    str2 = reversing_words(str1)
    str3 = reversing_words2(str1)
    print(str2)
    print(str3)        

list 
    list1 = [] = list() : 공백 리스트 생성
    list2 = list('hello') : 문자 h, e, l, l, o 를 요소로 가지는 리스트 생성
    list3 = list(range(1, 6)) : 1, 2, 3, 4, 5 를 요소로 가지는 리스트 생성
    list4 = [1, 2, 3, 'h', 'i'] : 1, 2, 3, h, i 를 요소로 가지는 리스트 생성
    list5 = ['aaa', ['bbb', ['ccc', ['ddd', 'eee', 'fff']]]] : 내장 리스트
    # 예제1 : eee만 출력
        list5 = ['aaa', ['bbb', ['ccc', ['ddd', 'eee', 'fff']]]]
        print(list5[0])
        print(list5[1][1])
        print(list5[1][1][1][1])

list/dict.pop() : list의 가장 마지막 변수를 뽑아내어 삭제함 (<->append와 반대)
                  dict는 특정 key를 넣으면 해당하는 value를 리턴하고 삭제
    # 예제1
        lst = [100, 200]
        lst.append(300)
        print(lst)    #[100, 200, 300]

        lst.pop()
        print(lst)    #[100, 200]

        lst.pop(0)
        print(lst)    #[200]

list.sort() : 정렬후 변수 자체에 적용, 대소문자 혼용일경우 우선순위는 대문자(아스키코드 값)
         역정렬 가능, 오름차순 정렬이 기본, 데이터 자체를 수정, 중복허락
         새로운 변수에 대입시에 none값만 대입되고 원본은 오픈X
list.sort(reverse=True) : 내림차순 정렬
sorted(list) : 원본수정 없이 복제본을 생성하여 정렬
    # 예제1 : sort()가 원본을 바꾸는지 확인
        lst = ['a', 'b', 'e', 'c']
        lst.sort()
        print(lst)
    # 예제2 : sort()를 변수에 대입시 출력값
        lst = ['a', 'b', 'e', 'c']
        v = lst.sort()
        print(v)
    # 예제3 : sort()로 내림차순 정렬
        lst = ['a', 'b', 'e', 'c']
        print(lst.sort(reverse=True))
        print(lst)
    # 예제4 : sorted()를 사용해 정렬, 원본확인
        lst = ['a', 'b', 'e', 'c']
        print(sorted(lst))
        print(lst)
        v = sorted(lst)
        print(v)
        v2 = sorted(lst, reverse=True)
        print(v2)
    # 예제5 : dict 정렬
        mydict = {'one':1, 'two':2, 'three':3}
        sorted(mydict)
        sorted(mydict, reverse=True)

tuple : 쉼표로 구분된 변경 불가능한 리스트, 연산 사용가능
    tuple1 = ()
    tuple2 = tuple()
    t1 = (1, 2, 3, 4, 5)
    t2 = ('red', 'blue', 'green')
    t = t1 + t2
    t3 = 'test', 'test1', 'test2' : 괄호없이 나열된 객체들도 튜플로 간주
        # 예제1
            t1 = (1, 2, 3, 4, 5)
            t2 = ('red', 'blue', 'green')
            t = t1 + t2
            print(t)

dict : {key:value, key2:value, ...}, json 포멧과 흡사, 변수명=['key'], 순서X
       key는 절대 중복X
    1. 이미 존재하는 dict에 추가 저장 : dict변수['newKey'] = 새로운데이터
    2. 이미 존재하는 데이터 반환 : get(), ['key']

zip() : list들을 key와 value 형식으로 구성해주는 함수
    # 예제1 : zip() 활용
        name = ['a', 'b', 'c']
        age = [1, 2, 3]

        v = dict(zip(name, age))
        print(v)

dict.items() : dict의 데이터(key와 value)들을 리턴, list()로 타입변환 가능
    #예제1 : item() 활용
        def fun3(**kwargs):

            print(kwargs.items())   #dict_items([('x', 10), ('y', 20), ('z', 30)])
            print(list(kwargs.items()))   #[('x', 10), ('y', 20), ('z', 30)]

        fun3(x=10, y=20, z=30)

dict.get(key, 디폴트값) : 키의 값을 리턴, 키의 값이 없다면 디폴트값을 리턴
                    디폴트값이 없다면 무시

dict.clear() : 모든 데이터를 삭제

dict.update() : 기존 데이터에 전달받은 데이터를 더하여 사전을 갱신

dict.keys() : key 들을 리턴

dict.values() : value 들을 리턴
            

패킹 : 하나의 변수에 다수의 데이터를 넣는 구조 의미
    # 예제1
        v = 1, 2, 's'
        print(type(v))
        print(v)

언패킹 : 하나의 변수에서 여러개의 데이터를 각각 꺼내오는 구조의미
    # 예제1
        v = 1, 2, 's'
        a, b, c = v
        print(a, b, c)   # ,로 출력데이터 구분시 자동으로 여백처리

**기호가 의미하는 횟수**
    1. 아무것도 없음 : 무조건 한번
    2. + : 1~무한대 의미
    3. * : 0~무한대 의미
    4. ? : 0 또는 1

인수(argument) : 호출 프로그램에 의하여 함수에 전달되는 값
매개변수(parameter) : 인수값을 전달받는 변수
    # 예제1
        def f1():
            return 1, 2

        print(f1(), type(f1()))

        v = f1()
        print(v, type(v))
    # 예제2 : 언패킹 활용
        def f2():
            return 1, 'a'

        print(f2())
        
        v1, v2 = f2()
        print(v1, v2)

jupyter notebook에서 cell 구분 단축키 : ctrl shift -

디폴트(default)인수 : 매개변수 기본 초기화값 활용하는 함수
    # 예제1
        def fun1(name, age=10):
            print(name, age)

        fun1('유재석')
        fun1('지석진', 50)

키워드 인수(**kwargs) : keyword argument 줄임말, 키워드 = 특정값 형태로 호출
    # 예제1 : 함수 변수지정
        def fun2(x, y, z):
            return x + y + z

        print(fun2(10, 20, 30))
        print(fun2(x=10, y=20, z=30))
        print(fun2(xx=10, y=20, z=30))
    # 예제2 : **kwargs 사용
        def fun3(**kwargs):
            print(kwargs)
            print(type(kwargs))
            print(kwargs['x'])
            print(kwargs.items())
            print(list(kwargs.items()))

        fun3(x=10, y=20, z=30)
    # 예제 3 
        def fun4(**kwargs):
            for v in [('x', 10), ('y', 20), ('z', 30)]:
                print(v)

        fun4()

        def fun4(**kwargs):
            for k, v in [('x', 10), ('y', 20), ('z', 30)]:
                print(k, v)
                print(k, ':', v)

        fun4()

임의의 인수 : *를 사용할 경우 인수는 tuple형식, 가변인자 활용
    # 예제1
        def fun3(*args, sep='-'):
            print(sep.join(args))

        fun3('a', 'b')
        fun3('a', 'b', 'c', 'd')

import : 제공받은 library에서 함수를 사용하기 위해 사용
    # 예제 : random 사용
        import random
        
        print(random.randrange(36))

random.random() : 0.0 이상 1.0 미만

random.randrange() : 1 에서 6 까지의 정수 중 하나를 무작위로 반환

## 미션 : 일회용 패스워드 생성기를 이용하여서 3개의 패스워드를 생성하여 출력하는 프로그램을 작성해 보기
    import random

    def Rpass():
        alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
        password = ''

        for i in range(6):
            index = random.randrange(36)
            password = password + alphabet[index]

        return password

    print(Rpass())
    print(Rpass())
    print(Rpass())

람다 함수
    1. 이름없이 정의된 익명함수
    2. 매개변수 제한이 없음, 단 하나의 값만 반환
    3. 함수의 반환, 변수의 데이터 값으로도 사용이 가능
    4. list의 sort의 key 속성의 값으로도 사용가능(실전 응용)
    5. 문법 : lambda 인자: 표현식(수식)
    6. lambda : 식을 함수처럼 기능구현 하겠다는 표기의 선언, 이름없는 함수 또는 식이라 표현
        # 예제1
            x = lambda a: a + 10

            print(x(5))
            print(x(20))
        # 예제2 : 함수를 람다표현으로 바꾸기
            def sum(x):
                return x + 10

            print(sum(5))

            sum2 = lambda a : a + 10

            print(sum2(5))
        # 예제3 : sorted()사용하여 list 내에 존재하는 각각의 tuple들의 index를 기준으로 정렬하기
            mylist2 = [('kim', 23, 100), ('lee', 27, 99), ('park', 43, 102)]

            sorted(mylist2, key = lambda a: a[2])  
            print(mylist2)
        # 예제4 : .sort()사용하여 list 내에 존재하는 각각의 tuple들의 index를 기준으로 정렬하기
            mylist2 = [('kim', 23, 100), ('lee', 27, 99), ('park', 43, 102)]

            mylist2.sort(key = lambda a: a[1], reverse=True) 
            print(mylist2)

.lower() : 소문자로 변경하는 함수
.upper() : 대문자로 변경하는 함수
    # 예제1 : 소문자로 변경후 정렬하기
        mylist3 = ['Spam', 'egg', 'Ham']

        for v in mylist3:
            print(v.lower())
        print(mylist3)

        mylist3.sort(key=lambda a : a.lower())
        print(mylist3)

map(함수, list/tuple) : 시퀀스의 모든 항목에 함수를 적용한 결과 리스트 반환
                        list(map()) 형태로 출력해야 데이터값 나옴
    # 예제1 : def를 이용
        def cube(x):
            return x**2

        print(map(cube, range(1, 11)))
        list(map(cube, range(1, 11)))
    # 예제2 : lambda를 이용
        list(map(lambda x : x**2, range(1, 11)))

reduce(함수, 데이터) : 주로 집계용으로 사용
           사용하기 위해서는 functools 모듈에서 뽑아써야함
    # 예제1
        from functools import reduce

        data = reduce(lambda a, b : a + b, [1, 2, 3, 4, 5])
        '''    # 앞의 x에는 앞선 계산결과가 대입되고 y에는 입력한 데이터들이 차례대로 대입됨
        x, y
        1, 2 =>3
        3, 3 => 6
        6, 4 => 10
        10, 5 => 15
        '''
        print(data)
    # 예제2 : reduce를 단순 python 문법으로 개발한 코드
        def my_Reduce():
            datas = [1, 2, 3, 4, 5]
            r = 0

            for i in datas:
                r = r + i

        my_Reduce()

filter(함수, 필터링당할 데이터들) : 데이터의 일부착출 가능한 함수(True만 추출)
    # 예제1 : 0~9에서 4이하만 추출
        list(filter(lambda a : a < 5, range(10)))
    # 예제2 : map과 비교
        list(map(lambda a : a < 5, range(10)))

## 미션 : (123,)값이 출력될 수 있게 ? 부분 완성
    list2 = (10,22,37,41,100,123,29) 

    list(filter(lambda a : a%123==0, list2))
    tuple(filter(lambda a : a%123==0, list2))
        