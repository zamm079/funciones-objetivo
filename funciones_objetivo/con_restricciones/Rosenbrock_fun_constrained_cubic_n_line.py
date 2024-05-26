import numpy as np
import matplotlib.pyplot as plt

def rosenbrock(x, y, a=1, b=100):
    return (a - x)**2 + b * (y - x**2)**2

def cubic_constraint(x):
    return x**3

def line_constraint(x):
    return 1.5 - x



# Crear una malla de puntos
x = np.linspace(-2, 2, 400)
y = np.linspace(-1, 3, 400)
X, Y = np.meshgrid(x, y)

# Calcular los valores de la función de Rosenbrock
Z = rosenbrock(X, Y)

# Definir las restricciones
cubic_y = cubic_constraint(x)
line_y = line_constraint(x)

# Configurar el gráfico
plt.figure(figsize=(10, 8))

# Graficar la función de Rosenbrock
contour_filled = plt.contourf(X, Y, Z, levels=50, cmap='viridis', alpha=0.75)
plt.colorbar(contour_filled, label='Valores de Z')

# Graficar las restricciones
plt.plot(x, cubic_y, 'r-', label='$y = x^3$')
plt.plot(x, line_y, 'b-', label='$y = 1.5 - x$')

# Sombrear la región factible
plt.fill_between(x, np.maximum(cubic_y, -1), line_y, where=(cubic_y <= line_y), color='gray', alpha=0.3)

# Ajustar etiquetas y título del gráfico
plt.title('Función de Rosenbrock con Restricciones', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)

# Ajustar el rango de los ejes
plt.xlim([-2, 2])
plt.ylim([-1, 3])

# Mostrar leyenda
plt.legend()

# Mostrar la gráfica
plt.show()
