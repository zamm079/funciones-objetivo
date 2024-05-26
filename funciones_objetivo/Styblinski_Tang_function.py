import numpy as np
import matplotlib.pyplot as plt

def StyblinskiTang_function(X):
    r = np.sum(X**4 - 16*X**2 + 5*X,axis=0 )
    return r

x = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)
X,Y = np.meshgrid(x,y)
z = np.array([X,Y])
Z=StyblinskiTang_function(z)
print(Z)


plt.figure(figsize=(10, 8))
contour_filled = plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar(contour_filled, label='Valores de Z')
contour_lines = plt.contour(X, Y, Z, levels=50, colors='white', linewidths=0.5)
plt.title('Contorno de la función Styblinski–Tang', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.xlim([-5, 5])
plt.ylim([-5, 5])
plt.show()