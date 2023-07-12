print("Mulai".center(20,"="))

# Bin
angka = 14
print(f"{angka:#b}") # Menggunkan 0b
print(f"{angka:b}") # Tanpa menggunakan 0b

print("Sama saja dengan diatas tapi dengan code berbeda")
angka2 = format(14,'#b') # Menggunkan 0b
print(angka2)
angka2 = format(14,'b') # Tanpa menggunakan 0b
print(angka2)

eb = bool(' ')
print(eb)

tes = (print("index " + str(i)) for i in range(2))
print(str(tes))

hasil = 8,4,4

def f_filter(nilai):
    return nilai > 30

ISI = [1,3,41,4,57,46,3,575,25,325,2]
print(list(filter(f_filter,ISI)))

ISI.sort(key = lambda x : (x))
print(f"{ISI}")

ISI.reverse()
print(f"{ISI}")
