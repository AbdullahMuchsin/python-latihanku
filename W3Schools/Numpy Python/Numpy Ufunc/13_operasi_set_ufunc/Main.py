import numpy as np

x = np.array([1,2,3,4,5,3,5,4])
y = np.array([2,9,3,7,5])

# Fungsi ini hanya dapat dipakai array 1D
# Cara menjadikan array / list menjadi set di numpy dengan fungsi unique
print("================= Unique")
hasil = np.unique(x) # Nilai yang duplikat akan jadi satu karna set tidak bisa di duplikat
print(hasil)
# cara menemukan nilai yang sama di ke dua array dengan fungsi intersect1d
print("================= Intersect1d")
hasil1 = np.intersect1d(x, y, assume_unique=True)
print(hasil1)
# Menemukan nilai tidak sama pada array pertama di array kedua dengan fungsi setdiff1d
print("================= setdiff1d")
hasil2 = np.setdiff1d(x, y, assume_unique=True)
print(hasil2)
# Menemukan nilai yang tidak sama dari ke dua array tersebut dengan fungsi setxor1d
print("================= setxor1d")
hasil3 = np.setxor1d(x, y, assume_unique=True)
print(hasil3)
# assume_unique=True Berfungsi untuk mempercepat komputasi
# assume_unique=True Tapi setelah di jadikan True hasilnya malah berbeda