# BELAJAR OOP PYTHON CLASS ABSTRACT DAN DECORATOR
from abc import ABC,abstractmethod

class Absen(ABC):
    def __init__(self,name,kondisi):
        self.nama = name
        self.kondisi = kondisi

    @property
    @abstractmethod
    def nama(self):
        pass

    @property
    @abstractmethod
    def kondisi(self):
        pass

class info(Absen):

    def info(self):
        print(f"""Nama    : {self.__name}
Kondisi : {self.__kondisi}
        """)

    @Absen.nama.setter
    def nama(self,input):
        self.__name = input
    
    @nama.getter
    def nama(self):
        return self.__name
    
    @Absen.kondisi.getter
    def kondisi(self):
        return self.__kondisi
    
    @kondisi.setter
    def kondisi(self,input):
        self.__kondisi = input
    

    
siswa1 = info("Surudin","A")
siswa2 = info("Marsudin","-")

siswa1.info()
siswa2.info()