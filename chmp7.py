import numpy as np
import matplotlib.pyplot as plt

# Данные из таблицы
x_data = np.array([0.01, 0.06, 0.11, 0.16, 0.21, 0.26, 0.31, 0.36, 0.41, 0.46, 0.51])
y_data = np.array([0.9918, 0.9519, 0.9136, 0.8769, 0.8416, 0.8077, 0.7753, 0.7441, 0.7141, 0.6854, 0.6579])

# Точки для интерполяции
interpolation_points = np.array([0.027, 0.124, 0.035, 0.416, 0.432, 0.5])

# Функция для первой интерполяционной формулы Ньютона
def newton_interpolation(x, y, x0):
    n = len(x)
    f = np.zeros((n, n))
    f[:, 0] = y  # Заполнение первого столбца значениями y
    for j in range(1, n):  # Построение таблицы конечных разностей
        for i in range(n - j):
            f[i][j] = (f[i+1][j-1] - f[i][j-1]) / (x[i+j] - x[i])
    
    # Вычисление значения функции в точке x0
    result = f[0, 0]
    product = 1.0
    for j in range(1, n):
        product *= (x0 - x[j-1])
        result += f[0, j] * product
    return result

# Вычисляем значения функции в заданных точках
results = {x0: newton_interpolation(x_data, y_data, x0) for x0 in interpolation_points}
print(results)
