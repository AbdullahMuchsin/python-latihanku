import numpy as np

# Operasi di Numpy
ndarray = np.arange(0,10)
print(ndarray)
print("=============== Operasi Tambah")
print(ndarray + 6)
print(ndarray + ndarray)
print("=============== Operasi Pengurangan")
print(ndarray - 2)
print(ndarray - ndarray)
print("=============== Operasi Perkalian")
print(ndarray * 3)
print(ndarray * ndarray)
print("=============== Operasi Pembagian")
print(ndarray / 6)
print(ndarray / ndarray) # Jika ada error karena di bagi nol di numpy tetap dieksekusi
print(ndarray / 0) # Jika ada error karena di bagi nol di numpy tetap dieksekusi
print("=============== Fungsi Akar (sqrt) di Numpy")
print(np.sqrt(ndarray))
print("=============== Fungsi Log, sin, cos, dan tan")
print("Log :",np.log(ndarray))
print("\nsin :",np.sin(ndarray))
print("\ncos :",np.cos(ndarray))
print("\ntan :",np.tan(ndarray))
print("=============== Fungsi Min, Max, dan exp(Exsponensial (e = 2.7182))")
print("Min :",np.min(ndarray))
print("\nMax :",np.max(ndarray))
print("\nExp :",np.exp(ndarray))
