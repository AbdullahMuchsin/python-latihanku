import os
import CRUD as CRUD

if __name__ == '__main__':
    nameOs = os.name
    match nameOs:
        case "nt": os.system("cls")
        case "posix": os.system("clear")

    print("PERPUSTAKAAN".center(25,"="))
    print("SELAMAT DATANG".center(25,"-"))

    CRUD.cek()
            
    while True:
        nameOs = os.name
        match nameOs:
            case "nt": os.system("cls")
            case "posix": os.system("clear")

        print("PERPUSTAKAAN".center(25,"="))
        print("SELAMAT DATANG".center(25,"-"))
        print("1. Lihat Daftar")
        print("2. Menambhakan Daftar List")
        print("3. Perbarui daftar List")
        print("4. Menghapus daftar List")
        print("5. Keluar")
        isSelect = input("Pilih Nomor : ")

        match isSelect:
            case "1": CRUD.baca_konsol()
            case "2": CRUD.viewNambah()
            case "3": CRUD.viewPerbarui()
            case "4": CRUD.viewHapus()
            case "5": break
            
        isOption = input("[?]Lagi (y/n) : ")
        if isOption in ("n","N"):
            break
    print("Program Berakhir".upper().center(25,"="))