def test1():
    print('hi')
    print('123')
    
test1()

print(test1) #함수는 변수에 포함-함수의 id가 출력됨
print(test1())
test2=test1

test2()

test1=1000 #함수라는 변수에 int를 삽입
# test1() #오류

print(test1) #()붙이면 함수호출-int출력요구-이기때문에 오류발생함
             #현재 test1=1000이라는 변수를 출력함
             
def test3(a1,a2,a3,a4,a5): #매개변수 
    print(a1,a2)
    print(a3,a5,a5) #하나가 실제로 사용되지 않아도 매개변수는 모두 필요
    
test3(3,6,8,6,5) #매개변수는 갯수맞춰 주어져야함
test3('a','b','c','d','e')#부족하거나 많을경우 에러발생
test3(a5=1,a4=2,a1=2,a2=6,a3=7) #하나가 실제로 사용되지 않아도 매개변수는 모두 필요

             
def test3(a1,a2,a3,a5,a4=3): #매개변수에 기본값 지정한 경우 지정 값 뒤 순서는 전부 기본값 필요
    print(a1,a2)
    print(a3,a5,a5) 
    
test3(a5=1,a1=2,a2=6,a3=7) #매개변수 기본값 지정한 경우 오류 발생하지 않음

# def test3(a1, a2, a3, a4=3, a5): #오류발생
#     print(a1, a2)
#     print(a3, a4, a5)

# test3(a1=2, a2=6, a3=7, a5=1) 

def test4(a1,a2):
    r1=a1+a2
    return r1


print(test4(3,4))
print(test4(2,3))

def test5(a1,a2):
    r1=a1+a2
    r2=a1-a2
    r3=a1//a2
    r4=a1*a2
    return r1,r2,r3,r4

print(type(test5(3,5)), test5(3,5)) # 여러결과값 한꺼뻔에 반환할땐 튜플로반환
k1, k2, k3, k4 = test5(3,5)
print(k1,k2,k3,k4) #튜플의 분해