import numpy as np

a = np.array([1,2,3,4])
b = np.array([[1,2,3,4],[6,7,8,9]])
c = np.array([[[1,2,3,4],[5,6,7,8]],[[4,3,2,1],[9,8,7,6]]])

print("Index pertama dari a:",a[0])
print("Index pertama dari b:",b[0,0])
print("Index pertama dari c:",c[0,0,0])

print("\nIndex ketiga dari a:",a[2])
print("Index baris kedua kolom ketiga dari b:",b[1,2])
print("Index matrik pertama baris ke dua kolom pertama dari c:",c[0,1,0])

# Untuk Mengambil nilai dari terakhir bisa dengan -
print("\nIndex terakhir dari a:",a[-1])
print("Index baris kedua kolom terakhir dari b:",b[1,-1])
print("Index matrik kedua baris ke dua kolom terakhir ke dua dari c:",c[1,1,-2])