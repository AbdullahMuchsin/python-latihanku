import numpy as np

a = np.array([1,2,3,4])
b = np.array([[1,2,3,4],[6,7,8,9]])
c = np.array([[[1,2,3,4],[5,6,7,8]],[[4,3,2,1],[9,8,7,6]]])

print("Index pertama sampai index-3 dari a:",a[0:3])
print("Index ke-2 sampai terakhir dari a:",a[2:])
print("Index ke-0 sampai terakhir dari loncat 2 a:",a[::2])


print("baris ke-2 kolom semua b:",b[1,:])
print("baris ke-1 dan ke-2 kolom ke-3 b:",b[0:2,2])
print("baris ke-1 dan ke-2 kolom ke-2 sampai kolom terakhir b:\n",b[:,1:])

print("Matrix ke-1 baris ke-2 kolom semua c:",c[0,1,:])
print("Matrix ke-2 baris ke-1 dan ke-2 kolom ke-3 c:",c[1,:2,2])
print("Matrik ke-1 dan ke-2 baris ke-1 dan ke-2 kolom ke-2 sampai kolom terakhir c:\n",c[:,:,1:])

# Untuk Mengambil nilai dari terakhir bisa dengan -
print("\nIndex ke-3 sampai terakhir dari a:",a[-3:-1])
print("Index baris kedua kolom ke-2 sampai k-3 dari b:",b[-1,-3:-2])
print("Index matrik kedua baris ke pertama sampai terakhir kolom terakhir ke dua dari c:",c[-1,-2:,-2])