def cari_kontak(kunci, dataKontak):
    if kunci in dataKontak:

        print(f"""
    KEY           : {kunci}
    Nama          : {dataKontak[kunci]["nama"]}
    Nomor Telepon : {dataKontak[kunci]["telepon"]}
    Gmail         : {dataKontak[kunci]["gmail"]}
        """)
