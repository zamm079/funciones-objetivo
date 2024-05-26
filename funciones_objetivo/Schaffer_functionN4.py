import numpy as np
import matplotlib.pyplot as plt

def Schaffer_functionN4(x,y):
    numerator = np.cos(np.sin(np.abs(X**2 - Y**2)))**2 - 0.5
    denominator = (1 + 0.001 * (X**2 + Y**2))**2
    return 0.5 + numerator / denominator


x = np.linspace(-100, 100, 100)
y = np.linspace(-100, 100, 100)
X, Y = np.meshgrid(x, y)
Z = Schaffer_functionN4(X, Y)
print(Z)

plt.figure(figsize=(8,6))
contour_filled = plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar(contour_filled, label='Valores de Z')
contour_lines = plt.contour(X, Y, Z, levels=50, colors='white', linewidths=0.5)
plt.title('función Schaffer N.4', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.xlim([-100, 100])
plt.ylim([-100, 100])
plt.show()