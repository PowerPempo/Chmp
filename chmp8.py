import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Задані точки
x = np.array([0.8, 0.9, 1.2, 1.6, 2.1])
y = np.array([1.42, 2.34, 3.48, 1.77, 2.66])

# Створення кубічного сплайну
cs = CubicSpline(x, y)

# Обчислення значень сплайну у вузлових точках для перевірки
y_spline = cs(x)

print("Перевірка значень у вузлових точках:")
for i in range(len(x)):
    print(f"x = {x[i]}, y (вихідне) = {y[i]}, y (сплайн) = {y_spline[i]:.4f}")

# Генерація нових точок для побудови гладкого графіку
x_new = np.linspace(np.min(x), np.max(x), 100)
y_new = cs(x_new)

# Побудова графіку
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o', label='Вихідні точки')
plt.plot(x_new, y_new, label='Кубічний сплайн')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Кубічний сплайн')
plt.legend()
plt.grid(True)
plt.show()
