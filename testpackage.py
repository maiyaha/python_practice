import package.testpack1 #폴더명과 현재파일명 겹치면 안됨

package.testpack1.test5_f1()

from package2 import testpack2 

testpack2.test6_f1() #패키지명생략

from package3.testpack3 import test7_f1, test7_f2 #전부생략하지만 지정됨
#단, 다른 패키지/모듈에도 같은 이름 있을수 있으니 전부임포트(*) 주의

test7_f2()

from package4 import * # __init__.py 필요
testpack4.test8_f1()