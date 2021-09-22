'''
1. 모든 지역에 거주하는 대상 가구수의 합
2. 가구당 평균 전력사용량의 총 평균
3. 가구당 평균 전기요금의 합
'''
import csv

newhouse = [] #대상 가구수(호)
newVolt = [] #가구당 평균 전력사용량(kWh)
newPay = [] #가구당 평균 전기요금(원)

with open("../지역별_전기요금_정보_2021.05_.csv", "r") as f:
    csv_reader = csv.reader(f)
       
    for row in csv_reader:
        # print(type(row[0]),  type(row[1]), type(row[2]))   # ""로 묶여있지 않아도 python에서 읽어들일때 string으로 인식해서 읽어드림
        print('-', row[1], '-')   # -  -같은 데이터가 출력되는 것은 raw 데이터에 ,가 인식되는데 python에서 읽어들일때 구분자로 인식하므로 len()=0 인 문자열()로 출력됨
        newhouse.append(row[1].strip().replace(",", "")) #index 1 즉 두번째 컬럼값의 데이터 앞뒤 잉여여백 제고 및 제거+
        newVolt.append(row[2].strip().replace(",", ""))
        newPay.append(row[3].strip().replace(",", ""))
    # print(newhouse)  # row[1] : strip()으로 앞뒤공백 제거 후 replace로 ,를 len()=0 인 문자열로 변환
    # print(newVolt)   # row[2] : strip()으로 앞뒤공백 제거 후 replace로 ,를 len()=0 인 문자열로 변환
    # print(newPay)    # row[3] : strip()으로 앞뒤공백 제거 후 replace로 ,를 len()=0 인 문자열로 변환

def sum(sumList):
    sum = 0
    for i in range(1, len(sumList)):
        if(sumList[i] != ""):   # ''는 int로 변환이 안되어서 ValueError: invalid literal for int() with base 10: '' 에러 나옴
            sum = sum + int(sumList[i])
        else:
            pass
    return sum


def avg(avgObject):
    count = 0
    for i in range(1, len(avgObject)):
        if(avgObject[i] != ""):      # ''는 int로 변환이 안되어서 ValueError: invalid literal for int() with base 10: '' 에러 나옴
            count += 1
    
    return (sum(avgObject)/count)    # 더한 data수만큼 나누어서 평균낸값을 리턴

print(sum(newhouse))
print(sum(newPay))
print(avg(newVolt))

'''
14882047
565472
335.1764705882353
'''    