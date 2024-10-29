import numpy as np 
import matplotlib.pyplot as plt 
def f(x, y): 
    return x + np.sin(y / np.sqrt(0.7)) 
# Вводимо параметри (ліва, права межі відрізку, крок, початкова умова) 
a, b, h, y0 = 1.2, 2.2, 0.1, 1.4 
 
n = int((b - a) / h)  
x = np.array([a + i * h for i in range(n + 1)]) 
y = np.empty(n + 1) 
y[0] = y0 
 
for i in range(n): 
    y[i + 1] = y[i] + f(x[i], y[i]) * h 
 
y_rounded = np.round_(y, 4) 
print("x =", x, "\ny =", y_rounded) 
 
plt.plot(x, y, "o", x, y, "red") 
plt.xlabel("x") 
plt.ylabel("y") 
plt.title("Метод Ейлера") 
plt.grid() 
plt.show() 