a1=0

while a1<10:
    a1=a1+1
    print(a1)
    
a2=0
while a2<10:
    a2=a2+1
    print(a2)
# else:
print('종료') #들여쓰기차이로 윗문장끝나면 무조건실행

A=[1,2,3,4,5]
 
for a in A:
    print(a)
    
for b in range(10): # 0~9 무조건 출력, range:반복횟수
    print(b)
    
C='python'
for c in C:
    if c is 'h': #작동안함
        break
    print(c)

C='python'

for c in C:
    if c is [3] : #작동안함
        break
    print(c)

        

C=['p','y','t','h','o','n']

for c in C:
    if c is 'h' :
        break
    print(c)


    C=[1,2,3,4,5]

    for c in C:
        if c > 4 :
            
            break
        print(c)
        
        

D=[0,1,2,3,4]

for d in D:
    if d % 2== 0:
        continue #해당하면 뛰어넘고 다음반복으로
    print(d)
    
    
    
    
D=[0,1,2,3,4]

for d in D:
    if d % 2== 0:
        continue #해당하면 뛰어넘고 다음반복으로
    print(d)

    for d in D:
        if d % 2== 1:
            continue #해당하면 뛰어넘고 다음반복으로
        print(d)
        
#1->024->3->024