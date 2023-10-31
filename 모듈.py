import testmodule1

import testmodule1

from testmodule2 import test2_f1 #하나만 불러오기
import testmodule2 #이름적어 불러오기
from testmodule3 import * #전부불러오기 - 중복 이름이 존재한다면 꼬일수있음

test2_f1() #하나만 불러오기

testmodule2.test2_f2() #이름적어 불러오기

test3_f1() # 모듈을 *로 불러옴

#단, 타 모듈에 같은 이름의 요소가 없을 때에만 모듈명을 생략할 수 있음

import testmodule4 as t4 #별칭

