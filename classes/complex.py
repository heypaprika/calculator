#기본전제 변수안의 값을 byte단위는 어려우니까 생략 우선 기본값으로 가정후 완료시 
class complex_calu(object):
    def __init__(self):
        #어떻게 잘 들어와서 나뉜다 나뉘는게 j라는 기본클래스가 구현되어 어려워서 일단 생략
        #문자열을 클래스로 받을때 감이 안옴
        # 복소수는 복소수끼리 실수는실수끼리 연산을 기본전제
        #상상코드 두수를 받아서 j를 존재여부로 self.i1을 j없앤 숫자 두개다없으면 i1,2 둘다없으면 r1 r2  한개씩만 있으면 2들은None
        '''
        r1과 i1이 우선인자
        self.i1=i제외부분
        self.i2=i제외부분
        self.r1= 실수
        self.r2= 실수
        어떻게??
        실패!
        '''
        '''
        두번째 가정
        만약 인식이 문자열로 통째로그대로 올경우
        일차적으로 연산기호를 기준으로  숫자를 나눈고
        리스트를 
        for s in some_list:
        if "j" in s:
            다른 리스트로 이동
        리스트 두개 생성 
        이때 문제점 연산기호는 어떻게???
        sol1)
        처음 문자로 돌아가서 사용 
        prob)
        연산기호 인식어떻게??
        실패!!
        그러나 만약 계산기가 하나의 단위(ex)12124하고 입력 )씩 들어온다면??
        이건 원하는바 아님XXX
        '''
        '''
        세번째
        연산기호의미 정의를 다시해서 함수를 재정의 즉 +기호를 사용하면 연산되는 것을 
        재정의 해서 j가 있을때 없을때를 구분시켜서
        complex라는 클래스가 존재해서 MVC기준만들기 어려움
        문제점
        j라는 것을 안쓰면 i를 기준으로 허수 측으로 나누고 써야한다
        이때 i를 기준으로 쓰는데 파이썬에서 문자열은 ''을 붙여야 사용이 가능하다
        그러나 계산기를 사용할때는 123i라고 사용 어떻게 ''없이 사용???
        
        '''
    #잘 나뉘어 졌다고 하면???처음꺼 사용가능시
    def add(self):
        return r1+r2+(i1+i2)i
    def sub(self):
        return r1-r2+(i1-i2)i
        #빼기
    def mul(self):
        return r1*r2+(i1*i2)i
        #곱하기
    def div(self):
        return r1/r2+(i1/i2)i
        #나누기

class complex_cal(object):#문자열을 자동으로 연산기호의 것을 재정의한다면??
    #똑같이 문자열에대한 문제발생
    def __init__(self):
        self.first = first
        self.second = second

    def __add__(self,other):
        '''
        퍼스트와 세컨드의 데이터타입을 판단 j나 i 있으면(how??)
        복소수라생각         
        want
        복소수와 실수를 다른 파트로 계산하고싶다
        '''
        return a+b
    def __sub__(self, other):
        return a + b
    def __mul__(self, other):
        return a + b
    def __truediv__(self, other):
        return a + b
    def exp(self,other):
        return
a=complex_cal()
print(type(a))
