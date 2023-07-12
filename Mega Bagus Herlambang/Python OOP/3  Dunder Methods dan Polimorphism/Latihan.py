import os

isRun = True

class Orang:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
        self.uang = 0
    def info(self):
        print("Nama :",self.nama)
        print("Umur :",self.umur)
        print("Sisa Uang Anda Sebesar : $" + str(self.uang))

class Bank(Orang):
    def __init__(self,nama,umur):
        super().__init__(nama,umur)
    
    def tambahUang(self, tambah):
        self.uang += tambah
        print("Uang berhasil ditabung sebesar $" + str(tambah) + " Sehingga total tabungan anda sebesar $" + str(self.uang))

    def tarikUang(self, tarik):
        if self.uang > tarik:
            self.uang -= tarik
            print("Uang berhasil ditarik sebesar $" + str(tarik) + " Sehingga total tabungan anda sebesar $" + str(self.uang))
        else:
            print("Maaf Uang Anda Tidak Cukup | Uang Anda Tinggal Sebesar $" + str(self.uang))

def Milih(orang):
    global isRun
    print("========= BANK MANDIRI =========")
    print("1. Cek Data")
    print("2. Menabung Uang")
    print("3. Tarik Uang")
    try:
        inp = int(input("Masukan Pilihan Anda : "))
    except:
        print("Input Tidak Valid !!!")
    
    match inp:
        case 1: orang.info()
        case 2:
            try:
                tambah = int(input("Berapa Uang Yang Ingin Ditabung : "))
            except:
                print("Input Tidak Valid !!!")

            orang.tambahUang(tambah=tambah)
        case 3: 
            try:
                tarik = int(input("Berapa Nominal Uang Yang Ingin Ditarik : "))
            except:
                print("Input Tidak Valid !!!")

            orang.tarikUang(tarik=tarik)
    
    isOption = input("Memilih Lagi[?] (y/n) : ")
    if isOption in ("n","N"):
        isRun = False

# Main
nama = input("Masukan Nama anda : ")
try:
    umur = int(input("Masukan Umur Anda : "))
except:
    print("Input Tidak Valid !!!")

orang = Bank(nama=nama, umur=umur)

while isRun:
    os.system("cls")
    Milih(orang)