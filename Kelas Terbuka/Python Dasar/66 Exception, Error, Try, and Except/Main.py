# Membuat program exception sendiri dengan isinstance and raise

from numbers import Number

def tambah(a,b):
    if not isinstance(a,Number) or not isinstance(b,Number):
        raise "Masukan angka semua"
    return a+b

hasil = tambah(3,2)
hasil2 = tambah("e",3)
print(hasil2)
print(hasil) # jika pakai isinstance raise jika error diawal program maka program raise dijalankan
             # Program berikutnya tidak dijalankan atau berhenti