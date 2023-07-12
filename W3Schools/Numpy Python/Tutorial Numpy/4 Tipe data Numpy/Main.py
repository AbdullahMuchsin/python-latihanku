import numpy as np

# Tipe data pada numpy ada beberapa macaam :
# i - Bilangan bulat
# b - Boolean
# u - Bilangan bulat yang tidak ditandatangani
# f - Mengambang
# c - Pelampung kompleks
# m - delta waktu
# M - Tanggal waktu
# O - Objek
# S - Rangkaian
# U - Sring unicode
# V - Memperbaiki potongan memori untuk tipe lain (void)

# Mengecek type data dengan dtype
a = np.array([1,2,3,4])
print(a.dtype)

b = np.array(["a","b","1","2"])
print(b.dtype)

c = np.array(["a",1.2,True,4])
print(c.dtype)

print("")
# Membuat Array dengan tipe data yang ditetapkan
a1 = np.array([1,2,3,4], dtype = 'f')
print(a1)
print(a1.dtype)

b1 = np.array([2.5,1.4,2], dtype = int)
print(b1)
print(b1.dtype)

# c1 = np.array([1,2.4,"c"], dtype = 'i') # Akan Error jika tipe data tidak mendukung tipe data dari nilai
# print(c1)
# print(c1.dtye)

c1 = np.array([1,2.4,"c"], dtype = 'bool')
print(c1)
print(c1.dtype)

print("")
# Mengkonversi tipe data pada Array yang ada dengan astype
a2 = np.array([1,2,3,4])
k_a2 = a2.astype(float)

print(k_a2)
print(k_a2.dtype)

b2 = np.array([True,False,True,True])
k_b2 = b2.astype(int)

print(k_b2)
print(k_b2.dtype)

# c2 = np.array([1,2,True,"a"]) # Akan Error jika tipe data tidak mendukung tipe data dari nilai
# k_c2 = c2.astype('i')

c2 = np.array([1,2,1.3,False])
k_c2 = c2.astype('bool')

print(k_c2)
print(k_c2.dtype)