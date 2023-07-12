from . import Operasi

def viewHapus():
    while True:
        baca_konsol()
        try:
            memilih = int(input("Pilih Nomor berapa Yang Anda Ingin Hapus : "))
        except:
            print("Input Tidak Valid")
        data = Operasi.Memilih(pilih = memilih)

        data_part = data.split("/")
        kunci = data_part[0]
        nama = data_part[1]
        waktu = data_part[2]
        penulis = data_part[3]
        tahun = data_part[4]

        print("Data Yang Anda Ingin")
        print("1. Nama    :",nama)
        print("2. Penulis :",penulis)
        print("3. Tahun   :",tahun)

        isOption = input("Apakah Anda Yakin[?] (y/n) : ")
        if isOption in ("y","Y"):
            Operasi.fileHapus(memilih)
            print("Data Berhasil diperbaharui")
            break

def viewPerbarui():
    while True:
        baca_konsol()
        try:
            memilih = int(input("Pilih Nomor Berapa yang Diperbarui : "))
        except:
            print("Input Tidak Valid")
        data = Operasi.Memilih(pilih = memilih)

        if data:
            break
        else: print("Input tidak valid")
    
    data_part = data.split("/")
    kunci = data_part[0]
    nama = data_part[1]
    waktu = data_part[2]
    penulis = data_part[3]
    tahun = data_part[4]

    print("Data sekarang")
    print("1. Nama    :",nama)
    print("2. Penulis :",penulis)
    print("3. Tahun   :",tahun)
    
    while True:
        isRubah = input("Pilih Nomor Yang Ingin Diperbarui : ")
        match isRubah:
            case "1": nama = input("Masukan Nama Baru : ")
            case "2": penulis = input("Masukan Penulis Baru : ")
            case "3":
                try:
                    tahun = int(input("Masukan Tahun Baru : "))
                except:
                    print("Input Tidak Valid")
        
        print("Data Sekarang")
        print("1. Nama    :",nama)
        print("2. Penulis :",penulis)
        print("3. Tahun   :",tahun)

        isOption = input("Apakah Data Sesuai[?] (y/n) : ")
        if isOption in ("y","Y"):
            Operasi.filePerbarui(memilih,kunci,nama,waktu,penulis,tahun)
            print("Data Berhasil diperbaharui")
            break
    
def viewNambah():
    nama = input("Masukan Nama Buku    : ")
    penulis = input("Masukan Penulis Buku : ")
    try:
        tahun = int(input("Masukan Tahun Buku   : "))
    except:
        print("Input Tidak Valid")
    
    Operasi.fileTambah(nama,penulis,tahun)
    baca_konsol()

def viewbaru():
    nama = input("Masukan Nama Buku    : ")
    penulis = input("Masukan Penulis Buku : ")
    try:
        tahun = int(input("Masukan Tahun Buku   : "))
    except:
        print("Input Tidak Valid")
    
    Operasi.fileBaru(nama,penulis,tahun)
    baca_konsol()

def baca_konsol():
    data_file = Operasi.Memilih()

    print("="*70)
    print(f"{'No':^2} | {'Nama':^25} | {'Penulis':^25} | {'Tahun':^5}")
    print("-"*70)
    for index,data in enumerate(data_file):
        data_part = data.split("/")
        
        nomor = index
        kunci = data_part[0]
        nama = data_part[1]
        waktu = data_part[2]
        penulis = data_part[3]
        tahun = data_part[4]

        print(f"{nomor + 1:^2} | {nama:25} | {penulis:25} | {tahun:^5}",end="")
    print("="*70)
