N, T = map(int, input().split(' '))

A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

a = sum(A)
b = sum(B)

if a <= T <= b:
    print('YES')
else:
    print('NO')
