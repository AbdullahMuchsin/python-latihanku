class bangunRuang:
    def __init__(self,p=0,l=0,t=0,s=0):
        self.panjang = p
        self.lebar = l
        self.tinggi = t
        self.sisi = s
        self.pi = 22/7

class Kubus(bangunRuang):
    def __init__(self,s):
        super().__init__(s)
        self.__sisi = s
    
    def volumeKubus(self):
        self.volKubus = self.__sisi**3
        return self.volKubus
    
    def luasPermukaan(self):
        self.luasPermu = 6 * (self.__sisi ** 2)
        return self.luasPermu

    def kelilingKubus(self):
        self.kelKubus = 12 * self.__sisi
        return self.kelKubus

    def luasSalahSatuKubus(self):
        self.luasStuKubus = self.__sisi * self.__sisi
        return self.luasStuKubus
    
    def info(self):
        print(f"""+=============KUBUS=============+
| Volume Kubus            : {self.volumeKubus()}
| Luas Permukaan          : {self.luasPermukaan()}
| Keliling Kubus          : {self.kelilingKubus()}
| Luas Salah Satu Kubus   : {self.luasSalahSatuKubus()}
+===============================+""")

class Balok(bangunRuang):
    def __init__(self,p,l,t):
        super().__init__(p,l,t)
        self.__panjang = p
        self.__lebar = l
        self.__tinggi = t

    
    def volumeBalok(self):
        self.volBalok = (self.__panjang * self.__lebar * self.__tinggi)
        return self.volBalok
    
    def luasPermukaan(self):
        self.__pl = self.__panjang * self.__lebar
        self.__lt = self.__lebar * self.__tinggi
        self.__pt = self.__panjang * self.__tinggi
        return 2 * (self.__pl + self.__lt + self.__pt)

    def kelilingBalok(self):
        return 4 * (self.__panjang + self.__lebar + self.__tinggi)
    
    def info(self):
        print(f"""+=============BALOK=============+
| Volume Kubus            : {self.volumeBalok()}
| Luas Permukaan          : {self.luasPermukaan()}
| Keliling Kubus          : {self.kelilingBalok()}
+===============================+""")
