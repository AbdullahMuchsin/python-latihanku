## LATIHAN PERULANGAN

# 1. Menggunkan for
sisi = 10
bi1 = 1

print("="*5 + "MULAI PROGRAM 1" + 5*"=")
for i in range(sisi):
    print("*"*bi1)
    bi1 += 1
print("="*5 + "AKHIR PROGRAM" + 5*"=" + "\n")


# 2. Menggunakan while
print("="*5 + "MULAI PROGRAM 2" + 5*"=")
bi2 = 1
while True:
    print("*"*bi2)
    bi2 += 1
    if bi2 > sisi:
        break
print("="*5 + "AKHIR PROGRAM" + 5*"=" + "\n")

# 3. Menggunakan while genap
print("="*5 + "MULAI PROGRAM 3" + 5*"=")
bi2 = 1
while True:
    if bi2 == 1:
        print("+"*bi2)
        bi2 += 1
    elif (bi2 % 2) != True:
        print("+"*bi2)
        bi2 += 1
    else:
        bi2 += 1
        continue
    if bi2 > sisi:
        break
print("="*5 + "AKHIR PROGRAM" + 5*"=" + "\n")

# 4. Menggunakan while Segitiga siku-siku
print("="*5 + "MULAI PROGRAM 4" + 5*"=")
st = (int(sisi/2) - 1)
bi2 = 1
while True:
    if (bi2 % 2) != True:
        print(" "*st + "*"*bi2)
        st -= 1
        bi2 += 1
    else:
        bi2 += 1
        continue
    if bi2 > sisi:
        break
print("="*5 + "AKHIR PROGRAM" + 5*"=" + "\n")

# 5. Menggunakan while ganjil
print("="*5 + "MULAI PROGRAM 5" + 5*"=")
bi2 = 1
while True:
    if (bi2 % 2):
        print("+"*bi2)
        bi2 += 1
    else:
        bi2 += 1
        continue
    if bi2 > sisi:
        break
print("="*5 + "AKHIR PROGRAM" + 5*"=" + "\n")

# 6. Menggunakan while Segitiga siku-siku
print("="*5 + "MULAI PROGRAM 6" + 5*"=")
st = int(sisi/2)
bi2 = 1
while True:
    if (bi2 % 2):
        print(" "*st + "*"*bi2)
        st -= 1
        bi2 += 1
    else:
        bi2 += 1
        continue
    if bi2 > sisi:
        break
print("="*5 + "AKHIR PROGRAM" + 5*"=" + "\n")

# 7. Menggunakan while Segitiga siku-siku genap-ganjil
print("="*5 + "MULAI PROGRAM 7" + 5*"=")
st1 = int(sisi/2)
st2 = int((sisi/2) - 1)
bi2 = 1
while sisi < 15:
        if (bi2 % 2):
            print(" "*st1 + "+"*bi2)
            bi2 += 1
        if (bi2 % 2) != True:
            print(" "*st2 + "+"*bi2)
            st1 -= 1
            st2 -= 1
            bi2 += 1
        if bi2 > sisi:
            break
print("="*5 + "AKHIR PROGRAM" + 5*"=" + "\n")

# 6. Menggunakan while ketupat
print("="*5 + "MULAI PROGRAM 8" + 5*"=")
sisi = 9
st = int(sisi/2)
st1 = st + 1
st2 = 3
bi2 = 1
while True:

    if (bi2 % 2) & (bi2 < ((sisi/2) + 1)):
        print(" "*st + "+"*bi2)
        st -= 1
        bi2 += 1
    elif (bi2 % 2) & (bi2 > (sisi/2)):
        if sisi % 2:
            print(" "*st2 + "+"*st1)
            st2 += 1
            st1 -= 1
            bi2 += 1
        elif (sisi % 2) != True:
            print(" "*st2 + "+"*st1)
            st2 += 1
            st1 -= 1
            bi2 += 1
    else:
        bi2 += 1
        if(bi2 > ((sisi/2) )):
            st1 -= 1
        continue
    if bi2 > sisi:
        break
print("="*5 + "AKHIR PROGRAM" + 5*"=" + "\n")
