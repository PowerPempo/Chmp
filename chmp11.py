import numpy as np

# Данные из таблицы
x_values_1 = np.array([1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
y_values_1 = np.array([10.517, 10.193, 9.807, 9.387, 8.977, 8.637])

x_values_2 = np.array([4.5, 5.0, 5.5, 6.0, 6.5, 7.0])
y_values_2 = np.array([8.442, 8.482, 8.862, 9.701, 11.132, 13.302])

# Функция для нахождения интерполяционного значения функции
def newton_interpolation(x, x_values, y_values):
    n = len(x_values)
    y = y_values[0]
    div_diff = y_values.copy()
    
    for i in range(1, n):
        for j in range(n - i):
            div_diff[j] = (div_diff[j+1] - div_diff[j]) / (x_values[j+i] - x_values[j])
        y += div_diff[0] * np.prod([x - x_values[j] for j in range(i)])
    return y

# Функция для нахождения первой производной
def first_derivative(x, x_values, y_values, eps=0.0001):
    h = eps
    dy = (newton_interpolation(x + h, x_values, y_values) - newton_interpolation(x - h, x_values, y_values)) / (2 * h)
    return dy

# Функция для нахождения второй производной
def second_derivative(x, x_values, y_values, eps=0.0001):
    h = eps
    ddy = (newton_interpolation(x + h, x_values, y_values) - 2 * newton_interpolation(x, x_values, y_values) + 
           newton_interpolation(x - h, x_values, y_values)) / (h**2)
    return ddy

# Выбор точки для расчета производных
x_point = 2.5

# Нахождение производных для первой таблицы (1.5-4.0)
dy_1 = first_derivative(x_point, x_values_1, y_values_1)
ddy_1 = second_derivative(x_point, x_values_1, y_values_1)

dy_1, ddy_1
