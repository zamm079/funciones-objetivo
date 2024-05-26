import numpy as np
import matplotlib.pyplot as plt

def Crossintray_function(x,y):
    term1 = np.sin(x) * np.sin(y)
    term2 = np.exp(np.abs(100 - np.sqrt(x**2 + y**2) / np.pi))
    r = -0.0001 * (np.abs(term1 * term2) + 1)**0.1
    return r

x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)


Z = Crossintray_function(X, Y)
plt.figure(figsize=(10, 8))
contour_filled = plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar(contour_filled, label='Valores de Z')
# contour_lines = plt.contour(X, Y, Z, levels=50, colors='black', linewidths=0.5)
plt.title('función Cross-in-Tray', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.xlim([-10, 10])
plt.ylim([-10, 10])
plt.show()