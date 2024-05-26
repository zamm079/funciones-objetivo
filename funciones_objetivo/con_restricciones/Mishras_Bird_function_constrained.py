import numpy as np
import matplotlib.pyplot as plt

def Mishras_Bird_function_constrained(x,y):
    r = np.sin(y) * np.exp((1 - np.cos(x))**2) + np.cos(x) * np.exp((1 - np.sin(y))**2) + (x - y)**2
    return r

x = np.linspace(-10, 0, 400)
y = np.linspace(-6.5, 0, 400)
X, Y = np.meshgrid(x, y)
Z = Mishras_Bird_function_constrained(X, Y)


def restriccion(X,Y):
    mask = (X + 5)**2 + (Y + 5)**2 <= Y
    return mask


plt.figure(figsize=(10, 8))
contour_filled = plt.contourf(X, Y, Z, levels=50, cmap='viridis', alpha=0.75)
plt.colorbar(contour_filled, label='Valores de Z')
plt.contourf(X, Y, restriccion(X,Y), levels=[0, 0.5], colors='gray', alpha=0.3)
plt.title('Función Mishra\'s Bird con Restricciones', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.xlim([-10, 0])
plt.ylim([-6.5, 0])
plt.show()