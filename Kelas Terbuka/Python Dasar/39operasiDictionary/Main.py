## BELAJAR OPERATOR DICTIONARY

dict_data = {
    'Sur' : 'Surudin',
    'Jer' : 'Jarjit',
    'Def' : 'Dani'
}
print(dict_data)

# Menghitung isi dictionary
p_dict = len(dict_data)
print(f"Panjang data dict adalah : {p_dict}")

# Memeriksa atau cek data dictionary
KEY = "Sur"
KEY2 = 'Sup'

CEKDATA = KEY in dict_data
CEKDATA2 = KEY2 in dict_data

print(f"Data {KEY} di dalam dict_data adalah : {CEKDATA}")
print(f"Data {KEY2} di dalam dict_data adalah : {CEKDATA}")

# Mengakses value (Read) dengan get
print(f"Data ke-> 2 adalah : {dict_data['Jer']}") # Pakai tanda petik sama yang di dictionary
print(f"Data ke-> ? adalah : {dict_data.get('Ser')}") # Jika pakai get kalau tidak ada jadi none
print(f"Data ke-> ? adalah : {dict_data.get('Sup','Data Tidak Ditemukan')}")

# Mengubah data dan Add data dictionary
dict_data['Jer'] = 'Jerry'
print(dict_data)
dict_data['Mat'] = 'Mamat'
print(dict_data)

dict_data.update({'Sur' : 'Marsudin', 'def' : 'Defa'})
print(dict_data)
dict_data.update({'Bay' : 'Bayu'})
print(dict_data)

# Cara menghapus data pada dictionary

del dict_data['Bay']
print(dict_data)