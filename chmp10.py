import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares

# Визначаємо функцію
def func(x):
    return np.sin(2 * x) + x

# Генеруємо значення x та y для заданого проміжку та кроку
x = np.arange(0.1, 1.1, 0.1)
y = func(x)

# Лінійне наближення (пряма)
def linear_residuals(a, x, y):
    return a[0] + a[1] * x - y

# Початкові значення для коефіцієнтів
initial_guess_linear = np.array([1, 1])
res_linear = least_squares(linear_residuals, x0=initial_guess_linear, args=(x, y))
a0, a1 = res_linear.x
print("Лінійне наближення: a0 = %.2f, a1 = %.2f" % (a0, a1))

# Функція для обчислення лінійного наближення
f_linear = lambda x: a0 + a1 * x

# Квадратичне наближення (парабола)
def quadratic_residuals(a, x, y):
    return a[0] + a[1] * x + a[2] * x**2 - y

# Початкові значення для коефіцієнтів
initial_guess_quadratic = np.array([1, 1, 1])
res_quadratic = least_squares(quadratic_residuals, x0=initial_guess_quadratic, args=(x, y))
a0, a1, a2 = res_quadratic.x
print("Квадратичне наближення: a0 = %.2f, a1 = %.2f, a2 = %.2f" % (a0, a1, a2))

# Функція для обчислення квадратичного наближення
f_quadratic = lambda x: a0 + a1 * x + a2 * x**2

# Побудова графіків
x_plot = np.linspace(0.1, 1, 100)
y_plot = func(x_plot)
y_linear = f_linear(x_plot)
y_quadratic = f_quadratic(x_plot)

plt.plot(x, y, 'o', label='Точки функції')
plt.plot(x_plot, y_plot, label='f(x) = sin(2x) + x', color='black')
plt.plot(x_plot, y_linear, label='Наближення прямою', color='blue')
plt.plot(x_plot, y_quadratic, label='Наближення параболою', color='red')
plt.title("Метод найменших квадратів")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
