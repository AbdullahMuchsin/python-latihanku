## LATIHAN OPERASI ASSIGNMENT

# Operasi mempersingkat eksekusi dengan assignment

a = 4 
b = 7
print("Nilai a :",a)
print("Nilai b :",b)

print("=========PENJUMBLAHAN=========")
a = 4 
b = 7
a += b # Ini sama dengan a = a + b
print("Hasil dari a += b adalah", a)

print("=========PENGURANGAN=========")
a = 4 
b = 7
a -= b # Ini sama dengan a = a - b
print("Hasil dari a -= b adalah", a)

print("=========PERKALIAN=========")
a = 4 
b = 7
a *= b # Ini sama dengan a = a * b
print("Hasil dari a *= b adalah", a)

print("=========PEMBAGIAN=========")
a = 4 
b = 7
a /= b # Ini sama dengan a = a / b
print("Hasil dari a /= b adalah", a)

print("=========EKSPONEN=========")
a = 4 
b = 7
a **= b # Ini sama dengan a = a ** b
print("Hasil dari a **= b adalah", a)

print("=========MODULUS=========")
a = 4 
b = 7
a %= b # Ini sama dengan a = a % b
print("Hasil dari a %= b adalah", a)

print("=========FLOOR DEVISION=========")
a = 4 
b = 7
a //= b # Ini sama dengan a = a // b
print("Hasil dari a //= b adalah", a)

print("=========OR=========")
x = 0b0010
y = 0b0100
print("Nilai x ",x,"Binary",format(x,'04b'))
print("Nilai y ",y,"Binary",format(y,'04b'))
x |= y # Ini sama dengan a = a | y
print("----------------------------(|)")
print("Nilai x ",a,"Binary",format(a,'04b'))

x = True
y = False
x |= b
print("Hasil dari x |= y adalah", x)
x = True
y = False
x |= y
print("Hasil dari x |= b adalah", x)

print("=========AND=========")
z = 0b0111
k = 0b0100
print("Nilai z ",z,"Binary",format(z,'04b'))
print("Nilai k ",k,"Binary",format(k,'04b'))
z &= k # Ini sama dengan z = z & k
print("----------------------------(&)")
print("Nilai z ",z,"Binary",format(z,'04b'))

z = True
k = False
z &= k
print("Hasil dari x &= k adalah", x)
z = True
y = True
z &= k
print("Hasil dari z &= k adalah", z)

print("=========XOR=========")
x = 0b0010
y = 0b0100
print("Nilai a ",x,"Binary",format(x,'04b'))
print("Nilai y ",y,"Binary",format(y,'04b'))
x ^= y # Ini sama dengan a = a ^ y
print("----------------------------(^)")
print("Nilai a ",x,"Binary",format(x,'04b'))

x = True
y = False
x ^= y
print("Hasil dari x ^= y adalah", x)
x = True
y = True
x ^= y
print("Hasil dari x ^= y adalah", x)

print("=========SHFITRIGHT=========")
x = 0b001000
print("Nilai x ",x,"Binary",format(x,'06b'))
x >>= 2 # Ini sama dengan a = a >> 2
print("----------------------------(>>)")
print("Nilai x ",x,"Binary",format(x,'06b'))

print("=========SHIFTLEFT=========")
x = 0b001000
print("Nilai x ",x,"Binary",format(x,'06b'))
x <<= 2 # Ini sama dengan a = a << 2
print("----------------------------(<<)")
print("Nilai x ",x,"Binary",format(x,'06b'))
