# 백준 1000번
A, B = map(int, input().split())
print(A + B)

A, B = input().split()
x = int(A)
y = int(B)
print(x + y)


# split 함수
# 문자열.split()
# 문자열.split('구분자')
# 문자열.split('구분자', 분활횟수)
# 문자열.split('구분자', maxsplit = 분할횟수) # 이게 제일 정확함

# 문자열.split 함수는 문자열을 일정한 규칙으로 잘라서 리스트로 만들어주는 함수
# 문자열.split(sep, maxsplit) 함수는 문자열 maxsplit 횟수만큼
# sep의 구분자 기준으로 문자열을 구분하여 잘라서 리스트로만듬

# sep 파라미터
# 기본값은 none 이고 이때 동작은 띄어쓰기 엔터를 구분자로하여 문자열을 자름
# 문자열.split(sep=',') 이라 한다면 문자열에서 ','를 기준으로 자름
# sep는 생략하고 문자열.split(',') 사용해도 무방함

# maxsplit 파라미터
# 기본값은 -1 이고 이때 동작은 제한없이 자를수 있을때까지 문자열 전체를 자름
# 문자열.split(maxsplit = 1) 이라 하면 문자열을 1번만 자르게됨
# maxsplit를 생략이 가능하지만 앞에 sep 파라미터가 있어야 사용가능

# 문자열.split(1) 불가능
# 문자열.split(",", 1) 가능
# 문자열.split(maxsplit = 1) 가능


# 1001번
A, B = map(int, input().split())
print(A - B)

# 10998번
A, B = map(int, input().split())
print(A * B)

# 1008 번
A, B = map(int, input().split())
print(A / B)

# 10869번 내꺼답
A, B = map(int, input().split())
print(A + B)
print(A - B)
print(A * B)
print(round(A / B))
print(A % B)

# 찾아본답..
a, b = input().split()
a = int(a)
b = int(b)
print(a + b)
print(a - b)
print(a * b)
print(int(a/b))
print(a % b)

# round() 함수써도 답 똑같이나오는데 int를 써야만 인정이된다 .,,,

# 10926번
ID = ['joonas', 'baekjoon']  # dic으로 해야할지 list로 해야할지
A = input()
for i in range(len(ID)):
    if A == ID[i]:
        print(A + "??!")
# 답
print(input() + "??!")

# 18108번
S = int(input())
if S == 2541:
    print(1998)
# 답
Number = int(input())
result = Number - 543
print(result)

# 10430문제
A, B, C = map(int, input().split())

print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)

# 2588번
A = int(input())  # 첫번째 입력은 숫자로 변환
B = input()  # 두번째 입력은 문자로

# 문자열 인덱스 써서 풀기
print(A * int(B[2]))
print(A * int(B[1]))
print(A * int(B[0]))
print(A * int(B))

# 답
A = int(input())  # 첫번째 입력받은 문자 : 숫자로 변환
B = input()       # 두번째 입력받은 문자 : 문자열 그대로 둠

# 문자열의 인덱스를 이용해서 두번째 입력 받은 문자를 하나씩 숫자로 반환하고 A와 곱한다.
AxB2 = A * int(B[2])
AxB1 = A * int(B[1])
AxB0 = A * int(B[0])
AxB = A * int(B)

print(AxB2, AxB1, AxB0, AxB, sep='\n')
# sep='\n'로 줄바꿈

# 25083번 새싹 ^ ^
print("         ,r\'\"7")
print("r`-_   ,',/")
print(" \. \". L_r\'")
print("   `~\/")
print("      |")
print("      |")

print("         ,r\'\"7")
print("r`-_   ,\'  ,/")
print(" \\. \". L_r\'")
print("   `~\\/")
print("      |")
print("      |")

# ' 또는 " 출력 하기 위해서는 \ <- 백슬래시 앞에 1개써줘야함 유의

# 10172
print("|\_/|")
print("|q p|   /}")
print('( 0 )"""\\')  # 마지막 ' 앞에 백슬하나 더써줌 백슬이랑 따옴표랑 붙여사용하면 문자열만드는걸로 인식 x
print('|"^"`    |')
print('||_/=\\\__|')  # 백슬 연속으로 \\ 두개출력하면 \ 나오는 성질 때매 백슬하나더 추가함

# 1330 문제
A, B = map(int, input().split())
if A > B:
    print('>')
elif A < B:
    print('<')
elif A == B:
    print('==')

# 삼항 연산자
A, B = map(int, input().split())

print('>') if A > B else print('<') if A < B else print('==')

# 9498번

A = int(input())
if 90 <= A <= 100:
    print('A')
elif 80 <= A <= 89:
    print('B')
elif 70 <= A <= 79:
    print('C')
elif 60 <= A <= 69:
    print('D')
else:
    print('F')


# 2753 번
A = int(input())
if A % 400 == 0:
    print(1)
elif A % 4 == 0 and A % 100 != 0:
    print(1)
else:
    print(0)
####  ## ######

year = int(input())

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print('1')
else:
    print('0')

# 14681
x = int(input())
y = int(input())
if 0 <= x and 0 <= y:
    print(1)
elif x < 0 and 0 <= y:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)

# 2884
H, M = map(int, input().split())
if M < 45:
    if M == 0:
        H = 23
        M += 60
    else:
        H -= 1
        M += 60

print(H, M - 45)

# 2525번
# 내꺼 틀린답
H, M = map(int, input().split())
R = int(input())
Plus = 0

if M + R < 60:
    M += R
    print(H, M)

elif H < 23 and M + R >= 60:
    Plus = (M + R) // 60
    M = M + R % 60
    H = H + Plus
    print(H, M - 60)

elif H == 23 and M + R >= 60:
    H = 0
    M += R
    print(H, M - 60)

########################
A, B = map(int, input().split())
C = int(input())

B += C

while True:
    if B >= 60:
        A += 1
        B -= 60
    else:
        break
if A >= 24:
    A -= 24

print(A, B)
###################
A, B = map(int, input().split())
C = int(input())

A = A + C // 60  # 몫
B = B + C % 60  # 나머지

if B >= 60:
    A += 1
    B -= 60
if A >= 24:
    A -= 24

print('%d %d' % (A, B))

# c를 받아 시와 분에 각각 더해줌
