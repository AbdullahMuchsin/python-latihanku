import numpy as np
from math import log

ndarray = np.arange(1,11)

# Melakukan operasi log di numpy
print("========================= Log dengan basis 2")
hasil = np.log2(ndarray)
print(hasil)
print("========================= Log dengan basis 10")
hasil2 = np.log10(ndarray)
print(hasil2)
print("========================= Log dengan basis e")
hasil3 = np.log(ndarray)
print(hasil3)
print("========================= Buat log sendiri dengan frompyfunc")
ndlog = np.frompyfunc(log, 2, 1)
hasil4 = ndlog([1,2,3,4,5],[10,10,10,10,10])
print(hasil4)