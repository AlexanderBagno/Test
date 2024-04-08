import numpy as np
import matplotlib.pyplot as plt

n = 3  # Количество членов ряда Тейлора
a = 1  # Константа из функции принадлежности
b = 1  # Константа из функции принадлежности
m = 2  # Количество членов ряда Фурье
l = 2  # Длина интервала разложения в ряд Фурье
minimum = -l / 2
step = l / 200
maximum = l / 2

# Приближение функции принадлежности рядом Тейлора
fact = 1
c = np.zeros(n)
p = min(33, n)
for k in range(p):
    summa = 0
    if k > 0:
        fact = fact * k
    for i in range(k + 1):
        summa = summa + fact / np.math.factorial(k - i) * (a * b) ** (k - i)
    factor = (-1) ** k / b ** (k + 1) / fact
    c[k] = factor * summa
for k in range(33, n):
    c[k] = (-1) ** k * np.exp(1)
print(c)

# Разложение ряда Тейлора в ряд Фурье
d = np.zeros((m, n))
e = np.zeros(m + 1)

summa = 0
for k in range(n):
    summa = summa + c[k] * (l / 2) ** (2 * k + 1) / (2 * k + 1)
e[0] = 2 / l * summa

fact = [1]
for k in range(n):
    fact.append(fact[k] * 2 * (k + 1) * (2 * k + 1))

for j in range(m):
    for k in range(n):
        summa = 0
        # print(k, end = ':\n')
        for i in range(k):
            # print(f's={summa}, e={(-1) ** i * (l/(2*np.math.pi*(j + 1))) ** (2*i + 2)}, f={fact/np.math.factorial(2*k - 1 - 2*i)}, g={(l/2) ** (2*k - 1 - 2*i) * (-1) ** j}')
            # summa = summa + (-1) ** i * (l / (2 * np.math.pi * (j + 1))) ** (2 * i + 2) * fact[i] / np.math.factorial(2 * k - 1 - 2 * i) * (l / 2) ** (2 * k - 1 - 2 * i) * (-1) ** j
            summa = summa + (-1) ** i * (l / (2 * np.math.pi * (j + 1))) ** (2 * i + 2) * fact[i] / np.math.factorial(2 * k - 1 - 2 * i) * (l / 2) ** (2 * k - 1 - 2 * i) * (-1) ** (j + 1)
        # print('')
        d[j, k] = d[j, k] + 4 * c[k] / l * summa
e[1] = e[1] + sum(d[0])
print(d)
print(e)

# Построение графиков
T = np.zeros(int((maximum - minimum) / step))
mu = np.zeros(int((maximum - minimum) / step))
F = np.zeros((m + 1, int((maximum - minimum) / step)))
F = F + e[0]
X = np.arange(minimum, maximum, step)
i = 0
for x in X:
    mu[i] = np.exp(-a * x ** 2) / (1 + b * x ** 2)
    for k in range(n):
        T[i] = T[i] + x ** (2 * k) * c[k]
    for j in range(1, m):
        for k in range(n):
            F[j, i] = F[j, i] + np.math.cos(2 * np.math.pi * (j + 1) / l * x) * e[j + 1]
    i = i + 1

plt.plot(X, mu, 'b')
plt.plot(X, T, 'c')
plt.plot(X, F[0], 'y')
if m > 0: plt.plot(X, F[1], 'r')
plt.show()
