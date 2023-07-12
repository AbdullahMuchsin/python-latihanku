# BELAJAR MENGGUNAKAN __INIT__

from sains import *
from sains import fisika
from sains import matematika
from sains.matematika.dasar import add
from sains.fisika.berat import berat1


hasil_kurang = matematika.dasar.kurang(242,525,2)
print(hasil_kurang)

hasil_berat = fisika.berat.berat1(24,4)
print(hasil_berat)

hasil_berat = berat1(2,4)
print(hasil_berat)


hasil_tambah = add(1,2,3,4,5,6,7,8)
print(hasil_tambah)

hasil_kurang = matematika.dasar.kurang(1,2,3,4,5,6,7,8)
print(hasil_kurang)

hasil_pangkat = matematika.pangkat.pangkat1(5)
print(f"{hasil_pangkat(2)}")

hasil_berat = fisika.berat.berat1(7,8)
print(hasil_berat)

# from sains import * # Pakai bintang tidak direkomendasikan

# hasil_kurang = matematika.dasar.kurang(242,525,2)
# print(hasil_kurang)

# hasil_berat = fisika.berat.berat1(24,4)
# print(hasil_berat)