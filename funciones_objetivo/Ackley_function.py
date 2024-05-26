import numpy as np
import matplotlib.pyplot as plt


def ackley_function(x, y):
    term1 = -20 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2)))-np.exp(0.5 * (np.cos(2*np.pi * x) + np.cos(2*np.pi * y)))+ 20 + np.exp(1)
    return term1

# Genera datos para trazar
x = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)
X,Y = np.meshgrid(x,y)
Z = ackley_function(X, Y)
print(Z)

plt.figure(figsize=(8, 6))
plt.contourf(X, Y, Z, levels=100, cmap='viridis')
plt.contour(X, Y, Z, colors='white')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Contour Plot of Ackley Function')
plt.colorbar(label='Z')
plt.show()