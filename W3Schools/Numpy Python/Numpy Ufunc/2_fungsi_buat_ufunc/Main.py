import numpy as np

# Cara Buat Fungsi Ufunc
def kllbalok(panjang,lebar,tinggi):
    hasil = 4 * (panjang + lebar + tinggi)
    hasil2 = 1 + hasil
    return hasil, hasil2

# Parametar frompyfunc 1. nama fungsi, 2. banyak input, 3. banyak output
baloks = np.frompyfunc(kllbalok, 3, 2)
a = [1,2,3,4,5,6,7]
b = [4,2,1,4,1,4,1]
c = [6,3,7,6,2,6,2]
print(baloks(a,b,c))

# Cara cek itu function ufunc apa bukan di numpy
# Yaitu dengan type

print("Ini adalah ufunc :", type(np.add)) # karena hasilnya numpy.ufunc jika selain ini bukan ufunc
print("Ini bukan ufunc :", type(np.argmax))

# Cek dengan if

if type(np.add) == np.ufunc:
    print("=========== Ini adalah ufunc ===========")
else:
    print("ini bukan ufunc")
