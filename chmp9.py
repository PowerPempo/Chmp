import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Задаем символьную переменную x и функцию f(x)
x = sp.symbols('x')
f = sp.sin(2 * x) + x

# Находим первые три производные
f1 = sp.diff(f, x)  # первая производная
f2 = sp.diff(f1, x)  # вторая производная
f3 = sp.diff(f2, x)  # третья производная

# Значения функции и производных в точке x = 0
x0 = 0
f_x0 = f.subs(x, x0).evalf()
f1_x0 = f1.subs(x, x0).evalf()
f2_x0 = f2.subs(x, x0).evalf()
f3_x0 = f3.subs(x, x0).evalf()

# Строим многочлены Тейлора второго и четвертого порядков
T2 = f_x0 + f1_x0 * (x - x0) + (f2_x0 / 2) * (x - x0)**2
T4 = T2 + (f3_x0 / 6) * (x - x0)**3  # Добавим третью производную

# Вывод значений производных и многочленов Тейлора
f_x0, f1, f1_x0, f2, f2_x0, f3, f3_x0, T2, T4
