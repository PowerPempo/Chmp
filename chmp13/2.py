import numpy as np 
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 
 
def model(y, x): 
    return x + np.sin(y / np.sqrt(0.7)) 
 
y0 = 1.4 
x = np.arange(1.2, 2.3, 0.1) 
 
y = odeint(model, y0, x) 
 
print('x=', x) 
print('y=', y.flatten()) 
 
plt.plot(x, y, marker='o') 
plt.xlabel('x') 
plt.ylabel('y(x)') 
plt.title('Перевірка методом odeint') 
plt.grid() 
plt.show()