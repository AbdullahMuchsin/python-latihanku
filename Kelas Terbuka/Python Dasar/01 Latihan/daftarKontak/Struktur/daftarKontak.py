
def lihat_kontak(daftarKontak):

    for data in daftarKontak.keys():

        KEY = data

        NAME = daftarKontak[KEY]["nama"]
        TELEPON = daftarKontak[KEY]["telepon"]
        GMAIL = daftarKontak[KEY]["gmail"]
    
        print(f"""
    KEY           : {KEY}
    Nama          : {NAME}
    Nomor Telepon : {TELEPON}
    Gmail         : {GMAIL}
        """)
