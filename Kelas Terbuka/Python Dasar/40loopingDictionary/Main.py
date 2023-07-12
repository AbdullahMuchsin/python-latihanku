## BELAJAR LOOPING DICTIONARY
kode = {
    's1':100,
    's2':200,
    'd1':1000,
    'd2':2000,
    'f1':10000,
    "f2":20000
}
# Tanpa atribut
print(kode)
for kd in kode: # Yang diakses adalah key nya
    print(kd)

# Menggunakan keys untuk key
ky = kode.keys()
print(ky)

for k in kode.keys():
    print(k)

# Menggunakan values untuk value (Nilai)
val = kode.values()
print(val)

for vl in val:
    print(vl)

# Menggunknan items untuk key and value
itm = kode.items()
print(itm)

for its in kode.items():
    print(its)

# Menggunkan items agar dapat seperti enumerate
for key,value in kode.items():
    print(f"Key : {key}, Value : {value}")
