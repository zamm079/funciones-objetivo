import numpy as np
import matplotlib.pyplot as plt

def Simionescu_function(x,y):
    r = 0.1 * x * y
    return r

def restriccion(x,y):
    n=8
    rt=1
    rs=0.2
    r = x**2 + y**2 <= (rt + rs * np.cos(n * np.arctan2(x,y)))**2
    return r

x = np.linspace(-1, 0.75, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)

# Calcular los valores de la función de Rosenbrock
Z = Simionescu_function(X, Y)

plt.figure(figsize=(8,6))
contour_filled = plt.contourf(X, Y, Z, levels=50, cmap='viridis', alpha=0.75)
plt.colorbar(contour_filled, label='Valores de Z')
contours = plt.contour(X, Y, Z, levels=10, colors='white', linewidths=0.5)
plt.plot(x,restriccion(x,y),'r-')
plt.clabel(contours, inline=True, fontsize=8)
plt.show()