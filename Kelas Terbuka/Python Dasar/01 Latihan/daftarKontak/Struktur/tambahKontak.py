import string
import random

tamplate_kontak = {
    "nama" : "nama",
    "telepon" : 11111,
    "gmail" : "gmail"
}

def nambah_kontak(listKontak):
    global dataKontak
    data = dict.fromkeys(tamplate_kontak.keys())

    data["nama"] = input("Masukan Nama Anda : ")
    data["telepon"] = int(input("Masukan Nomor Telepon Anda : "))
    data["gmail"] = input("Masukan Gmail Anda : ")

    KEY = "".join(random.choice(string.ascii_uppercase) for i in range(4))
    
    return listKontak.update({KEY:data})
