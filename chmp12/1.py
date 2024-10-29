from scipy import integrate  
import numpy as np

# Задаем функцию, которую необходимо интегрировать
def f1(x):  
    return 1 / np.sqrt(0.5 * x + 1.5)

# Метод левых прямоугольников
def left_rectangle(f, a, b, n):  
    h = (b - a) / n  
    result = sum(f(a + i * h) for i in range(n)) * h
    return result

# Метод правых прямоугольников
def right_rectangle(f, a, b, n):  
    h = (b - a) / n  
    result = sum(f(a + i * h) for i in range(1, n + 1)) * h
    return result

# Метод средних прямоугольников
def mid_rectangle(f, a, b, n):  
    h = (b - a) / n  
    result = sum(f(a + (i + 0.5) * h) for i in range(n)) * h
    return result

# Параметры интеграла
a = 1.2
b = 2
n = 10

# Вычисления
left_result = left_rectangle(f1, a, b, n)
right_result = right_rectangle(f1, a, b, n)
mid_result = mid_rectangle(f1, a, b, n)

# Проверка точного значения интеграла для сравнения
exact_value, _ = integrate.quad(f1, a, b)

print("Метод левых прямоугольников:", round(left_result, 5))
print("Метод правых прямоугольников:", round(right_result, 5))
print("Метод средних прямоугольников:", round(mid_result, 5))
print("Точное значение интеграла:", round(exact_value, 5))
