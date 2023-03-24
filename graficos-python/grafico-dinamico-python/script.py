import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 6)

plt.style.use('ggplot')
plt.ion() #inicio

for i in range(1000000):
    dados = np.random.randint(20, 30, 5) #20 é o minimo do valor gráfico e 30 o máximo, 5 representa o número de tabelas
    plt.cla()
    plt.clf()
    plt.bar(x, dados)
    plt.pause(1.5)

plt.ioff() #finalizador