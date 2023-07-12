import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([4,3,2,1,7])

# Cara menembukan produk atau mengalikan di numpy
print("=============== Fungsi proud mengalikan n dimensi")
hasil11 = np.prod(x) # Akan mengalikan semua n 
print(hasil11)
hasil12 = np.prod([x,y]) # akan mengalikan semua n secara urut
print(hasil12)
hasil13 = np.prod([x,y], axis=1) # akan mengalikan setiap larik
print(hasil13)
print("=============== Fungsi cumprod mangalikan secara kumulatif")
hasil21 = np.cumprod(x)
hasil22 = np.cumprod(y)
print(hasil21)
print(hasil22)