import numpy as np
import matplotlib.pyplot as plt

# Extraer muestras de la distribución.:
mu, sigma = 0, 0.1 # mean and standard deviation

s = np.random.normal(mu, sigma, 32000)    # ¡Descomentar! para ver Gráfica Normal (Gauss)

# s = np.random.randint(1,32000,32000)        # !Descomentar! para ver Gráfica RandInt

# Muestra el histograma de las muestras, junto con la función de densidad de probabilidad.:
count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.show()
