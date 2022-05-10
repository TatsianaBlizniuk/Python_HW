# Задание 2
# 7. Составить алгоритм решения ребуса КОТ + КОТ = ТОК (различные буквы означают различные цифры, старшая буква ‒ не 0).

import numpy
for k in range(1, 10):
    for o in range(0, 10):
        for t in range(1, 10):
            a = (100*k) + (10*o) + t
            b = (100*t) + (10*o) + k
            if a + a == b:
                print(k, o, t)
            else:
                print("Решение неверное при " + "k=" + str(k) + " o=" + str(o) + " t=" + str(t))