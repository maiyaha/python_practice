a1=list()
a2=[]

print(type(a1), type(a2), a1, a2)

a1=[1,2,3,4,5]
a2=[6,7,8,9,1,2,3]
a3=a1+a2
print(a1+a2)
print(a3*3)

#index()는 str과 동일

print(len(a1),len(a2),len(a3))
print(min(a2), max(a2))

a1=(1,2,3,4,5)
a2=[a1] #리스트속 요소1개=튜플
print(a1,a2)
print(a2.index(1)) #요소1이없음
a1=(1,2,3,4,5)
a3=list(a1) #리스트속 요소5개
print(a1,a3)
print(a3.index(1)) #요소1이0번째인덱스에있음


a1='let me drop the 음악'
a2=list(a1)
print(a1, a2, a1.split(' '))
a3=a1.split(' ')
print(a3.index('음악')) #4
print(a3.append('워')) #추가됨, 출력할 반환 없음
print(a3) #추가된 결과 출력

## 튜플/리스트에서는 find 지원 안함 ##

print(f'결과: {a3}')
a3.insert(0, '워워') #주의 : a3=a3인경우 a3가 None이되어 반환값 없음
print(a3)

v1=a3[-1]
print(a3, v1)
print(a3.pop(2))
print(a3)
print(a3.remove('the'))
print(a3)

a3.sort()
print(a3)
a3.reverse()
print(a3)



# tuple : 첫생성 그대로 감

a1=tuple()
a2=()
print(a1, a2, type(a1), type(a2))

t1=1,2,3,4,5
print(t1, type(t1))

print(t1[-1], t1[:3], t1[2:], t1[:3]+t1[2:])

t2=t1+(7,8,9,1,2,3)*2
print(t2)


tone=()
lone=[3,4,5]
tlist=tuple(lone) # 리스트를 튜플화
ltuple=(tone)

print(tone, lone, tlist, ltuple)
print(type(tone), type(lone), type(tlist), type(ltuple))

a1='myfreind'
t1=(a1) # 튜플화 안됨
print(t1, type(t1))
t1=tuple(a1) #튜플화됨
print(t1, type(t1))

#분해(unpack)
tuple = 1,2,3,4,5
list = [1,2,3,4,5]
a1, a2, a3, a4, a5 = tuple
b1, b2, b3, b4, b5 = list

print(a3, b5)

print(a2)

c1, c2, c3 = 1, 2, 3 # 사실 변수지정이면서 튜플을 생성한것임
print(c1, c2, c3)

#append, insert등 제외하고 리스트와 동일


#''' 리스트는 다양한 요소를 저장하고 
# 동적으로 관리해야 하는 상황에서 유용합니다. 예를 들어,
# 목록, 스택, 큐 등의 자료 구조를 구현하거나 
# 데이터 필터링 및 수정 등에 사용됩니다.'''
#'''튜플은 변경되지 않아야 하는 데이터를 저장하는 데 유용합니다.
# 예를 들어, 함수에서 여러 값을 반환하는 경우, 
# 데이터베이스 레코드, 좌표(위도, 경도) 등에 사용됩니다.'''