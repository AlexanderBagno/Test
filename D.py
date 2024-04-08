S = input()
Q = int(input())

s = list()
for symbol in list(S):
    sym = ord(symbol)
    if sym < 91:
        sym -= 26
    s.append(sym)

for idx in range(Q):
    l, r, x = map(int, input().split(' '))
    x = x % 52
    for j in range(l - 1, r):
        print(l - 1, r, j, x, s)
        if 96 < s[j] < 123:
            if x % 2 == 0:
                print('1', s[j])
                s[j] += x // 2
                print('1', s[j])
            else:
                print('2', s[j])
                s[j] -= 58 + x // 2
                print('2', s[j])
            if 54 < s[j] < 97 or s[j] > 122:
                print('3', s[j])
                s[j] -= 25
                print('3', s[j])
        else:
            if x % 2 == 0:
                print('4', s[j])
                s[j] += x // 2
                print('4', s[j])
            else:
                print('5', s[j])
                s[j] += 59 + x // 2
                print('5', s[j])
            if 54 < s[j] < 97 or s[j] > 122:
                print('6', s[j])
                s[j] -= 26
                print('6', s[j])

    answer = list()
    for symbol in s:
        if symbol < 91:
            symbol += 26
        answer.append(chr(symbol))

    print(''.join(answer))