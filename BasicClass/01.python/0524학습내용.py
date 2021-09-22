Class : 객체를 사용 가능하게 해주는 설계도
    1. 객체(object) : 메모리에 사용 가능하게 생성된 데이터 집합, class가 있어야 나올 수 있음
    2. 붕어빵틀 - class / 붕어빵 - 객체
    3. 객체 지향 프로그램 방식의 주 목적 : 클래스 하나 제대로 설계 후에 데이터 표현을 위한 재사용을 위함
    4. java script, java 라는 프로그램 언어에 동일한 개발 형식
    5. 다수의 데이터값을 보유할 수 있는 프로그램 구조
    6. 메소드 = 클래스 내부에 구현되는 기능 / 함수 = 클래스와 독립적으로 구현되는 기능

        # 예제1 
            class Person:

                def __init__(self, name, age):
                    self.name = name
                    self.age = age

            p1 = Person('백종원', 54)
            p2 = Person('류선영', 27)
            print(p1.name)
            print(p2.age)

        # 예제2
            class Student:
                def __init__(self, no, name, grade):
                    self.no = no
                    self.name = name
                    self.grade = grade

                def getName(self):
                    return self.name
                
                def setName(self, name):
                    self.name = name

            s1 = Student(1, '류선영', '1학년')
            s2 = Student(2, '백종원', '2학년')

            print(s1.getName())    #류선영
            print(s2.getName())    #백종원
            s2.setName('유재석')
            print(s2.getName())    #유재석

        # 예제3
            class Bank:
                bank_name = '플레이데이터 은행'

                def __init__(self, loc):
                    self.loc = loc

            b1 = Bank('마포')
            print(b1.bank_name, '의 지점 위치 - ', b1.loc)
            print(Bank.bank_name, '의 지점 위치 - ', b1.loc)
            print(b1.loc)

    7. static 변수 : static 키워드로 선언 = 객체 생성없이 사용 가능
    8. instance 변수 : non-static으로 선언 = 객체 생성 필수(instance), self가 적용된 변수
    9. python에선 public(무) 또는 private(__)로 표기
        # 예제1 : instance변수
            class UserClass:
                
                def __init__(self, data):
                    self.instanceVar = data
                    print('생성자')

                def getInstanceVar(self):
                    return self.instanceVar

            d = UserClass('생성자로 유입되는 데이터들')
            i = UserClass('변수')
            data1 = d.getInstanceVar()
            data2 = i.getInstanceVar()
            print(data1)
            print(data2)

        # 예제2 : getXxx() / setXxx()
            class Person():

                def __init__(self, name, age):
                    self.name = name
                    self.age = age

                def getName(self):
                    return self.name
                
                def getAge(self):
                    return self.age

                def setName(self, new_name):
                    self.name = new_name

                def setAge(self, new_age):
                    if new_age > 0:        # 새로입력한 나이가 양수일 경우에만 수정
                        self.age = new_age

            p1 = Person('류선영', 27)
            p2 = Person('백종원', 54)
            
            print(p1.getName())
            p1.setName('유재석')
            print(p1.getName())