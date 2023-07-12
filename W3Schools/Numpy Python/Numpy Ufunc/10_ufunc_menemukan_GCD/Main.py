import numpy as np

a = 4
b = 8
x = np.array([2,4,28])
ndarange = np.arange(3,10)
# Cara menemukan FPB(Faktor Persekutuan Besar) dengan fungsi numpy yaitu gcd
print("=============== Fungsi GCD")
hasil = np.gcd(a,b)
print(hasil)
# Pakai fungsi tambahan dari gcd reduce untuk list / array
hasil2 = np.gcd.reduce(x)
print(hasil2)
hasil3 = np.gcd.reduce(ndarange)
print(hasil3)