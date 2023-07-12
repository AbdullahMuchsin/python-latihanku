import numpy as np
from numpy import random

# Bilangan Distribusi Uniform yaitu dari 0-1
print("=========== Bilangan Distribusi Uniform")
nduniform = random.rand(2,3)
print(nduniform)
# Bilangan Distribusi Kontinu atau Normal (Gaussian)
print("=========== Bilangan Distribusi Normal")
ndnormal = random.randn(2,4)
print(ndnormal)
# Bilangan Random Integer
print("=========== Bilangan Random Int")
ndint = random.randint(5,10,(3,4))
print(ndint)
# Fungsi Reshape Untuk Mengubah Dimensi Atau Ukuran dan shape untuk cek ukuran
print("=========== Shape")
ndshape = random.randint(0,10,(4,4))
print(ndshape)
print("Ukuran :",ndshape.shape)
print("=========== Reshape")
ndreshape = ndshape.reshape(2,8) # Untuk Merubah Harus Sama Ukuran Nya Tidak Boleh Kurang Atau Lebih
ndreshape2 = random.randint(3,9,20).reshape(10,2)
print(ndreshape)
print(ndreshape2)
print("=========== Fungsi max, min, argmax, and argmin")
ndmn = random.randint(0,131,20)
ndmn2 = random.randint(3,100,(4,4))
print(ndmn)
print("Max :", ndmn.max())
print("Index Max :", ndmn.argmax())
print("Min :",ndmn.min())
print("Index Min :",ndmn.argmin())
print("------------ 2D")
print(ndmn2)
print("Max :", ndmn2.max())
print("Index Max :", ndmn2.argmax())
print("Min :",ndmn2.min())
print("Index Min :",ndmn2.argmin())
print("============ Cek Type Dengan Dtype")
print("Tipe ndmn :",ndmn.dtype)
print("Tipe ndmn2 :",ndmn2.dtype)

# Indexing di Numpy
print("============ Indexing in Numpy 1D")
ex = np.arange(0,10)
print(ex)
print(ex[3]) # Ambil nilai dari index 3
print(ex[:5]) # Ambil nilai dari awal sampai index sebelum 5 (4)
print(ex[3:]) # Ambil nilai dimulai dari index 3 sampai ter akhir
print(ex[:]) # Ambil nilai dari awal sampai akhir
print("============ Indexing in Numpy 2D")
ex2 = random.randint(0,10,(5,5))
print(ex2)
print(ex2[2]) # Ambil nilai dari baris 3
print(ex2[2][3]) # Ambil nilai baris 3 kolom 4 (Tidak di rekomendasikan)
print(ex2[2, 3]) # Ambil nilai baris 3 kolom 4 (Cara ini di rekomendasikan di numpy dari pada yang di atas)
print(ex2[2:3,2:]) # Ambil nilai dari baris 3 kolom 3 sampai 5
print(ex2[3:,:3]) # Ambil nilai dari baris 4 dan 5 kolom 1 sampai 3
print("============ Take Value in Boolean")
ndex = (ex > 5)
print(ndex)
print(ex[ndex])
print("------------ Ambil Nilai Ganjil")
ndex = (ex%2 == 1)
print(ex[ndex])
print("------------ Ambil Nilai Genap")
ndex = (ex%2 == 0)
print(ex[ndex])
print("------------ Dengan Cara Cepat")
ex = ex[(ex < 5)]
print(ex)
ex2 = ex2[(ex2 > 5)]
print(ex2) # Hasil dari 2D akan menjadi 1D jika ingin dirubah jadi 2D lagi bisa pakai fungsi reshape
print("============ Copy dan View di Numpy")
# Jika pakai copy ketika melakukan perubahan tidak akan berdampak juga pada yang asli
# Tapi jika pakai view kebalikan dari copy
# Kita dapat mengeceknya dengan base jika hasilnya None bararti itu copy
ex = np.arange(0,10)
ex1 = ex.copy()
ex2 = ex.view()
print("ex :", ex)
print("ex1 :", ex1)
print("ex2 :", ex2)
ex1[2] = 72
ex2[5] = 82
print("ex1 :", ex1)
print("ex2 :", ex2)
print("ex :", ex)
print("ex1 :", ex1.base)
print("ex2 :", ex2.base)