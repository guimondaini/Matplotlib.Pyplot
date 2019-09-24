# Boxplot - diagrama de caixa

import matplotlib.pyplot as plt
import random

vetor = []

for i in range(10):
	numero_aleatorio = random.randint(0,50)
	vetor.append(numero_aleatorio)

plt.title("Boxplot")
plt.boxplot(vetor)
plt.show()