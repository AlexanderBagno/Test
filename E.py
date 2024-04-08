N = int(input())

barriers = []
for i in range(N):
    x, y = map(int, input().split(' '))
    barriers.append([x, y])

Q = int(input())
position = [0, 0]
message = ''

for T in range(Q):
    dir, k = input().split(' ')
    K = int(k)

    if dir == 'U':
        for i in range(K):
            position[1] += 1
            if position in barriers and message == '':
                message = f'Stop {T + 1}'
                break
    elif dir == 'D':
        for i in range(K):
            position[1] -= 1
            if position in barriers and message == '':
                message = f'Stop {T + 1}'
                break
    elif dir == 'R':
        for i in range(K):
            position[0] += 1
            if position in barriers and message == '':
                message = f'Stop {T + 1}'
                break
    else:
        for i in range(K):
            position[0] -= 1
            if position in barriers and message == '':
                message = f'Stop {T + 1}'
                break

if message == '':
    message = 'Complete'

print(message)
