# Crescimento da População Brasileira 1980-2016

import matplotlib.pyplot as plt

#Abrir arquivo DataSus
dados = open("populacao-brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
	if i != 0:
		linha = dados[i].split(";")
		x.append(int(linha[0]))
		y.append(int(linha[1]))

plt.title("Crescimento da População Brasileira 1980-2016")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")

plt.plot(x, y, color="k", linestyle="--")
plt.bar(x, y, color="#e4e4e4")

plt.show()
