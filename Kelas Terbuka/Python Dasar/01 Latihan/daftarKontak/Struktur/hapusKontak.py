def daftar_kunci(daftarKontak):

    print("DAFTAR KEY")
    
    for data in daftarKontak.keys():

        KEY = data
        print(f"KEY  : {KEY}")

def hapus_kontak(dataKontak,keys):
    del dataKontak[keys]