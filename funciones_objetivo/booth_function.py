import numpy as np
import matplotlib.pyplot as plt

def booth_function(X,Y):
    r = (X + 2*Y - 7)**2 + (2*X + Y - 5)**2
    return r

x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)
X,Y = np.meshgrid(x,y)

Z = booth_function(X,Y)
print(Z)

plt.figure(figsize=(10, 8))
contour_filled = plt.contourf(X, Y, Z, levels=np.linspace(np.min(Z), np.max(Z), 50), cmap='viridis')
plt.colorbar(contour_filled, label='Valores de Z')

contour_lines = plt.contour(X, Y, Z, levels=np.linspace(np.min(Z), np.max(Z), 50), colors='white', linewidths=0.5)


plt.title('Contorno de la función booth', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.show()