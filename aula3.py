import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]

# Título
titulo = "Scatterplot: gráfico de dispersão"

#Eixos
eixox = "Eixo X"
eixoy = "Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x, y, label="Meus pontos", color="k", marker=".", s=100)
plt.plot(x, y, color="k", linestyle=":")
plt.legend()

plt.show()