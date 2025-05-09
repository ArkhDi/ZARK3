import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def f(x1, x2):
    return 100 * np.sqrt(np.abs(x2 - 0.01 * x1 ** 2)) + 0.01 * np.abs(x1 + 10)
x1_min, x1_max = -15, -5
x2_min, x2_max = -3, 3

x10, x20 = -10, 1

step = 0.1

x1 = np.arange(x1_min, x1_max, step)
x2 = np.arange(x2_min, x2_max, step)
X1, X2 = np.meshgrid(x1, x2)
Y = f(X1, X2)

y0 = f(x10, x20)

fig = plt.figure(figsize=(14, 10))

#изометрический вид
ax1 = fig.add_subplot(221, projection='3d')
ax1.plot_surface(X1, X2, Y, cmap='viridis')
ax1.set_xlabel('x1')
ax1.set_ylabel('x2')
ax1.set_zlabel('y=f(x1, x2)')
ax1.set_title('Трехмерная поверхность (изометрический вид)')

#вид сверху
ax2 = fig.add_subplot(222, projection='3d')
ax2.plot_surface(X1, X2, Y, cmap='viridis', zorder=0)
ax2.view_init(elev=90, azim=-90)
ax2.set_xlabel('x1')
ax2.set_ylabel('x2')
ax2.set_zlabel('y=f(x1, x2)')
ax2.set_title('Трехмерная поверхность (вид сверху)')

#y = f(x1) при x2 = x20
ax3 = fig.add_subplot(223)
x1_values = np.linspace(x1_min, x1_max, 500)
y_values = f(x1_values, x20)
ax3.plot(x1_values, y_values, label=f'x2 = {x20}')
ax3.scatter([x10], [y0], color='red')
ax3.set_xlabel('x1')
ax3.set_ylabel('y=f(x1)')
ax3.set_title(f'y = f(x1) при x2 = {x20}')
ax3.legend()
ax3.annotate(f'({x10}, {x20})', (x10, y0), textcoords="offset points", xytext=(0,10), ha='center')

#y = f(x2) при x1 = x10
ax4 = fig.add_subplot(224)
x2_values = np.linspace(x2_min, x2_max, 500)
y_values = f(x10, x2_values)
ax4.plot(x2_values, y_values, label=f'x1 = {x10}')
ax4.scatter([x20], [y0], color='red')
ax4.set_xlabel('x2')
ax4.set_ylabel('y=f(x2)')
ax4.set_title(f'y = f(x2) при x1 = {x10}')
ax4.legend()
ax4.annotate(f'({x10}, {x20})', (x20, y0), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()
