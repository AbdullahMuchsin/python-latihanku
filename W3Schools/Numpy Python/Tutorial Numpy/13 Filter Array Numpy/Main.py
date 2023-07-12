import numpy as np

# Cara Menyaring Data Array yang ingin di ambil
ndarray = np.array([2,1,2,3,24,52,5,2,1,45,13,3,4])
ndsort = np.sort(ndarray)

print(ndsort)
print("------------------------------------------")
# Cara Pertama
a = [True,False,True,False,True,False,True,False,True,False,True,False,True]
y = ndsort[a]
print(y)
print("------------------------------------------")
# Cara Kedua 1
a = []

for i in ndsort:
    if i > 4: # Mencari Nilai Lebih Besar Dari 4
        a.append(True)
    else:
        a.append(False)
hasil = ndsort[a]

print(hasil)
print("------------------------------------------")
# Cara Kedua 2
a = []

for i in ndsort:
    if i%2 == 0: # Mencari Nilai Genap
        a.append(True)
    else:
        a.append(False)

hasil = ndsort[a]
print(hasil)
print("------------------------------------------")
# Cara Ketiga Yang Mudah
filter_ = ndsort > 10 # Mencari Nilai Lebih Besar Dari 10
hasil = ndsort[filter_]

print(hasil)
print("------------------------------------------")
# Contoh Lain
filter_ = ndsort%2 == 1 # Mencari Nilai Ganjil
hasil = ndsort[filter_]

print(hasil)
print("------------------------------------------")