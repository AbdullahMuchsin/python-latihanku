# BELAJAR OOP PYTHON CLASS ABSTRACT
'''
    Fungsi dari class abstract adalah agar tidak class tidak bisa di jadikan object sehingga
    berfungsi mencegah perubahan. untuk menggunakan class abstract terlebih dahulu import ABC,
    abstractmethod dari class abc singkatan dari Abstract base class.
    fungsi ABC berguna agar class tidak di jadikan object, dan fungsi dari abstractmethod
    agar fungsi yang inheritance akan membuat fungsi/method dari class utama sehingga jika
    kita membuat fungsi sesuatu yang memiliki fitur tersebut jika di inheritance tidak hilang
'''

from abc import ABC,abstractmethod

class Absen(ABC):

    @abstractmethod
    def name(self):
        pass
    @abstractmethod
    def kondisi(self):
        pass

class dataAbsen(Absen):
    def __init__(self,nama,absen):
        self.nama = nama
        self.absen = absen

    def name(self):
        print(self.nama)
    
    def kondisi(self):
        print(self.absen)

siswa1 = dataAbsen("Surudin","-")
siswa1.name()
siswa1.kondisi()

