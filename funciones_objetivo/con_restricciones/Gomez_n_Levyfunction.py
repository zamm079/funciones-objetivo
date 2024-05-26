import numpy as np
import matplotlib.pyplot as plt

def GomezLevy_function(x,y):
    r = 4*x**2 - 2.1*x**4 + 1/3*x**6 + x*y - 4*y**2 + 4*y**4
    return r 

def restriccion(x,y):
    r = -np.sin(4*np.pi*x) + 2*np.sin(2*np.pi*y) <= 1.5
    return r

x = np.linspace(-1, 0.75, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)

# Calcular los valores de la función de Rosenbrock
Z = GomezLevy_function(X, Y)

plt.figure(figsize=(8,6))
contour_filled = plt.contourf(X, Y, Z, levels=50, cmap='viridis', alpha=0.75)
plt.colorbar(contour_filled, label='Valores de Z')
contours = plt.contour(X, Y, Z, levels=10, colors='white', linewidths=0.5)
plt.plot(x,restriccion(x,y),'r-')
plt.clabel(contours, inline=True, fontsize=8)
plt.show()