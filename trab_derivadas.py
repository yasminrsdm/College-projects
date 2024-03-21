# -*- coding: utf-8 -*-
"""Trab Derivadas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-PhLROUSQYRilATgmNMv0biH6xhtkibX

# **1)**
"""

import numpy as np

# Função para construir uma matriz para cálculos de derivadas.
def construir_matriz(n, h=0.001, impar=True):
    t = int((n - 1) / 2)  # Calcula o número de termos a serem usados.
    matriz = np.zeros((t, t))  # Cria uma matriz de zeros com tamanho (t, t).

    for e in range(1, int(t + 1)):  # Loop para iterar pelas linhas da matriz.
        for m in range(1, int(t + 1)):  # Loop para iterar pelas colunas da matriz.
            if impar:
                # Calcula o valor do termo da matriz para derivadas ímpares.
                matriz[e - 1, m - 1] = (2 * ((e * h) ** (2 * m - 1))) / np.math.factorial((2 * m) - 1)
            else:
                # Calcula o valor do termo da matriz para derivadas pares.
                matriz[e - 1, m - 1] = (2 * ((e * h) ** (2 * m))) / np.math.factorial(2 * (m))

    return matriz  # Retorna a matriz construída.

# Função para construir os deltas usados nos cálculos das derivadas.
def construir_deltas(n, func, x0, h=0.001, par=True):
    l = []  # Inicializa uma lista vazia para armazenar os deltas calculados.
    t = (n - 1) / 2  # Calcula o número de termos a serem usados.

    for e in range(1, int(t + 1)):  # Loop para iterar pelos termos de delta.
        if par:
            # Calcula o delta para derivadas pares.
            delta = func(x0 + (e * h)) + func(x0 - (e * h)) - 2 * func(x0)
        else:
            # Calcula o delta para derivadas ímpares.
            delta = func(x0 + (e * h)) - func(x0 - (e * h))
        l.append(delta)  # Adiciona o delta calculado à lista.

    l = np.array(l)  # Converte a lista de deltas em uma array NumPy.
    l = l.reshape((int(t), 1))  # Redimensiona a array para ter a forma correta.
    return l  # Retorna os deltas como uma array.

# Função para calcular derivada de uma determinada ordem.
def calcular_derivada(orde, func, x0, n, h=0.001):
    if type(orde) not in (int, float):
        return 'TypeError: a ordem deve ser int ou float'  # Verifica se a ordem é válida.

    N = n - 1  # Calcula o número de pontos.
    par = (orde % 2) == 0  # Verifica se a ordem é par.

    # Calcula os deltas necessários para os cálculos.
    deltas_func = construir_deltas(N, func, x0, h, par)
    matriz_func = construir_matriz(N, h, not par)

    matriz_inversa = np.linalg.inv(matriz_func)  # Calcula a matriz inversa.
    valores_derivada = np.matmul(matriz_inversa, deltas_func)  # Calcula a derivada usando multiplicação de matriz.

    if par:
        indice = int((orde / 2) - 1)  # Calcula o índice correspondente à derivada par.
    else:
        indice = int((orde - 1) / 2)  # Calcula o índice correspondente à derivada ímpar.

    return float(valores_derivada[indice])  # Retorna o valor da derivada calculada.

"""# **2)**"""

import numpy as np
from scipy.misc import derivative

# Definir a função f(x)
def f(x):
    return x**3 + x**2 - 3*x + 2

# Intervalo [−2, 2]
intervalo = np.linspace(-2, 2, 5)
resultados_calculados = []

# Calcular as derivadas usando o código fornecido para cada ponto no intervalo
for x0 in intervalo:
    primeira_derivada_calculada, segunda_derivada_calculada = calcular_derivadas(x0, n=5)
    resultados_calculados.append((x0, primeira_derivada_calculada, segunda_derivada_calculada))

# Calcular as derivadas usando scipy.misc.derivative para cada ponto no intervalo
resultados_scipy = []
for x0 in intervalo:
    primeira_derivada_scipy = derivative(f, x0, dx=0.001, n=1, order=3)
    segunda_derivada_scipy = derivative(f, x0, dx=0.001, n=2, order=3)
    resultados_scipy.append((x0, primeira_derivada_scipy, segunda_derivada_scipy))

# Imprimir os resultados
for (x0, primeira_calculada, segunda_calculada), (x0_scipy, primeira_scipy, segunda_scipy) in zip(resultados_calculados, resultados_scipy):
    print("Ponto:", x0)
    print("Primeira derivada calculada:", primeira_calculada)
    print("Primeira derivada com scipy.misc.derivative:", primeira_scipy)
    print("Segunda derivada calculada:", segunda_calculada)
    print("Segunda derivada com scipy.misc.derivative:", segunda_scipy)
    print("=" * 40)

"""# **3)**"""

import sympy as sp

# a) y = a * x**n + b
a, b, x, n = sp.symbols('a b x n')
y_a = a * x**n + b
derivada_a = sp.diff(y_a, x)
print("a)",derivada_a)

# b) y = exp(-x) * cos(2 * x)
y_b = sp.exp(-x) * sp.cos(2 * x)
derivada_b = sp.diff(y_b, x)
print("b)",derivada_b)

# c) y = x**3 + x**2 - 3*x
y_c = x**3 + x**2 - 3*x
derivada_c = sp.diff(y_c, x)
print("c)",derivada_c)