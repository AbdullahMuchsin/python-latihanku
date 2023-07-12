import numpy as np
import matplotlib.pyplot as plt

# Persamaan Garis
# y = 2x + 3

x = np.arange(0,10)
y = 2*x + 3

plt.figure("Garis Konsisten")
plt.plot(x)
plt.plot(y)
plt.plot(x,y)

# Lingkaran
jari2 = 5
sudut = np.linspace(0,2*np.pi,100)

x2 = jari2*(np.cos(sudut))
y2 = jari2*(np.sin(sudut))

plt.figure("Lingkaran")
plt.plot(x2)
plt.plot(y2)
plt.plot(x2,y2)
plt.show()