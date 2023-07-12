from . import Operasi
def view_delete():
    while True:
        read_console()
        index_input = int(input("Masukan Nomor Yang ingin di Hapus : "))
        data_index = Operasi.read(index=index_input)
            
        data_break = data_index.split(",")

        presskey = data_break[0]
        datetime = data_break[1]
        nama = data_break[2]
        harga = data_break[3]
        tahun = data_break[4][:-1]

        print("Data Ini Yang Akan Di Hapus")
        print(f"Nama Barang  : {nama:.20}")
        print(f"Harga Barang : {harga:.20}")
        print(f"Tahun Barang : {tahun:.4}")

        isYakin = input("Apakah anda yakin ingin menghapus (y/n) : ")

        if isYakin == "Y" or isYakin == "y":
            Operasi.delete_item(index_input)
            break
        else:
            print("Nomor yang anda pilih error")

def view_update():
    while True:
        read_console()
        index_input = int(input("Masukan Nomor Yang ingin di Update : "))
        data_index = Operasi.read(index=index_input)

        if data_index:
            break
        else:
            print("Maaf Nomor yang anda masukan tidak valid")
            
    data_break = data_index.split(",")

    presskey = data_break[0]
    datetime = data_break[1]
    nama = data_break[2]
    harga = data_break[3]
    tahun = data_break[4][:-1]

    while True:
        print(f"1. Nama Barang  : {nama:.20}")
        print(f"2. Harga Barang : {harga:.20}")
        print(f"3. Tahun Barang : {tahun:4}")
        up_input = input("Pilih Yang Ingin Di Ubah [1][2][3] : ")
        match up_input:
            case "1": nama = input("Masukan Nama Baru : ")
            case "2":
                while True:
                    try:
                        harga = str(int(input("Masukan Harga Barang : ")))
                        break
                    except:
                        print("Masukan Angka")
            case "3":
                while True:
                    try:
                        tahun = int(input("Masukan Tahun Barang : "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Tahun tidak boleh kurang dari 4 dan lebih dari 4")
                    except:
                        print("Masukan Angka")

        Operasi.update_item(index_input,presskey,datetime,nama,harga,tahun)
        
        print(f"1. Nama Barang  : {nama:.20}")
        print(f"2. Harga Barang : {harga:.20}")
        print(f"3. Tahun Barang : {tahun:4}")
        isOption = input("Apakah data sudah benar (y/n) ? ")

        if isOption == "y" or isOption == "Y":
            break
def view_new():

    NAMA = input("Masukan Nama Barang : ")
    while True:
        try:
            HARGA = str(int(input("Masukan Harga Barang : ")))
            break
        except:
            print("Masukan Angka")
    while True:
        try:
            TAHUN = int(input("Masukan Tahun Barang : "))
            if len(str(TAHUN)) == 4:
                break
            else:
                print("Tahun tidak boleh kurang dari 4 dan lebih dari 4")
        except:
            print("Masukan Angka")
    
    Operasi.new_item(NAMA,HARGA,TAHUN)
    read_console()

def read_console():
    data = Operasi.read()

    INDEX = "Nomor"
    NAMA = "Nama"
    HARGA = "Harga"
    TAHUN = "Tahun"

    print("="*110)
    print(f"{INDEX:^5} | {NAMA:^40} | {HARGA:^30} | {TAHUN:^10}")
    print("-"*110)

    for index,data in enumerate(data):
        data_break = data.split(",")

        nomor = index

        presskey = data_break[0]
        datetime = data_break[1]
        nama = data_break[2]
        harga = data_break[3]
        tahun = data_break[4]

        print(f'{nomor + 1:^5} | {nama:.40} | {harga:.30} | {tahun:.10}',end="")

    print("="*110)