import numpy as np

x = [11,12,13,14,15]
y = [1,2,3,4,5]

# Pertambahan dengan fungsi add()
print("================== ADD()")
hasil1 = np.add(x,y)
print(hasil1)
# Pengurangan dengan fungsi SUBTRACT
print("================== SUBTRACT()")
hasil2 = np.subtract(x,y)
print(hasil2)
# Perkalian dengan fungsi multiply
print("================== MULTIPLY()")
hasil3 = np.multiply(x,y)
print(hasil3)
# Pembagian dengan fungsi divide
print("================== DIVIDE()")
hasil4 = np.divide(x,y)
print(hasil4)
# Eksponen dengan fungsi power
print("================== POWER()")
hasil5 = np.power(x,y)
print(hasil5)
# Modulus dengan fungsi mod and remainder
print("================== MOD() and REMAINDER()")
hasil61 = np.mod(x,y)
hasil62 = np.remainder(x,y)
print(hasil61)
print(hasil62)
# Hasil bagi dan modulus dengan fungsi divmod
print("================== DIVMOD()")
hasil71,hasil72 = np.divmod(x,y)
print("Hasil bagi    :", hasil71)
print("Hasil modulus :", hasil72)
# Nilai mutlak dengan fungsi abs/absolute
print("================== ABSOLUTE()")
ex = np.array([-13,-13,-313,-32])
hasil8 = np.absolute(ex)
print(hasil8)