import numpy as np
import matplotlib.pyplot as plt

def Schaffer_functionN2(x,y):
    term1 = np.sin(x**2 - y**2)**2 - 0.5
    term2 = (1 + 0.001 * (x**2 + y**2))**2
    r = 0.5 + term1 / term2
    return r

x = np.linspace(-100, 100, 100)
y = np.linspace(-100, 100, 100)
X, Y = np.meshgrid(x, y)


Z = Schaffer_functionN2(X, Y)
plt.figure(figsize=(10, 8))
contour_filled = plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar(contour_filled, label='Valores de Z')
contour_lines = plt.contour(X, Y, Z, levels=50, colors='white', linewidths=0.5)
plt.title('Contorno de la función Schaffer N.2', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.xlim([-100, 100])
plt.ylim([-100, 100])
plt.show()