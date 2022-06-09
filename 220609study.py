# 2525
A, B = map(int, input().split())
C = int(input())

A += C // 60
B += C % 60

if B >= 60:
    A += 1
    B -= 60
if A >= 24:
    A -= 24

print(A, B)


# 2480

A, B, C = map(int, input().split())

if A == B == C:
    print(10000 + A * 1000)

elif A == B or B == C:
    print(1000 + B * 100)
elif A == C:
    print(1000 + A * 100)

else:
    print(max(A, B, C) * 100)


# 2739번

N = int(input())

if 1 <= N <= 9:
    for i in range(N, N+1):
        for j in range(1, 10):
            print(f'{i} * {j} = {i * j}')
# SO easy

# 다른사람코드
n = int(input())

for i in range(1, 10):  # 1~9
    print(n, '*', i, '=', n*i)

# 10950
T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(A + B)

# 8393
n = int(input())
result = 0

for i in range(1, n+1):
    result += i
print(result)
