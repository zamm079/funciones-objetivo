import numpy as np
import matplotlib.pyplot as plt

def goldstein_price_function(x,y):
    part1 = (1 + (x + y + 1)**2 * (19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2))
    part2 = (30 + (2*x - 3*y)**2 * (18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2))
    r = part1 * part2
    return r

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

Z = goldstein_price_function(X, Y)

plt.figure(figsize=(8, 6))


contour_filled = plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar(contour_filled, label='Valores de Z')


contour_lines = plt.contour(X, Y, Z, levels=50, colors='white', linewidths=0.5)

# Ajustar etiquetas y título del gráfico
plt.title('Contorno de la función Goldstein-Price', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.show()