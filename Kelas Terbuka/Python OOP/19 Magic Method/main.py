class Mapel:
    def __init__(self,name,kkm): # __init__ ketika class hero di panggil makan __init__ fungsi ini yg akan dieksekusi
        self.name = name
        self.kkm = kkm
        self.__list_name = []
    
    def add_name(self,name):
        self.__list_name.append(name)

    def __len__(self):
        return len(self.__list_name)
    
    def __repr__(self): # Ini akan terpanggil jika print Object CLass yang kosong
        return f"Debug - Nama Mapel {self.name}:\n\tKKM : {self.kkm}"

    def __str__(self): # Ini akan terpanggil jika print Object CLass yang kosong
        return f"Nama Mapel {self.name}:\n\tKKM : {self.kkm}" # sama dengan repr tapi __str__ini dulu yang terpanggil

    def __add__(self,object): # Untuk operasi aritmatika
        return self.kkm + object.kkm
    
    @property # Kasih property agar hasil sesuai
    def __dict__(self):
        return f"Class ini memiliki nama dan nilai"
pelajaran1 = Mapel("Matematika",75)
pelajaran2 = Mapel("Fisika",75)

pelajaran1.add_name("Dani")
pelajaran1.add_name("Surudin")
pelajaran1.add_name("Kiko")

print(len(pelajaran1))


print(pelajaran1) # pakai repr()untuk memanggil __repr__
print(repr(pelajaran1)) # pakai repr()untuk memanggil __repr__
print("Jumblah kkm matematika dan fisika : " + str(pelajaran1 + pelajaran2)) #pelajaran1 sebagai self dan pelajaran2 sebagai object

print(pelajaran2.__dict__) # Kasih __dict__karena jadi variable
