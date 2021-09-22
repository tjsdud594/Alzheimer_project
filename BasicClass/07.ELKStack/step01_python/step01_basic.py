from datetime import datetime
from elasticsearch import Elasticsearch

# ES를 사용가능한 python 객체 생성, 접속, doc생성, 검색등이 다 가능한 기능을 보유한 객체
# 이 소스가 실행중인 시스템(해당 ip)에서 실행되는 ES에 자동 접속
es = Elasticsearch()


# index가 test-index인 파일 생성
def put():
    '''
    doc라는 변수에 3개의 field 선언해서 값 설정
    python 자체적으론 dict 타입
    es관점에선 field와 value
    datetime.now() : 현 날짜시간 표현
    '''
    doc = {
        'author': 'kimchy',
        'text': 'Elasticsearch: cool. bonsai cool.',
        'timestamp': datetime.now(),
    }

    '''
    es.index(index="test-index", id=1, body=doc)
    es : Elasticsearch 객체
    index() : ES보유한 index 생성 함수
    * 용어정리 : index 생성은 RDBMS관점에서 table 생성 + 데이터 저장
    index명 = : index로 사용할 이름을 설정
    id : pk와 같이 고유한 id값 설정 의미
    =1 : id값으로 1 의미
    body : index에 설정한 table과 같은 index구조에 id값과 저장될 데이터 설정하는 속성
    =doc : dict 구조의 변수값으로 index에 새로운 데이터 생성, 이미 존재할 경우 update
    '''
    res = es.index(index="test-index", id=1, body=doc)
    print(res['result'])
    
def get():
    res = es.get(index="test-index", id=1)
    print(res['_source'])
    

# es.indices.refresh(index="test-index")

def match_all():
    '''
    GET test-index/_search
    {
    "query": {
        "match_all": {}
        }
    }
    '''
    res = es.search(index="test-index", body={"query": {"match_all": {}}})

    # %d 가변적인 데이터 단 d는 디지털 약자 즉 숫자 의미
    print("Got %d Hits:" % res['hits']['total']['value'])

    for hit in res['hits']['hits']:
        '''키바나 결과
        "_source" : {
            "author" : "kimchy",
            "text" : "Elasticsearch: cool. bonsai cool.",
            "timestamp" : "2021-07-13"
            }
        '''
        # 콘솔창에 출력된 결과
        # 2021-07-13T09:48:55.988382 kimchy: Elasticsearch: cool. bonsai cool.
        # %(키)s %(키2)s   % dict 구조의 데이터의 해당 key와 일치되는 데이터를 문자열 포맷에 자동 적용
        print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

        # kimchy / 2021-07-13T09:48:55.988382 / Elasticsearch: cool. bonsai cool.
        print("%(author)s / %(timestamp)s / %(text)s" % hit["_source"])

        # test-index
        print(hit["_index"])
    
def bank_search():
    res = es.search(index="bank", body={"query": {"match": {"bank":"국민은행"}}, "size": 0, "aggs": {"b_1": {"terms": {"field": "customers"}}}})
    print(res["aggregations"]["b_1"])
    for bucket in res["aggregations"]["b_1"]["buckets"]:
        print("방문고객: %(key)s명, 지점수: %(doc_count)s" % bucket)

def bank_search2():
    res = es.search(index="bank", body={"size": 0, "aggs": {"b_2": {"cardinality": {"field": "branch.keyword"}}}})
    print("지점 종류: %d" %res["aggregations"]["b_2"]["value"])


def bank_get():
    res = es.search(index="bank", body={"query": {"match": { "bank": "국민은행"}}})
    print(res)
    print("집계 개수 %d" % res['hits']['total']['value'])
    # print(res['aggregations'])


def bank_get2():
    res = es.search(index="bank", body={"query": { "match": { "bank": "국민은행" }},"size": 0,  "aggs": { "b_1": {"terms": { "field": "customers"}}}})
    print(res["aggregations"]["b_1"]["buckets"])
    for bucket in res["aggregations"]["b_1"]["buckets"]:
        print("고객수: %(key)s, 지점수: %(doc_count)s" % bucket)
    

def bank_search3():
    res = es.search(index="bank", body={"query": {"match": {"bank": "NH농협은행"}}, "size": 0, "aggs": {"b_4": {"histogram": {"field": "customers", "interval": 1000}}}})
    print(res["aggregations"]["b_4"]["buckets"])
    for bucket in res["aggregations"]["b_4"]["buckets"]:
        # print(bucket)
        print("%(key)s명 이하 인원 방문: %(doc_count)s개" % bucket)


if __name__=="__main__":
    # put()
    # get()
    # match_all()
    # bank_search()
    # bank_search2()
    # bank_get()
    bank_get2()
    # bank_search3()