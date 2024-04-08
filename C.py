def components_find(matrix_x, matrix_y):
    components_x = 0
    components_y = 0

    for i in range(len(matrix_x) - 1):
        if matrix_x[i] == 0 and matrix_x[i + 1] == 1:
            components_x += 1
    if matrix_x[len(matrix_x) - 1] == 0:
        components_x += 1

    for i in range(len(matrix_y) - 1):
        if matrix_y[i] == 0 and matrix_y[i + 1] == 1:
            components_y += 1
    if matrix_y[len(matrix_y) - 1] == 0:
        components_y += 1

    return components_x * components_y


N, M = map(int, input().split(' '))
matrix_x = [0] * N
matrix_y = [0] * N
positions = list()
counter = 0
components_list = []

for index in range(M):
    symbol, X, Y = input().split(' ')
    x = int(X) - 1
    y = int(Y) - 1
    if symbol == '+':
        matrix_x[x] = 1
        matrix_y[y] = 1
        positions.append((x, y))
        components_list.append(components_find(matrix_x, matrix_y))

    else:
        positions.remove((x, y))
        if all(x != t[0] for t in positions):
            matrix_x[x] = 0
        if all(y != t[1] for t in positions):
            matrix_y[y] = 0
        components_list.append(components_find(matrix_x, matrix_y))

for element in components_list:
    print(element)
