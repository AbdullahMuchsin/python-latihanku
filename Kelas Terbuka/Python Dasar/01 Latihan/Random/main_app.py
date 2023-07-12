class aritmatika:
    x = 10
    y = 5

    tambah = x + y
    kurang = x - y
    kali = x * y
    bagi = x / y

print(aritmatika.tambah)
print(aritmatika.kurang)

array = ["nama", "huu", "kurus", "Penggaris"]

array.sort(key = lambda arcy: len(arcy))

data = len(array)
data1 = array.count("huu")
print(data1)

isBool = True
angka = -5
while isBool:
    for i in range(1,21):
        print(i)
        angka = angka + i
        if angka > 15:
                isBool = False
