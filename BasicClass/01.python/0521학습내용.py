from typing import ValuesView


Comprehension
    1. 리스트, 세트, 딕셔너리 내에서 실행 할 수 있는 한 줄 for 문
    2. 리스트 컴프리헨션, 세트 컴프리헨션, 딕셔너리 컴프리헨션이라고 함
    3. 컴프리헨션 : 내장, 내포의 의미
        # 예제1 : 0~9까지 제곱하는 로직
            datas = []

            for x in range(10):
                datas.append(x**2)

            print(datas)

            datas2 = [x**2 for x in range(10)]

            print(datas2)

        # 예제2 : 0~5까지 반복해서 순차적으로 +2를 한 결과값들을 하나의 list에 저장 후 출력
            datas3 = [x+2 for x in range(6)]

            print(datas3)

        # 예제3 : 0~5까지의 데이터 중 짝수인 경우만 +2를 해서 list에 저장 및 출력하기
            datas4 = [x+2 for x in range(6) if x%2 == 0]

            print(datas4)

        # 예제4 : list에 튜플 생성해서 저장하는 로직
            combs = []

            for x in [1, 2, 3]:
                for y in [4, 5, 6]:
                    if x != y:
                        combs.append((x, y))

            print(combs)

            combs2 = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6] if x!= y]

            print(combs2)

        # 예제5 : dict 구조에 comprehension 적용해 보기
            data = {x:y for x, y in [(1, 'one'), (2, 'two')]}

            print(type(data))
            print(data)
            print(data[1])

        # 예제6 : range(1, 4)로 {1:2, 2:3, 3:4} 결과값이 나올수 있게 컴프리헨션 사용
            datas1 = {x:x+1 for x in range(1, 4)}

            print(datas1)

        # 예제7 : {80, 90, 70} 값만 출력되게 comprehension 적용
            score = {'A' : 90, 'B' : 80, 'C' : 70}
            rank_dict = {rank : name for rank, name in score.items()}

            print(rank_dict)

            for rank, name in score.items():
                print(f'{rank} : {name}')
            
            for v in score.values():
                print(v, end=' ')

        # 예제8 : value*value 식이 수행되는 로직 개발 (v = 0~9)
            [v*v for v in range(11)]    #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

        # 예제9 : 짝수만 value*value 식 수행
            [v*v for v in range(11) if v%2 == 0]   #[0, 4, 16, 36, 64, 100]
        
        # 예제10 : for 함수를 이용해서 [[10, 11, 12], [13, 14, 15], [16, 17, 18]] 생성
            lst = []

            for v1 in [0, 1, 2]:
                lst2 = []
                for v2 in [10, 11, 12]:
                    lst2.append(v1*3+v2)
                
                lst.append(lst2)
            
            print(lst)    #[[10, 11, 12], [13, 14, 15], [16, 17, 18]]

        # 예제11 : 예제 10을 Comprehension
            [[v1*3+v2 for v2 in [10, 11, 12]] for v1 in [0, 1, 2]]

## 미션1 : comprehension 문법으로 변경하기
    eve = []
    for i in range(10, 30):
        for j in range(10, 30):
            a = i * j
            if str(a) == str(a)[::-1]:
                eve.append(a)
    print(eve)      #[121, 242, 252, 252, 272, 464, 272, 323, 252, 414, 323, 494, 252, 525, 242, 484, 616, 414, 575, 696, 525, 575, 494, 676, 616, 464, 696]

    eve = [i * j for j in range(10, 30) for i in range(10, 30) if str(i * j) == str(i * j)[::-1] ]
    #[121, 242, 252, 252, 272, 464, 272, 323, 252, 414, 323, 494, 252, 525, 242, 484, 616, 414, 575, 696, 525, 575, 494, 676, 616, 464, 696]

## 미션2 : 제시된 코드와 동일한 로직의 comprehension 구성하기
    reference = [1, 2, 3, 4, 5, 6]

    output = []

    for number in reference:
        if number % 2 == 0:
            prev_num = number-1  # calculate previous number
            output.append(prev_num)  # append to the list

    print(output)   #[1, 3, 5]

    output = [number-1 for number in reference if number % 2 == 0 ]
    print(output)
    [number-1 for number in reference if number % 2 == 0 ]    #[1, 3, 5]

## 미션3 : 제시된 반복문등을 분석 하고 comprehension 문법 적용해서 결과에 맞게 구성하기
    list_string = ['encore', 'playdata', '교육', '4차 산업 인재상']

    for word in list_string:
        print(word)
        
    print("----- split() -----")
        
    for word in list_string:
        print(word.split())
        
        
    print('----- list에 저장 -----')
    list = []
    for word in list_string:
        list.append(word.split())
        
    print(list)
    #encore
    # playdata
    # 교육
    # 4차 산업 인재상
    # ----- split() -----
    # ['encore']
    # ['playdata']
    # ['교육']
    # ['4차', '산업', '인재상']
    # ----- list에 저장 -----
    # [['encore'], ['playdata'], ['교육'], ['4차', '산업', '인재상']]

    [print(word) for word in list_string]
    print("----- split() -----")
    [print(word.split()) for word in list_string]
    print("----- split() -----")
    [word.split() for word in list_string]

## 미션4 : 제시된 데이터를 활용하여 철자 길이가 4이상인 경우의 데이터에 한해서만 문자열의 첫 글자만 대문자로 및 출력
    words = ['encore', 'playdata', 'sw응용&분석', 'hi']

    [a.upper()[0]+a[1::] for a in words if len(a) >= 4]


zip(A, B) : A, B 두 그룹의 데이터를 서로 엮음(tuple 형태)
    # 예제1
    x = [1, 2, 3]
    y = [4, 5, 6]

    zipped = zip(x, y)

    print(zipped)    #<zip object at 0x000001A6A52F2400>
    
    all = list(zipped)
    print(all)    #[(1, 4), (2, 5), (3, 6)]

    # 예제2
    x = [1, 2, 3]
    y = [4, 5, 6]

    x2, y2 = zip(*zip(x, y))    # *(가변인수) 안넣으면 에러난다.

    print(x2, type(x2), type(x))  #(1, 2, 3) <class 'tuple'> <class 'list'>
    print(y2)   #(4, 5, 6)
    print(x == list(x2))  #True
    print(x == x2)   #False

    print(x == list(x2) and y == list(y2))   #True

    # 예제3 : zip 함수를 이용한 list들의 데이터를 활용하는 방법
    x = [1, 2, 3]
    y = [4, 5, 6]

    list(zip(x, y))    #[(1, 4), (2, 5), (3, 6)]

    list1 = list(zip(x, y))
    for i in list1:
        list2 = list1[i]   #(1, 4) (2, 5) (3, 6)
        for j in list2:
            list3 = list2[j]  # 1 2 3
            print(list3, ':', list2[j+1])

Exception : 예외처리기법
    1. try: 
            실행할 코드
       except: 
            예외가 발생했을 때 처리하는 코드
            # 예제1 : 반드시 1과 2가 출력
                try:
                    print(1)
                    print(10/0)
                except:
                    print('연산오류')
                print(2)

            # 예제2: pass 사용
                try:
                    print(1)
                    print(10/0)
                except:
                    pass
                print(2)

    2. try: 
            실행할 코드
       except 예외이름: 
            예외가 발생했을 때 처리하는 코드
            # 예제1 : IndexError 발생시
                try:
                    print(1)
                    print(10/0)
                except IndexError:     # 미존재하는 index값 입력한 경우
                    print('index 오류')
                except ZeroDivisionError:   # 0으로 나눌 경우
                    print('연산오류')
                print(2)

            # 예제2 : input 이용
                data = [10, 20, 30]
                
                try:
                    index, div_number = input('인덱스와 나눌 숫자를 입력하세요: ').split()
                    print('연산된 결과값', ':', data[int(index)] / int(div_number))
                except IndexError:
                    print('발생되는 모든 예외 처리')

    3. try: 
            실행할 코드
       except 예외 as 변수: 
            예외가 발생했을 때 처리하는 코드
            # 예제1 :  예외의 에러 메세지 받아오기
                data = [10, 20, 30]

                try:
                    index, div_number = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
                    print('연산된 결과값: ', data[index] / div_number)
                except ZeroDivisionError as e:
                    print('숫자를 0으로 나눌 수 없습니다', e)
                except IndexError as e:
                    print('입력하신 인덱스엔 데이터가 존재하지 않습니다', e)

    4. try: 
            실행할 코드
       except: 
            예외가 발생했을 때 처리하는 코드
       else:
            예외가 발생하지 않았을 때 실행할 코드
            # 예제1 : map(int, input().split) = input한 데이터를 split()으로 구분후에 int로 변환해주는 코드
                try:
                    index, div_number = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
                    print('연산된 결과값', data[index] / div_number)
                except ZeroDivisionError as e:
                    print('숫자를 0으로 나눌 수 없습니다', e)
                except IndexError as e:
                    print('입력하신 인덱스엔 데이터가 존재하지 않습니다', e)
                else:
                    print('예외가 발생되지 않았을 때만 실핻되는 블록')

    5. try: 
            실행할 코드
       except: 
            예외가 발생했을 때 처리하는 코드
       else:
            예외가 발생하지 않았을 때 실행할 코드
       finally:
            예외 발생 여부와 상관 없이 항상 실행할 코드
            # 예제1
                try:
                    index, div_number = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
                    print('연산된 결과값: ', data[index] / div_number)
                except ZeroDivisionError as e:
                    print('숫자를 0으로 나눌 수 없습니다', e)
                except IndexError as e:
                    print('입력하신 인덱스엔 데이터가 존재하지 않습니다', e)
                else:
                    print('예외가 발생되지 않았을 때만 실행되는 블록')
                finally:
                    print('로직 종료')

## 미션1 : 5의 배수가 아닌경우 예외 발생시키기
    try:
        x = int(input('5의 배수를 입력하세요: '))
        
        if x % 5 == 0:
            print(f'{x}는 5의 배수입니다')
        elif x% 5 != 0:
            print(f'{x}는 5의 배수가 아닙니다') 
    except Exception as e:
        print('5의 배수가 아닌 예외 발생')

## 미션2 : 18미만인 경우 예외 발생(raise : 사용자가 에러를 직접 발생시키는 기능)
    try:
        age = int(input('나이를 입력하세요: '))

        if age < 18:
            raise ValueError
        else:
            print('출입 가능')
    except ValueError:
        print('미성년자 출입불가')

## 미션3 : id가 master인 경우에만 인증성공, master가 아니라면 예외 발생
    try:
        id = input('id를 입력하세요: ')

        if id == 'master':
            print('인증성공')
        else:
            raise Exception
    except Exception:
        print('인증실패')

## 미션4 : id값 검증하는 함수 개발해서 master인 경우에만 인증성공/master가 아니라면 예외 발생
    def login(id):
        if id == 'master':
            print('인증성공')
        else:
            print('인증실패')


Assertion(단정문) : assert(가정설정문)는 뒤의 조건이 False인 경우 AssertionError를 발생
    1. if 조건식과 흡사한듯 하나 if 코드는 실제 end user가 입력되는 상황등을 검증시에 주로사용
    2. 개발시 상황에 따른 검증코드로 주로 사용
    3. 개발시에 개발 로직 검증 후에 실제 client에게 서비스 하게 되는 시점에 삭제 또는 주석
    4. 개발자 관점에서 안정적인 코드를 구현하기 위한 형식
        # 예제1 : 데이터가 0보다 큰 수 여야만 하는 상황인 경우
            def checkPositive(v):
                assert v > 0, '0보다 큰 수가 아닙니다.'

                print('단정문 실행 직후')
                return '0보다 큰 수 입니다.'

        # 예제2 : ..{}.format(변수) 이용
            result = 1 - 3
            assert result > 0, '에러{}'.format(result)
            print('실행 여부 확인')