import numpy as np

# Array python
a = [1,2,3,4,5]
b = [6,7,8,9,10]

# Array numpy
anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

# ELEMENTWISE Operation

# Penjumblahan
hasil = anp + bnp
print(hasil)

# Pengurangan
hasil = anp - bnp
print(hasil)

# Perkalian
hasil = anp * bnp
print(hasil)

# Pembagian
hasil = anp / bnp
print(hasil)

# Eksposisi
hasil = anp ** bnp
print(hasil)

# Mutidimensi / Matrix
c = np.array(([1,2,3,4] , [5,6,7,8]))
d = np.array(([11,12,13,14] , [15,16,17,18]))

hasil = c + d
print(hasil)

print(np.__version__)