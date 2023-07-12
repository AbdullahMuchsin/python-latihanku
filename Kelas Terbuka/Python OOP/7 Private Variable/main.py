# BELAJAR PRIVATE VARIABLE OOP PYTHON
'''

    Cara membuat private variable yaitu dengan menulis __name (ada 2 garis bawah)
    Cara membuat protected variable yaitu dengan menulis _name (ada 1 garis bawah)

    itu di buat di variable or fungsi ok "tapi saat di dalam class atau method"
'''
class Hero:
    jumblah = 0
    __angka = 100
    _nama = "Ini protected"
    def __init__(self, name, health): 
        self.name = name
        self.health = health

        # Private
        self.__tahan = 100
        # Protected
        self._speed = "oke"

    # Varibale instance private (Tidak akan bisa diakses)
        self.__tahan = 100
    def __privasi(self):
        self.armor = 100
        print(self.armor)

    # Varibale instance protected (Prilakunya sama dengan publik tapi menandakan jangan di ubah)

    def _perlindungan(self):
        self.kecepatan = "oke"
        print(self.kecepatan)

agus = Hero("Agus", 100)

# Private di class
print(Hero.__dict__)
print(Hero.jumblah)
# print(Hero.__angka)
Hero.__angka = 232 # Akan membuat variable baru dengan nama private tapi bersifat bukan private
print(Hero.__dict__)
print(Hero.__angka) # Jadi bisa di akses dari variable baru tapi bukan yang private hanya copy han saya nama nya

# Protectec di class
Hero.jumblah = 718
print(Hero.jumblah)
print(Hero._nama)

# Private and Protected for Method :
# Varibale instance private (Tidak akan bisa diakses)
print(agus.__dict__) 
# print(agus.__tahan) # Tidak bisa di akses karena private
agus.__tahan = "sippp" # Akan membuat variable baru dengan nama private tapi bersifat bukan private
# print(agus.__tahan)
print(agus.__dict__)
print(agus.__tahan) # Jadi bisa di akses dari variable baru tapi bukan yang private hanya copy han saya nama nya

# Varibale instance protected (Prilakunya sama dengan publik tapi menandakan jangan di ubah)
print(agus.__dict__)
agus._speed = 100
print(agus._speed)
print(agus.__dict__)
agus._perlindungan()