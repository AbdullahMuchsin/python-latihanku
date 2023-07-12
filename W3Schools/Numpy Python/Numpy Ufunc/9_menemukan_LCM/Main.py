import numpy as np

a = 3
b = 7
ndarray = np.array([2,3,5])
ndarnge = np.arange(2,8)
# Cara menemukan KPK (Kelipatan Persekutuan Terendah) dengan fungsi lcm
print("================== Fungsi LCM")
hasil = np.lcm(a,b)
print(hasil)
# Jika dengan array / list pakai fungsi tambahan reduce dari lcm
hasil2 = np.lcm.reduce(ndarray)
print(hasil2)
hasil3 = np.lcm.reduce(ndarnge)
print(hasil3)