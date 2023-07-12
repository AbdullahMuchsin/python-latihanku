import numpy as np

# Cara mencari nilai hiperbolik dengan parameter radian
print("=================== SINH")
hasil = np.sinh(np.pi/2)
print(hasil)
hasil = np.sinh([np.pi/2,np.pi/3,np.pi/4]) # list / array
print(hasil)
print("=================== COSH")
hasil1 = np.cosh(np.pi/2)
print(hasil1)
hasil1 = np.cosh([np.pi/2,np.pi/3,np.pi/4]) # list / array
print(hasil1)
print("=================== TANH")
hasil2 = np.tanh(np.pi/2)
print(hasil2)
hasil2 = np.tanh([np.pi/2,np.pi/3,np.pi/4]) # list / array
print(hasil2)
# Cara konversi hasil ke radian dengan arcsinh, arccosh, dan arctanh
print("=================== ARCSINH")
hasil5 = np.arcsinh(1.0)
print(hasil5)
hasil5 = np.arcsinh([0.1,0.3,0.5])
print(hasil5)
print("=================== ARCCOSH")
hasil6 = np.arccosh(0.1)
print(hasil6)
hasil6 = np.arccosh([0.1,0.3,0.5])
print(hasil6)
print("=================== ARCTANH")
hasil7 = np.arctanh(0.1)
print(hasil7)
hasil7 = np.arctanh([0.1,0.3,0.5])
print(hasil7)