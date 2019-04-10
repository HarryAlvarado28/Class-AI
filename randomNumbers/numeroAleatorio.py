from random import randint, uniform,random
import matplotlib.pyplot as plt

n = 1
a = 0
nvar = []
ntor = []
while a < 32000:
    nvar.append(a)
    ntor.append(randint(0,32000))  # randint()
    a+=n
plt.plot(nvar, ntor, 'ro')
plt.xlabel('Números Aleatorios')
plt.show()
