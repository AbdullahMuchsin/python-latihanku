import numpy as np

# Cara mengetahui dimensi itu memiliki berapa data atau bentuk bisa menggunakan
# Fungsi shape

a = np.array([[1,2,3,4],[1,2,3,4]])
print(a.shape)

b = np.array([[[3,3,4],[0,1,4]],[[1,2,5],[1,2,6]]])
print(b.shape)

c = np.array([1,2,3,4,5], ndmin = 5)
print(c)
print(c.shape)