## MENGGUNKAN COPY PADA LIST UNTUK FULL DUPLIKAT

a = ["Apel","Nanas","Leci","Melon"]
b = a # Pass by reference

print("="*3 + "Pass by reference".upper())
print(f"Data a : {a}")
print(f"Data b : {b}")
a[0] = "Semangka"
b[-1] = "Durian"
# Maka data a dan b akan sama berubah
print(f"Data a : {a}")
print(f"Data b : {b}")
# Kedua andress sama
print(f"andress a : {hex(id(a))}")
print(f"andress b : {hex(id(b))}\n")

print("="*3 + "duplikat full".upper())
c = a.copy()
print(f"Data a : {a}")
print(f"Data c : {c}")
print(f"Data b : {b}")
a[0] = "Lemon"
b[-1] = "Tomat"
c[-2] = "Anggur"
# Maka data a dan b akan sama tapi data c berbeda
print(f"\nData a : {a}")
print(f"Data c : {c}")
print(f"Data b : {b}")
# Kedua andress a dan b sama tapi c berbeda 
## Karena pakai a.copy() untuk duplikat
print(f"andress a : {hex(id(a))}")
print(f"andress b : {hex(id(b))}")
print(f"andress c : {hex(id(c))}")
