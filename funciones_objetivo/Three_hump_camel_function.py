import numpy as np
import matplotlib.pyplot as plt

def Three_hump_camel_function(X,Y):
    r  = 2*X**2 - 1.05*X**4 + (X**6)/6 + X*Y + Y**2
    return r



x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = Three_hump_camel_function(X, Y)


plt.figure(figsize=(10, 8))
contour_filled = plt.contourf(X, Y, Z, levels=np.linspace(np.min(Z), np.max(Z), 50), cmap='viridis')
plt.colorbar(contour_filled, label='Z')
contour_lines = plt.contour(X, Y, Z, levels=np.linspace(np.min(Z), np.max(Z), 50), colors='white', linewidths=0.5)
plt.title('función Three-Hump Camel', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.show()
