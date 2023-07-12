## LATIHAN MENGGUNAKAN DEEP COPY NESTED LIST

a = [1,2]
b = [4,8]

ab = [a,b, 9]
cab = ab.copy()

print(f"Data ab  : {ab}")
print(f"Data cab : {cab}")
print(f"address asli ab : {hex(id(ab))}")
print(f"address copy ab : {hex(id(cab))}")

# Cara mengambil need data list
print(f"Data ke 1,1-> {ab[0][0]}")
print(f"Data ke 2,2-> {cab[1][1]}")

ab[1][0] = 17
cab[0][1] = 20
ab[2] = 17

print("\naddress data list :")
if hex(id(ab[0])) == hex(id(cab[0])) :
    print(f"Data ab  : {ab}")
    print(f"Data cab : {cab}")
    print("Sama hanya data list yang terluar berbeda".upper())
    print(f"address 1 ab      : {hex(id(ab[0]))}")
    print(f"address copy 1 ab : {hex(id(cab[0]))}")
    print("Sama kan address nya".upper())
else:
    print("Tidak sama kan address nya".upper())

# Cara copy full (need copy)
from copy import deepcopy

xab = deepcopy(ab)
print("\nIni xab pakai deepcopy".upper())
print(f"Data ab  : {ab}")
print(f"Data cab : {cab}")
print(f"Data xab : {xab}")
print(f"address asli ab      : {hex(id(ab))}")
print(f"address copy ab      : {hex(id(cab))}")
print(f"address deep copy ab : {hex(id(xab))}")

ab[1][0] = 25
cab[0][1] = 21
xab[2] = 7

print("\naddress data list :")
if hex(id(ab[0])) == hex(id(xab[0])) :
    print(f"address 1 ab          : {hex(id(ab[0]))}")
    print(f"address copy 1 ab     : {hex(id(cab[0]))}")
    print(f"address deep cop 1 ab : {hex(id(xab[0]))}")
    print("Sama kan address nya".upper())
else:
    print(f"Data ab  : {ab}")
    print(f"Data cab : {cab}")
    print(f"Data xab : {xab}")
    print("Sama hanya data list yang terluar berbeda apalagi yang xab".upper())
    print(f"address 1 ab           : {hex(id(ab[0]))}")
    print(f"address copy 1 ab      : {hex(id(cab[0]))}")
    print(f"address deep copy 1 ab : {hex(id(xab[0]))}")
    print("Tidak sama kan address nya".upper())

