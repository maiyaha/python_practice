a1 = 10
if a1 == 10:
    print('if O')
    pass


if a1 != 10: #FALSE이기때문에 ELSE없으면 출력안됨
        print('if O') 
else:
        print('if X')
print('if X') #무조건출력됨

if a1==20:
    print('a1=20')
elif a1==39:
    print('a1=39')
elif a1==50:
    print('a1=50')
# elif a1==10:
#     print('a1=10')
else:
    print('a1=38')