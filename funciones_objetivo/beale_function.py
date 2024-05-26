import numpy as np
import matplotlib.pyplot as plt

def beale_function(x,y):
    r = (1.5 - x + x*y)**2 + (2.25 - x + x*y**2)**2 + (2.625 - x + x*y**3)**2
    return r

x = np.linspace(-4.5,4.5,100)
y = np.linspace(-4.5,4.5,100)
X,Y = np.meshgrid(x,y)
Z = beale_function(X,Y)
print(Z)


contour_filled = plt.contourf(X, Y, Z, levels=50, cmap='viridis')
contour_lines = plt.contour(X, Y, Z, levels=np.linspace(-4.5, 4.5, 100), colors='white', linewidths=0.5)
plt.colorbar(contour_filled, label='Valores de Z')


plt.title('función beale')
plt.xlabel('x')
plt.ylabel('y')
plt.show()