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