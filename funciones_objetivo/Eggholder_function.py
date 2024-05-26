import numpy as np
import matplotlib.pyplot as plt

def Eggholder_function(X,Y):
    term1 = -(Y + 47) * np.sin(np.sqrt(np.abs(X/2 + (Y + 47))))
    term2 = -X * np.sin(np.sqrt(np.abs(X - (Y + 47))))
    return term1 + term2


x = np.linspace(-512, 512, 100)
y = np.linspace(-512, 512, 100)
X, Y = np.meshgrid(x, y)
Z = Eggholder_function(X, Y)

plt.figure(figsize=(10, 8))
contour_filled = plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar(contour_filled, label='Valores de Z')
# contour_lines = plt.contour(X, Y, Z, levels=50, colors='white', linewidths=0.5)
plt.title('Contorno de la función Eggholder', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.xlim([-512, 512])
plt.ylim([-512, 512])
plt.show()