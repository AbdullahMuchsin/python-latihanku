import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([3,4,5,5,6])
z = np.array([2,3,4,7,8])

# Penjumblahan dengan add menjumblahkan setiap elemen / n
print("================== ADD")
hasil = np.add(x,y)
print(hasil)
# Penjumblahan dengan sum menjumblahkan semua baris or kolom
print("================== SUM")
hasil21 = np.sum([x,y,z])
print(hasil21)
# Dengan tambah parameter axis untuk menentukan barapa larik
hasil22 = np.sum([x,y,z],axis=1)
print(hasil22)
# Penjumblahan dengan cumsum yaitu penjumblahan kumulatif
print("================== CUMSUM")
hasil3 = np.cumsum(x)
print(hasil3)
