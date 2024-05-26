import numpy as np
import matplotlib.pyplot as plt

# Definición de los parámetros de la función Shekel
m = 5
n = 4
a = np.array([
    [4.0, 1.0, 8.0, 6.0],
    [4.0, 1.0, 8.0, 6.0],
    [4.0, 1.0, 8.0, 6.0],
    [4.0, 1.0, 8.0, 6.0],
    [4.0, 1.0, 8.0, 6.0],
    [4.0, 1.0, 8.0, 6.0],
    [4.0, 1.0, 8.0, 6.0],
    [4.0, 1.0, 8.0, 6.0],
    [4.0, 1.0, 8.0, 6.0],
    [4.0, 1.0, 8.0, 6.0],
]).T

c = np.array([0.1, 0.2, 0.2, 0.4, 0.4])

# Definición de la función Shekel
def shekel_function(X, a, c):
    sum_terms = np.zeros(X.shape[0])
    for i in range(m):
        sum_terms += 1.0 / (np.sum((X - a[:, i])**2, axis=1) + c[i])
    return -sum_terms

# Crear una malla de puntos en el espacio de dos dimensiones
x = np.linspace(0, 10, 400)
y = np.linspace(0, 10, 400)
X, Y = np.meshgrid(x, y)

# Expandir la malla para tener una entrada de 4 dimensiones
XY = np.stack([X.ravel(), Y.ravel(), np.zeros_like(X).ravel(), np.zeros_like(X).ravel()], axis=1)

# Calcular los valores de la función para cada punto en la malla
Z = shekel_function(XY, a, c).reshape(X.shape)

# Configurar el gráfico
plt.figure(figsize=(10, 8))

# Graficar los contornos rellenados
contour_filled = plt.contourf(X, Y, Z, levels=200, cmap='viridis')
plt.colorbar(contour_filled, label='Valores de Z')

# Graficar las líneas de contorno sin etiquetas
contour_lines = plt.contour(X, Y, Z, levels=200, colors='black', linewidths=0.5)

# Ajustar etiquetas y título del gráfico
plt.title('Contorno de la función Shekel 5 con detalles', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)

# Ajustar el rango de los ejes
plt.xlim([0, 10])
plt.ylim([0, 10])

# Mostrar la gráfica
plt.show()
