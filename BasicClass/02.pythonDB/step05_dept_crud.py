'''
 dept table : deptno는 절대 중복 불허
     1. crud 로직만 구현
    2.예외처리를 꼼꼼하게 구현
fetch 종류와 예시 : https://cx-oracle.readthedocs.io/en/latest/user_guide/sql_execution.html#fetch-methods
'''

import cx_Oracle # python과 oracle을 연동할 수 있게 해주는 모듈


# dept01 table 생성(단 deptno는 pk로 설정)
def dept01_create():
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")  # cx_Oracle.connect(id, pw, 개별 db별 별칭(database service name(dsn))를 이용해 DB에 접속
        cur = conn.cursor()    # cursor() : 연결한 DB와 상호작용을 위한 객체생성

        try:
            cur.execute("drop table dept01")  # cur.execute("sql문장") : 생성한 cursor 객체를 이용해 소괄호 안의 "sql문장" 실행

            try:    
                cur.execute("create table dept01 as select * from dept")
                try:
                    cur.execute("alter table dept01 add constraint pk_dept01_deptno primary key(deptno)")   # deptno를 pk로 설정하여 중복, null 방지
                    conn.commit()     # commit()하지 않으면 execute()를 아무리해도 결과가 DB에 반영 안됨
                except Exception as e:     # 에러 종류를 포괄적으로 받는 Exception 사용해 출력
                    print(e)      
                     
            except Exception as e:     # 에러 종류를 포괄적으로 받는 Exception 사용해 출력
                print(e)

        except:
            print('dept01 table 미존재')

    except Exception as e:
        print(e)

    finally:
        cur.close()
        conn.close()     # 항상 cursor / connection은 종료해주어야함!


# dept01 데이터 전체 출력
def dept01_query_all():
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        cur = conn.cursor()

        try:
            cur.execute("select * from dept01")
            conn.commit()

            try:
                rows = cur.fetchall()    # fetchall() : 모든 데이터를 한번에 가져옴
                for row in rows:         # fetchone() : 한 번 호출에 하나의 행만 가져올 때 사용
                    print(row)           # fetchmany(n) : n개 만큼의 데이터를 가져올 때 사용
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)

    except Exception as e:
        print(e)

    finally:
        cur.close()
        conn.close()



# 부서이름의 일부 혹은 전체를 입력하여 부서번호와 위치 출력
def dept01_query_one1(dname):
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        cur = conn.cursor()

        try:
            cur.execute("select * from dept01 where dname like :dname", dname=dname)
            conn.commit()

            try:
                rows = cur.fetchall()
                print(rows)
            except Exception as e:
                print(e)  

        except:
            print('table 생성시 오류')  

    except Exception as e:
        print(e)

    finally:
        cur.close()
        conn.close()



# 부서번호를 입력하여 부서이름과 위치를 출력
def dept01_query_one2(deptno):
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        cur = conn.cursor()

        try:
            cur.execute("select * from dept01 where deptno=:deptno", deptno=deptno)
            conn.commit()

            try:
                rows = cur.fetchall()
                print(rows)
            except Exception as e:
                print(e)  

        except:
            print('table 생성시 오류')  

    except Exception as e:
        print(e)

    finally:
        cur.close()
        conn.close()



# dept01에 새로운 데이터를 추가(단 deptno는 pk이므로 중복불가)
def dept01_insert(new_deptno, new_dname, new_loc):
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        cur = conn.cursor()

        try:
            cur.execute("insert into dept01 values (:new_deptno, :new_dname, :new_loc)", new_deptno=new_deptno, new_dname=new_dname, new_loc=new_loc)
            conn.commit()
        except Exception as e:
            print(e)

    except Exception as e:
        print(e)

    finally:
        cur.close()
        conn.close()



# deptno의 기존 데이터를 업데이트(deptno가 pk이므로 deptno를 기준으로 업데이트)
def dept01_update(deptno, new_dname, new_loc):
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        cur = conn.cursor()
    
        try:
            cur.execute("update dept01 set dname=:new_dname, loc=:new_loc where deptno=:deptno", new_dname=new_dname, new_loc=new_loc, deptno=deptno)
            conn.commit()
        except Exception as e:
            print(e)

    except Exception as e:
        print(e)

    finally:
        cur.close()
        conn.close()


# dept01의 데이터 삭제(deptno가 pk이므로 deptno를 기준으로 삭제)
def dept01_delete(del_deptno):
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        cur = conn.cursor()
    
        try:
            cur.execute("delete from dept01 where deptno=:deptno", deptno=del_deptno)
            conn.commit()
        except Exception as e:
            print(e)

    except Exception as e:
        print(e)

    finally:
        cur.close()
        conn.close()



if __name__ == '__main__':
    # dept01_create()
    # dept01_query_all()
    # dept01_query_one1('%NG')
    # dept01_query_one2(10)
    # dept01_query_all()
    # dept01_insert(80, "복지부", "서울")
    # dept01_query_all()
    # dept01_insert(10, "복지부", "서울")
    # dept01_query_all()
    # dept01_update(80, "인사부", '판교')
    # dept01_query_all()
    # dept01_delete(80)
    # dept01_query_all()