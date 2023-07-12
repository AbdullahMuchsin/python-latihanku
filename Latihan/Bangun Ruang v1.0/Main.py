import Operasi, os

isOption = True
while isOption:
    name_os = os.name
    print(name_os)
    match name_os:
        case "nt": os.system("cls")

    try:
        p = int(input("Masukan Panjang : "))
        l = int(input("Masukan Lebar : "))
        t = int(input("Masukan Tinggi : "))
        s = int(input("Masukan Sisi (Untuk Kubus) : "))
    except:
        print("Angka tidak valid")

    kubus = Operasi.Kubus(s=s)
    kubus.info()

    balok = Operasi.Balok(p=p,l=l,t=t)
    balok.info()

    isOption = input("Apakah selesai (y/n) ? ")
    if isOption == "y" or isOption == "Y":
        isOption = False