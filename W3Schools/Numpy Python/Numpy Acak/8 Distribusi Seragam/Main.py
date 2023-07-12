import numpy, seaborn
import matplotlib.pyplot as plt

# Menggambarkan dimana probabilitas memiliki peluang pristiwa yang sama 
# Untuk terjadi

ex = numpy.random.uniform(size=(10))
print(ex)

x = numpy.random.uniform(size=(1000))
seaborn.distplot(x,hist=True,kde=True)

plt.show()