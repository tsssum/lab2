#Ивановская 9 группа
#2d

#Цвет: teal, coral, sandybrown, palegreen.
#Линия: штриховая, сплошная, штриховая, штриховая.
#Толщина: 2, 1, 2, 2.
#Сетка: ☑,☒,☑,☑.
#Сетку сделать пунктирной.

#(A) y = ±√(√(1 + 4x^2) - x^2 - 1)
#(B) 𝑟 = 100(1.2 + 0.9 cos(1.8𝜑) + 0.1 cos(0.9𝜑))

import numpy as np
import matplotlib.pyplot as plt

plt.figure('Графики', figsize=(10, 5))

x = np.linspace(-10, 10, 1000)
y_pos = np.sqrt(np.sqrt(1 + 4 * x**2) - x**2 - 1)
y_neg = -np.sqrt(np.sqrt(1 + 4 * x**2) - x**2 - 1)


#график А
first = plt.subplot2grid([2,2], [1, 0])
first.plot(x, y_pos, color='teal', linestyle='--', linewidth=2)
first.plot(x, y_neg, color='teal', linestyle='--', linewidth=2)
first.set_title('y = ±√(√(1 + 4x^2) - x^2 - 1)')
first.grid(color='gray', linestyle=':', linewidth=1)


phi = np.linspace(0, 10 * 2 * np.pi, 1000)
r = 100 * (1.2 + 0.9 * np.cos(1.8 * phi) + 0.1 * np.cos(0.9 * phi))


#график В
second = plt.subplot2grid([6,2], [2, 1],  rowspan=3, polar=True)
second.plot(phi, r, color='coral', linestyle='-', linewidth=1)
second.set_title('r = 100(1.2 + 0.9 cos(1.8phi) + 0.1 cos(0.9phi))')
second.set_yticklabels([])
second.grid()

plt.show()