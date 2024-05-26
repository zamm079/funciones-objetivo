import numpy as np
import matplotlib.pyplot as plt

def Townsend_function(x,y):
    r = -(np.cos((x - 0.1)*y))**2 - x*np.sin(3*x + y)
    return r

def restriccion(x,y):
    t = np.arctan(x,y)
    r = x**2 + y**2 < (2 * np.cos(t) - 1/2 *np.cos(2*t) - 1/4 *np.cos(3*t) - 1/8 *np.cos(4*t))
    return r
# def townsend(x, y):
#     return (2 - 1.05 * x**2 + (x**4) / 6) * x**2 + x * y + y**2



x = np.linspace(-2.25, 2.25, 400)
y = np.linspace(-2.5, 1.75, 400)
X, Y = np.meshgrid(x, y)
Z = Townsend_function(X, Y)

plt.figure(figsize=(8,6))
contour_filled = plt.contourf(X, Y, Z, levels=50, cmap='viridis', alpha=0.75)
plt.colorbar(contour_filled, label='Valores de Z')
contours = plt.contour(X, Y, Z, levels=10, colors='black', linewidths=0.5)
plt.plot(x,restriccion(x,y),'r-')
plt.clabel(contours, inline=True, fontsize=8)
plt.show()

# # Configurar el gráfico
# plt.figure(figsize=(10, 8))

# # Graficar la función Townsend
# contour_filled = plt.contourf(X, Y, Z, levels=50, cmap='viridis', alpha=0.75)
# plt.colorbar(contour_filled, label='Valores de Z')

# # Agregar contornos
# contours = plt.contour(X, Y, Z, levels=10, colors='black', linewidths=0.5)
# plt.clabel(contours, inline=True, fontsize=8)

# # Ajustar etiquetas y título del gráfico
# plt.title('Función Townsend', fontsize=14)
# plt.xlabel('x', fontsize=12)
# plt.ylabel('y', fontsize=12)

# # Ajustar el rango de los ejes
# plt.xlim([-2, 2])
# plt.ylim([-2, 2])

# # Mostrar la gráfica
# plt.show()
