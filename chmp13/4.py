import numpy as np 
import matplotlib.pyplot as plt 
 
def f(x, y): 
    return x + np.sin(y / np.sqrt(11)) 
 
a, b, h, y0 = 0.6, 1.6, 0.1, 1.2 
n = int((b - a) / h) 
 
x = np.arange(a, b + h, h) 
y = np.empty(n + 1) 
y[0] = y0 
 
for i in range(n): 
    y_pred = y[i] + f(x[i], y[i]) * h 
    y[i + 1] = y[i] + (f(x[i], y[i]) + f(x[i + 1], y_pred)) * h / 2 
 
y_rounded = np.round_(y, 4) 
print("x =", x, "\ny =", y_rounded) 
plt.plot(x, y, "o", x, y, "red") 
plt.xlabel("x") 
plt.ylabel("y") 
plt.title("Метод Ейлера-Коші") 
plt.grid() 
plt.show()