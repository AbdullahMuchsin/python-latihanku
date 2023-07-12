import numpy as np

x = np.array([5.22,-5.22,7.77,-7.77])

print("=================== Fungsi Fix and Trunc")
# Dibulatkan ke bawah tidak melihat + dan -
hasil11 = np.fix(x)
hasil12 = np.trunc(x)
print(hasil11)
print(hasil12)
print("=================== Fungsi Round")
# Dibulatkan ke yang paling dekat
hasil2 = np.around(x)
print(hasil2)
print("=================== Fungsi Floor")
# Dibulatkan ke bawah melihat + dan -
hasil3 = np.floor(x)
print(hasil3)
print("=================== Fungsi Ceil")
# Dibulatkan ke atas melihat + dan -
hasil4 = np.ceil(x)
print(hasil4)