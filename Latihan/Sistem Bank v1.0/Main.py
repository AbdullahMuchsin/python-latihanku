import os

class Person():
    def __init__(self,nama,umur,gender):
        self.nama = nama
        self.umur = umur
        self.gender = gender
    
    def show(self):
        print("Nama   :",self.nama)
        print("Umur   :",self.umur)
        print("Gender :",self.gender)

class Bank(Person):
    def __init__(self,nama,umur,gender):
        super().__init__(nama,umur,gender)
        self.uang = 0
    
    def tambahUang(self,tambah):
        self.uang += tambah
        print("Tabungan anda sekarang sebesar $", self.uang)

    def tarikUang(self,tarik):
        if tarik <= self.uang:
            self.uang -= tarik
            print("Tabungan anda sekarang sebesar $", self.uang)
        else: print("Maaf uang anda tidak cukup | Uang anda tersisa $",self.uang)

    def show_bank(self):
        self.show()
        print("Uang anda tersisa $",self.uang)

def main(person):
    while True:
        os.system("cls")
        print(" BANK TERKINI ".center(25,"="))
        print("1. Lihat Data")
        print("2. Menabung")
        print("3. Tarik Uang")
        isSelect = input("Pilih Nomor Berapa : ")

        match isSelect:
            case "1": person.show_bank()
            case "2": 
                try:
                    tambah = int(input("Masukan nominal uang yang ingin di tabung : "))
                except:
                    print("Input tidak valid")
                person.tambahUang(tambah)
            case "3":
                try:
                    tarik = int(input("Masukan nominal uang yang ingin anda tarik : "))
                except:
                    print("Input tidak valid")
                person.tarikUang(tarik)
        isOption = input("[?]Lagi (y/n) : ")
        if isOption in ("n","N"):
            break
if __name__ == '__main__':
    muchsin = Bank("Muchsin",18,"Laki-Laki")
    main(muchsin)
    print("Program Berakhir")