# MEMBUAT PROJECT DATABASE PERPUSTAKAAN

import os
import CRUD as CRUD
if __name__ == "__main__":
    nama_clear_os = os.name

    match nama_clear_os:
        case "nt" : os.system("cls")
        case "posix" : os.system("clear")

    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("==========================")

    # Cek database itu ada atau tidak
    CRUD.init_console()
    
    while (True):
        match nama_clear_os:
            case "nt" : os.system("cls")
            case "posix" : os.system("clear")
        
        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print("==========================")

        print("1. Read Data")
        print("2. Add Data")
        print("3. Update Data")
        print("4. Delete Data\n")

        isSelect = input("Masukan opsi : ")

        match isSelect:
            case "1" : CRUD.read_console()
            case "2" : CRUD.create_console()
            case "3" : CRUD.update_console()
            case "4" : CRUD.delete_console()

        isOption = input("Apakah selesai (y/n) ? ")
        if isOption == "y" or isOption == "Y":
            break
    
    print("PROGRAM BERAKHIR".center(25,"="))

