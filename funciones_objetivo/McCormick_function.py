import numpy as np
import matplotlib.pyplot as plt

def McCormick_function(x,y):
    r = np.sin(x + y) + (x - y)**2 - 1.5*x + 2.5*y + 1
    return r

x = np.linspace(-1.5, 4, 100)
y = np.linspace(-3, 4, 100)
X, Y = np.meshgrid(x, y)
Z = McCormick_function(X, Y)

plt.figure(figsize=(8,6))
contour_filled = plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar(contour_filled, label='Valores de Z')
contour_lines = plt.contour(X, Y, Z, levels=50, colors='white', linewidths=0.5)
plt.title('Contorno de la función McCormick', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.xlim([-1.5, 4])
plt.ylim([-3, 4])
plt.show()