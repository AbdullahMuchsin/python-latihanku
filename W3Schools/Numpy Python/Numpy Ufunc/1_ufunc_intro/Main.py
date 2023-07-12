import numpy as np

# Cara biasa menjumblahkan dengan python yaitu dengan zip
a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = []

for i,j in zip(a, b):
    c.append(i + j)
print(c)

# Cara menjumblahkan dengan library numpy
ndarray = np.array([1,2,3,4,5])
ndarray1 = np.array([6,7,8,9,10])

hasil = np.add(ndarray, ndarray1)
print(hasil)