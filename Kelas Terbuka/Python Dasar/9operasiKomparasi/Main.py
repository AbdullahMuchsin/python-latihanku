## BELAJAR OPERASI KOMPARASI
# Semua hasil komparasi adalah boolean
# >,<,>=,<=,==,!=,is, and is not

a = 5
b = 3

# Komparasi lebih besar (>)
print("==== LEBIH BESAR (>)")
hasil = a > 8
print(a,'>',8,'=',hasil)
hasil = b > a
print(b,'>',a,'=',hasil)
hasil = a > 5
print(a,'>',5,'=',hasil)

# Komparasi kurang dari(<)
print("==== KURANG DARI (<)")
hasil = a < 8
print(a,'<',8,'=',hasil)
hasil = b < a
print(b,'<',a,'=',hasil)
hasil = a < 5
print(a,'<',5,'=',hasil)

# Komparasi lebih besar sama dengan (>=)
print("==== LEBIH BESAR SAMA DENGAN (>=)")
hasil = a >= 8
print(a,'>=',8,'=',hasil)
hasil = b >= a
print(b,'>=',a,'=',hasil)
hasil = a >= 5
print(a,'>=',5,'=',hasil)

# Komparasi kurang dari sama dengan (<=)
print("==== KURANG DARI SAMA DENGAN (<=)")
hasil = a <= 8
print(a,'<=',8,'=',hasil)
hasil = b <= a
print(b,'<=',a,'=',hasil)
hasil = a <= 5
print(a,'<=',5,'=',hasil)

# Komparasi sama dengan (==)
print("==== SAMA DENGAN (==)")
hasil = a == 8
print(a,'==',8,'=',hasil)
hasil = b == a
print(b,'==',a,'=',hasil)
hasil = a == 5
print(a,'==',5,'=',hasil)

# Komparasi tidak sama dengan (!=)
print("==== TIDAK SAMA DENGAN (!=)")
hasil = a != 8
print(a,'!=',8,'=',hasil)
hasil = b != a
print(b,'!=',a,'=',hasil)
hasil = a != 5
print(a,'!=',5,'=',hasil)

# is adalah komparasi object identity
## Jika is dibandingkan dengan riteral(tanpa variable) akan error
x = 7 # ini adalah assignment membuat object
z = 7 # jika nilai sama meski variabel berbeda akan tetap berada di memori yang sama 

# Komparasi is sama dengan (is)
print("==== IS SAMA (is)")
print('nilai x =',x,'id',hex(id(x)))
print('nilai z =',z,'id',hex(id(z)))
hasil = x is z
print(x,'is',z,'=',hasil)

## Jika is not dibandingkan dengan riteral(tanpa variable) akan error
x = 7 # ini adalah assignment membuat object
z = 5 # jika nilai sama meski variabel berbeda akan tetap berada di memori yang sama 

# Komparasi is not sama dengan (is not)
print("==== IS NOT TiDAK SAMA (is not)")
print('nilai x =',x,'id',hex(id(x)))
print('nilai z =',z,'id',hex(id(z)))
hasil = x is not z
print(x,'is not',z,'=',hasil)