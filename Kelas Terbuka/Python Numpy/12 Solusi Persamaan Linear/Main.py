import numpy as np

A = np.array([[2,2],
              [1,3]])
Y = np.array([[18],
              [19]])

# Cari Nilai X1 X2 dengan Cara X-invers . Nilai Y1,Y2
A_inv = np.linalg.inv(A)
X1 = np.dot(A_inv,Y)

# Cari Nilai X1 X2 dengan Fungsi dari numpy
X2 = np.linalg.solve(A,Y)
print("View")
print("A",A)
print("Y",Y)
print("A_inv",A_inv)
print("X1",X1)
print("X2",X2)

