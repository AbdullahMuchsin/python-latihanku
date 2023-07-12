import numpy as np

# Array 0D
a = np.array(30)
print("0 D :",a)

# Array 1D
b = np.array([1,2,3,4,5])
print("1 D :",b)

# Array 2D
c = np.array([[1,2,3],[9,8,7]])
print("2 D :",c)

# Cara Atur Dimensi Array Saat Membuat dengan ndmin
d = np.array([40,4,3,2,], ndmin=20)
print("Costom D :",d)

# Cara Cek dimensi dengan ndim
print("0 D :",a.ndim)
print("1 D :",b.ndim)
print("2 D :",c.ndim)
print("Costom D :",d.ndim)