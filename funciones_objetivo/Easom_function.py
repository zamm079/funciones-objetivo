import numpy as np
import matplotlib.pyplot as plt

def Easom_function(x,y):
    r = -np.cos(x)*np.cos(y)*np.exp(-((x-np.pi)**2 + (y-np.pi)**2))
    return r



x = np.linspace(-100, 100, 100)
y = np.linspace(-100, 100, 100)
X, Y = np.meshgrid(x, y)
Z = Easom_function(X, Y)


plt.figure(figsize=(8, 6))
contour_filled = plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar(contour_filled, label='Valores de Z')
contour_lines = plt.contour(X, Y, Z, levels=50, colors='white', linewidths=0.5)
plt.title('Contorno de la función Easom', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.xlim([-10, 10])
plt.ylim([-10, 10])
plt.show()