# BELAJAR MENENGGUNKAN __MAIN__

# Main adalah top level code enviroment

# nilai __name__ = __main__ Jika program dijalankan pada file utama (Bukan dari import)
print(f"Nilai __main__ adalah {__name__}")

def tambah(angka_satu:int, angka_dua:int)-> int:
    angka_1 = angka_satu
    angka_2 = angka_dua

    hasil = angka_1 + angka_2
    return  hasil

# __main__ fungsi di Main.py

if __name__ == "__main__": # Jadi jika dari program utama makan akan berjalan
    HASIL = tambah(5,7)
    print(f"Hasil dari perhitungan tersebut adalah {HASIL}")

# __main__ import dari fungsi
import fungsi

print(f"Nilai __main__ adalah '{fungsi.__name__}'") # hasil __name__ utama dengan import berbeda

# __main__ package
import package # jika di run di terminal (python -m package) maka akan ditampilkan isi dari __main__ di package (penjelasan fungsi ada di file __main__.py)

hasil_package_tambah = fungsi.tambah(2,4)
print(f"Hasil dari package_tambah adalah {hasil_package_tambah}")





