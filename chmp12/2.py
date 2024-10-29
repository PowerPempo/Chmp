from scipy import integrate  
import numpy as np

# Задаем функцию, которую необходимо интегрировать
def f2(x):
    return np.log10(x**2 + 3) / (2 * x)

# Метод Симпсона
def simpson_rule(f, a, b, n):  
    h = (b - a) / n  
    result = f(a) + f(b)  
    for i in range(1, n):
        x = a + i * h
        result += 4 * f(x) if i % 2 != 0 else 2 * f(x)
    result *= h / 3
    return result

# Параметры интеграла
a = 1.2
b = 2
n = 8

# Вычисления
simpson_result = simpson_rule(f2, a, b, n)

# Проверка точного значения интеграла для сравнения
exact_value, _ = integrate.quad(f2, a, b)

print("Метод Симпсона:", round(simpson_result, 5))
print("Точное значение интеграла:", round(exact_value, 5))
