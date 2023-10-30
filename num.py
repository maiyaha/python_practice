import math, random


a1=abs(10)
a2=abs(-1)
print(a1,a2)


#소수점
a1=math.ceil(5.35)
a2=math.ceil(-5.35) #올림

print(a1,a2)

a1=math.floor(5.35)
a2=math.floor(-5.35) #내림

print(a1,a2)


a1=min(30,10,-239 ,4)
a2=max(30,10,-239 ,4)
a3=(30,10,-239 ,4)

print(a1,a2,a3)

a4=round(3213.545) #소수점안보여줌
a5=round(3213.231,1) #소수점첫째까지보여줌
a6=round(3213.231,2) #소수점둘쨰까지보여줌
a7=round(3213.231,-1) #정수첫째자리에서반올림
print(a4, a5, a6, a7)


a1=[1,2,3,4,5]
a2='finder'
v1=random.choice(a1)
v2=random.choice(a1)
v3=random.choice(a1)
v4=random.choice(a2)
print(v1,v2,v3,v4)

a1=random.randrange(100)
print(a1)
# a2=random.randrange('friends') #str은작동안함
# print(a2)
a3=random.randrange(5,50) #50은나오지않음
print(a3)

a4=random.randrange(5,20, 3) #20은나오지않음
print(a4)

a5=random.random()
print(a5) #0<=a5< 1

a1=[1,2,3,4,5,6,7,8,9,10]
random.shuffle(a1)
print(a1)

a1=random.randint(5,20)
print(a1)



'''random.randint와 random.randrange의 설계 차이는 Python의 역사와 API 설계 원칙에 기인합니다. 이러한 설계 차이는 다음과 같은 이유로 결정되었습니다:

random.randint:

이 함수는 "inclusive" 방식으로 작동합니다. 즉, 최솟값과 최댓값을 포함하여 범위 내의 정수를 생성합니다. 이것은 직관적이며 사용하기 간편하며 일반적인 경우에 적합합니다.
random.randrange:

이 함수는 "exclusive" 방식으로 작동합니다. 즉, 시작 값은 포함하지만, 끝 값은 포함하지 않습니다. 이 설계는 다른 언어 및 수학에서 일반적인 방식으로 범위를 지정하는 데 사용됩니다. 이 설계는 특정 수학적 문제나 다른 프로그래밍 언어와의 호환성을 고려할 때 유용합니다.
Python의 설계자들은 이러한 설계 선택을 커뮤니티의 요구 사항과 일반적인 사용 사례에 맞추어 결정했습니다. 이렇게 함으로써 Python은 다양한 문제 해결 및 응용 프로그램 개발에 적합한 도구가 될 수 있습니다.'''


#str

str1='python'
str2=str1.center(20,'-')
print(str2)

str2=str1.ljust(20,'-')
print(str2)

str2=str1.rjust(20,'-')
print(str2)

a1='asdf fdsa sdaf asdf'
a2='asdffdsasdafasdf'

print(a1.count('asdf'))
print(a1.count('a'))
print(a1.count('a', 8)) #3 공백도 인덱스에 포함
print(a2.count('a', 8)) #2 시작점은 세지않음(앞에서부터 8글자 제외)

print(len(a1))
print(len(a2))

print(a1.startswith('asdf'))
print(a1.endswith('asdf'))
print(a1.endswith('as'))
print(a1.find('df')) # 0 1 2(세번째에등장)
print(a1.find('fdd')) # -1 == false
print(a1.index('dd')) # ValueError: substring not found

a1='asdf12323fdsasdafasdf54564'
str1=a1.isalnum()
print(str1)

a1='asdf 12323 fdsasdafasdf54564' #공백있으면 인식못함
str1=a1.isalnum()
print(str1)

a1='fdsasdafasdf54564' #공백없으면 인식함
str1=a1.isalnum()
print(str1)

a1='fdsasdafasdf54564' 
str1=a1.isdigit()
print(str1)
str1=a1.isalpha()
print(str1)

a1='54564'
str1=a1.isdigit()
print(str1)
a1='fdsasdafasdf'
str1=a1.isalpha()
print(str1)

a1='5456 4'
str1=a1.isdigit() #공백인식못해 false
print(str1)
a1='fdsasdafa sdf'
str1=a1.isalpha() #공백인식못해 false
print(str1)


print(a1.islower()) #이둘은 공백있어도 인식
print(a1.isupper())

a1='fdsasAAfa sdf'
print(a1.islower())

a1='dasfsd'
a2='123123'
print(a1.join(a2)) #자동 for...인듯?

a1=['dasfsd', '12312', 'dfg']
a2='-'
a=a2.join(a1) #a2로 a1을 조인하기-순서주의, str만
print(a)

a1='asdfasdf'
a2='ASDFASDF'
print(a1.upper())
print(a2.lower())

print(a1.replace('df', 'jkl'))

a1='fdsa-sAAfa sdf'
print(a1.split())
print(a1.split('s'))