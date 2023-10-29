print('복소수', 50+9j)
print('지수', 10e3)
print('세자리', 123_456_789) #언더바로표시, 프린트되진 않음

print(type(112.23))
print(type(10e3))
print(type(50+9j))
print(type(11223))
print(type(True))
print(type('True'))

a1=a2=a3=100

print(a1)
print(a2)
print(a3)

a1, a2, a3 = 100, 2000, 30000

print(a1)
print(a2)
print(a3)

a2=("asdf")
print(a2*4)
print(a2*4+'5')

print(11.11+float('11.1'))
print(11.11+'11.1') #계산불가

tuple=(1,2,3,4,5)
list=[1,2,3,4,5]
print(tuple)
print(list)

print(tuple[1:3])
print(list[1:3])

dic1 = {'v1':11, 'v2':12, 'v3':13}

print(dic1)
print(dic1['v1'])