import numpy as np
import matplotlib.pyplot as plt

def Levi_functionN13(x,y):
    term1 = np.sin(3 * np.pi * x)**2
    term2 = (x - 1)**2 * (1 + np.sin(3 * np.pi * y)**2)
    term3 = (y - 1)**2 * (1 + np.sin(2 * np.pi * y)**2)
    r = term1 + term2 + term3
    return r


x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = Levi_functionN13(X, Y)


plt.figure(figsize=(8,6))
contour_filled = plt.contourf(X, Y, Z, levels=np.linspace(np.min(Z), np.max(Z), 50), cmap='viridis')
plt.colorbar(contour_filled, label='Z')
# contour_lines = plt.contour(X, Y, Z, levels=np.linspace(np.min(Z), np.max(Z), 50), colors='white', linewidths=0.5)


plt.title('Contorno de la función Lévi N.13', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.xlim([-10, 10])
plt.ylim([-10, 10])
plt.show()