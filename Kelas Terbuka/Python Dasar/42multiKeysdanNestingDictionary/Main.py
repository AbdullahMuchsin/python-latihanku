## BELAJAR MULTI KEYS AND NESTING DICTIONARY

import datetime

siswa1 = {
    'nama' : 'Surudin Marsudin',
    'nim' : '1102402001',
    'lahir' : datetime.datetime(2007,4,24),
    'kota' : 'Surakarta',
    'kelas' : '10 IPA'
}
siswa2 = {
    'nama' : 'Gilang Surya',
    'nim' : '1102402002',
    'lahir' : datetime.datetime(2004,7,14),
    'kota' : 'Medan',
    'kelas' : '12 IPS'
}
siswa3 = {
    'nama' : 'Salim Andana',
    'nim' : '1102402003',
    'lahir' : datetime.datetime(2006,6,22),
    'kota' : 'Medan',
    'kelas' : '11 IPA'
}

dataSiswa = {
    'SISWA001' : siswa1,
    'SISWA002' : siswa2,
    'SISWA003' : siswa3
}

print(f"{'KEY':<9} {'NAMA':^17} {'NIM':^11} {'LAHIR':^8} {'KOTA':^9} {'KELAS':^6}")
for dataS in dataSiswa.keys():
    KEY = dataS

    NAMA = dataSiswa[KEY]['nama']
    NIM = dataSiswa[KEY]['nim']
    LAHIR = dataSiswa[KEY]['lahir'].strftime("%x")
    KOTA = dataSiswa[KEY]['kota']
    KELAS = dataSiswa[KEY]['kelas']

    print(f"{KEY:<9} {NAMA:^17} {NIM:^11} {LAHIR:^8} {KOTA:^9} {KELAS:^6}")



