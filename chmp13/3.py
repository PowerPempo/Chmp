from scipy.integrate import solve_ivp 
import matplotlib.pyplot as plt 
import numpy as np 
# Функція, що повертає dy/dx 
def model(x, y): 
    return x + np.sin(y / np.sqrt(0.7)) 
 
# Початкова умова 
y0 = [1.4] 
 
# Коректний діапазон значень x 
x = np.linspace(1.2, 2.2, 11)  # Точне включення кінцевих значень 
 
# Розв'язання ODE 
sol = solve_ivp(model, [1.2, 2.2], y0, t_eval=x) 
 
# Виведення результатів 
print('x=', sol.t) 
print('y=', sol.y[0]) 
 
# Побудова графіка результатів 
plt.plot(sol.t, sol.y[0], marker='o') 
plt.xlabel('x') 
plt.ylabel('y(x)') 
plt.title('Перевірка методом solve_ivp ') 
plt.grid() 
plt.show() 