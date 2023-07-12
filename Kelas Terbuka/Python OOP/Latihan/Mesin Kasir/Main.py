# MEMBUAT MESIN KASIR
import os
import CRUD as CRUD

if __name__ == "__main__":
    os_clear = os.name
    print(os_clear)
    match os_clear:
        case "ponix" : os.system("clear")
        case "nt": os.system("cls")

    print("SELAMAT DATANG")
    print(" DI TOKO JAYA ")
    print("===============")
    
    CRUD.cekIn()

    isRunning = True
    while isRunning:
        os_clear = os.name
        print(os_clear)
        match os_clear:
            case "ponix" : os.system("clear")
            case "nt": os.system("cls")

        print("SELAMAT DATANG")
        print(" DI TOKO JAYA ")
        print("===============")

        print("1. Melihat daftar barang")
        print("2. Manambahkan daftar barang")
        print("3. Mengubah daftar barang")
        print("4. Menghapus daftar barang")
        isSelect = input("Pilih : ")
        os_clear = os.name
        match os_clear:
            case "ponix" : os.system("clear")
            case "nt": os.system("cls")
        match isSelect:
            case "1": CRUD.read_console()
            case "2": CRUD.view_new()
            case "3": CRUD.view_update()
            case "4": CRUD.view_delete()

        isOption = input("Apakah sudah selesai (y/n) : ")
        if isOption == "y" or isOption == "Y":
            isRunning = False

    print("Program Selesai")