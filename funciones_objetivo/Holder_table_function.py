import numpy as np
import matplotlib.pyplot as plt

def Holder_table_function(x,y):
    term1 = -np.abs(np.sin(x)*np.cos(y))
    term2 = np.exp(np.abs(1 - np.sqrt(x**2 + y**2)/np.pi))
    r = term1*term2
    return r


x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)
Z = Holder_table_function(X, Y)


plt.figure(figsize=(8, 6))
contour_filled = plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar(contour_filled, label='Valores de Z')
contour_lines = plt.contour(X, Y, Z, levels=50, colors='white', linewidths=0.5)

plt.title('función Hölder Table', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.xlim([-10, 10])
plt.ylim([-10, 10])
plt.show()