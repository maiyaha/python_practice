a1={}
a2=dict()
print(a1, a2, type(a1), type(a2))

a1={'a': 10,
    'b': 20,
    'c': 30}

print(a1, a1['c']) #키로 찾아옴 , 값으로는 못찾아옴

a1['오오'] = '우오' #추가
print(a1)

print(a1['오오'])
a1['a']='우악' #덮어쓰기
print(a1)

del a1['a'] #key로만 수정/추가해야함, 순서가 없으므로 삽입 개념 존재하지 않음
print(a1) 

print(a1.get('c')) #있는값 get 반환
print(a1.get('k')) #없는값 get시 None 반환

print(list(a1)) #key를 리스트로 나열
print(a1.keys())

print(a1.values()) #value를 리스트로 나열

print('----------')

print(a1.items()) #각 값을 튜플화해(하나의값으로) 리스트처럼 나열 : for문만들때 사용가능
print('-------------')
for a in a1.items():
    print(a)
    
