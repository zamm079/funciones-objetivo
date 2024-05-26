import numpy as np
import matplotlib.pyplot as plt

def bukin_functionN6(x,y):
    r = 100 * np.sqrt(np.abs(y - 0.01*x**2)) + 0.01 * np.abs(x + 10)
    return r

x = np.linspace(-15,-5,100)
y = np.linspace(-3,3,100)
X,Y = np.meshgrid(x,y)
Z = bukin_functionN6(X,Y)
print(Z)


plt.figure(figsize=(10, 8))
contour_filled = plt.contourf(X, Y, Z, levels=np.linspace(np.min(Z), np.max(Z), 50), cmap='viridis')
plt.colorbar(contour_filled, label='Valores de Z')
contour_lines = plt.contour(X, Y, Z, levels=np.linspace(np.min(Z), np.max(Z), 50), colors='white', linewidths=0.5)

plt.title('función Bukin N.6', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)

plt.xlim([-15, -5])
plt.ylim([-3, 3])
plt.show()