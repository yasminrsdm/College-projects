# -*- coding: utf-8 -*-
"""Exercicio minimos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XjOjX_zmH5A9CHf20jk4YZRXSh38LrZ3
"""

import numpy as np

def ajuste_linear(x, y):
    # Calcula os parâmetros a e b do ajuste linear (y = ax + b)
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x_squared = np.sum(x**2)
    sum_xy = np.sum(x * y)

    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    b = (sum_y - a * sum_x) / n

    return a, b

import matplotlib.pyplot as plt

# Ler os dados do arquivo "dados.txt" (certifique-se de que o arquivo esteja no mesmo diretório)
dados = np.loadtxt("dados.txt")
x = dados[:, 0]
y = dados[:, 1]

# Realizar o ajuste linear
a, b = ajuste_linear(x, y)

# Gerar pontos para a reta de ajuste
x_fit = np.linspace(min(x), max(x), 100)
y_fit = a * x_fit + b

# Plotar os pontos e a reta de ajuste
plt.scatter(x, y, label="Pontos")
plt.plot(x_fit, y_fit, color='pink', label=f"Ajuste Linear: y = {a:.2f}x + {b:.2f}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

# Imprimir os valores de a e b
print("Parâmetros do Ajuste Linear:")
print(f"a = {a:.2f}")
print(f"b = {b:.2f}")