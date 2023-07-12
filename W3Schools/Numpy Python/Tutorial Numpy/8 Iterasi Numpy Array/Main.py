import numpy as np

# Iterasi dengan 1D
a = np.array([1,2,3,4,5,6])

for i in a:
    print(i)

print("")
# Iterasi dengan 2D
b = np.array([[1,2,3,4],[5,6,7,8]])

for i in b:
    print(i)

print("b".center(10,"="))
for i in b:
    for j in i:
        print(j)

print("")
# Iterasi dengan 3D
c = np.array([[[1,2,3],[4,5,6]],[[3,2,1],[6,5,4]]])

for i in c:
    print(i)

print("c".center(10,"="))
for i in c:
    for j in i:
        for k in j:
            print(k)

# Menggunkan fungsi iter agar lebih mudah

print("\n========== A ============")
for x in np.nditer(a):
    print(x)

print("\n========== B ============")
for y in np.nditer(b):
    print(y)

print("\n========== C ============")
for z in np.nditer(c):
    print(z)

# Cara pakai nditer dengan hasil tipe data yang ditentukan

# for i in np.nditer(b, flags = ['buffer'], op_dtype = 'S'):
#     print(i)
# Belum tahu kenpa tidak bisa

# Iterasi dengan ukuran yang berbeda
print("========= : ========")
for j in np.nditer(b[:,3]):
    print(j)

# Menggunkan ndenumerate untuk mengambil urutan index nya
print("\n=========== 1D ============")
for index,data in np.ndenumerate(a):
    print(index,data)

print("\n=========== 2D ============")
for index,data in np.ndenumerate(b):
    print(index,data)

print("\n=========== 3D ============")
for index in np.ndenumerate(c):
    print(index)