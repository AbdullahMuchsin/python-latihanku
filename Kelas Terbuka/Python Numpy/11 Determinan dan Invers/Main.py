import numpy as np

a = np.array([[1,-2],
               [-1,1]])

print("Mencari Invers a:")
a_inv = np.linalg.inv(a)
print(a_inv)

print("Mencari Determinan a:")
a_det = np.linalg.det(a)
ainv_det = np.linalg.det(a_inv)
print("Determinan a:\n",a_det)
print("Determinan a_inv:\n",ainv_det)


print("Perkalian Dari Matrix a dan Invers a:")
print(np.dot(a,a_inv))
