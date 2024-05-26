import numpy as np
import matplotlib.pyplot as plt


def rosenbrock(x, y):
    return (1 - x)**2 + 100 * (y - x**2)**2


x = np.linspace(-1.5, 1.5, 400)
y = np.linspace(-1.5, 1.5, 400)
X, Y = np.meshgrid(x, y)
Z = rosenbrock(X, Y)


def rest_circunferencia(X,Y):
    mask = X**2 + Y**2 <= 2
    return mask


plt.figure(figsize=(8,6))
contour_filled = plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar(contour_filled, label='Valores de Z')
plt.contourf(X, Y, rest_circunferencia(X,Y), levels=100, colors='white', alpha=0.3)
plt.title('Función Rosenbrock con Restricción de Disco', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.legend()
plt.show()
