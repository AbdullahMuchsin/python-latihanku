import numpy as np

# Jika ingin meng copy pakai fungsi copy agar perubahan antar kedua tidak saling memengaruhi
# Jika pakai fungsi view akan memengaruhi kedua nya

# Menggunakan fungsi copy()
a = np.array([1,2,3,4])
x = a.copy() # Pakai fungsi copy
a[0] = 122
print(a)
print(x)

x[2] = 300
print(a)
print(x)

print("")
# Menggunakan fugsi view()
b = np.array([11,22,33,44,55])
y = b.view()
b[2] = 0
print(b)
print(y)

y[0] = 7
print(b)
print(y)

print("")
# Cara cek atribut tersebut memiliki data atau tidak dengan base
# Jika memiliki akan menghasilkan None jika tidak akan menampilkan data

print(x.base)
print(y.base)