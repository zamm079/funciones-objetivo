import numpy as np
import matplotlib.pyplot as plt

def matyas_function(x,y):
    r = 0.26 * (x**2 + y**2) - 0.48*x*y
    return r

x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)
X,Y = np.meshgrid(x,y)
Z = matyas_function(X,Y)
print(Z)


plt.figure(figsize=(8, 6))
contour_filled = plt.contourf(X, Y, Z, levels=np.linspace(np.min(Z), np.max(Z), 50), cmap='viridis')
plt.colorbar(contour_filled, label='Z')
contour_lines = plt.contour(X, Y, Z, levels=np.linspace(np.min(Z), np.max(Z), 50), colors='black', linewidths=0.5)


plt.title('función Matyas', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)

# Ajustar el rango de los ejes
plt.xlim([-10, 10])
plt.ylim([-10, 10])

# Mostrar la gráfica
plt.show()