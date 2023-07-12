# LATIHAN OPERASI LOGIKA
# not, or, and, xor

# NOT (berfungsi mengubah menjadi kebalikan)
print("====NOT====")
a = True
c = not a
print("Data a :",a)
print("---------------NOT")
print("data a :",c)

# OR (Jika salah satu true maka hasilnya true)
print("====OR====")
a = True
b = True
x = a or b
print(a,' OR',b,' =',x)
a = True
b = False
x = a or b
print(a,' OR',b,'=',x)
a = False
b = True
x = a or b
print(a,'OR',b,' =',x)
a = False
b = False
x = a or b
print(a,'OR',b,'=',x)

# AND (Jika salah satu false maka hasilnya false)
print("====AND====")
a = True
b = True
x = a and b
print(a,' AND',b,' =',x)
a = True
b = False
x = a and b
print(a,' AND',b,'=',x)
a = False
b = True
x = a and b
print(a,'AND',b,' =',x)
a = False
b = False
x = a and b
print(a,'AND',b,'=',x)

# XOR (jika berbeda true dan sebaliknya)
print("====XOR====")
a = True
b = True
x = a ^ b
print(a,' XOR',b,' =',x)
a = True
b = False
x = a ^ b
print(a,' XOR',b,'=',x)
a = False
b = True
x = a ^ b
print(a,'XOR',b,' =',x)
a = False
b = False
x = a ^ b
print(a,'XOR',b,'=',x)
