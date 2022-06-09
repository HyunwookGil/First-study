import sys  # sys모듈 읽어들이기

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
# 2741
N = int(input())
for i in range(1, N+1):
    print(i)

# 11021
T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    print("Case #" + str(i) + ":", A + B)

# 11022

T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    print(f'Case #{i}: {A} + {B} = {A + B}')
# 2438

N = int(input())

for i in range(1, N+1):
    print('*' * i)

# 2439
N = int(input())

for i in range(1, N+1):
    print(" " * (N - i) + '*' * i)

# 10871
N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    if A[i] < X:
        print(A[i], end=' ')

# 10952
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        print(a + b)
