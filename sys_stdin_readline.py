# jupyter 에서는 input만 써야함,,

# import sys
# setence = sys.stdin.readline()

# sys.stdin.readline 은 return 값이 문자열이므로  / 그냥 문장 하나 받을때사용가능
# sys.stdin.readline 을 출력하면 문자열에 계행 \n 이 기본으로 추가됨

# import sys
# number = int(sys.stdin.readline())
# print(type(number))

# sys.stdin.readline() 의 return 값은 문자열 이기 때문에 정수로 입력받으려면 형 변환을 해야한다
# sys.stdin.readline() 으로 받은 문자열은 계행문자 \n 을 포함한다

# import sys
# n = int(sys.stdin.readline())
# data = [sys.stdin.readline().strip() for i in range(n)]

# sys 모듈은 python 인터프리터가 제공하는 변수와 함수를 직접 제어할수 있게 해주는 모듈
# stdin은 sys 모듈 안에 있는 파일 객체이고
# stdin은 파이썬 인터프리터가 표준 입력에 사용하는 파일 객체
# readline 은 파일객체의 메서드중 하나로 read(), readlines() 와 같이 파일객체를 읽을때 사용

# sys.stdin.readline()은  sys라는 모듈의 파일객체 stdin의 메소드 중 readline()을 사용한다는 의미
# readline()은  입력을 읽을때 한번에 한줄씩 읽는데
# 이말은 여러줄의 입력이 있을때 한줄을 읽고 나면 그 다음 줄을 가리킨다는것

# input() 과의 차이점 내장함수
# sys.stdin.readline() file object
# input 은 공백을 제거하고 결과를 return 하는 반면 sys.stdin.readline()은 공백 계행 문자 등을 함께 리턴 하므로 strip() 써야함
# input 은 읽을게 없으면 EOP에러 sys.stdin.readline()은  읽을게 없을때 빈 문자열을 return 한다

# s = input()
# print(list(s))

import sys
s = sys.stdin.readline().strip()
print(list(s))

# strip 사용
