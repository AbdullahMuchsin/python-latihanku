# BELAJAR OOP PYTHON GETTER AND SETTER

''''
    Di pyhton ada namanya property yaitu fungsinya seperti mengubah method menjadi perilakunya
    seperti varible dan juga ada property getter, setter and deleter
    getter berfungsi mengambil valiue
    setter berfungsi mngubah valiue
    delter berfungsi menghapus valiue

'''

class Hero:
    def __init__(self, name, health, speed):
        self.__name = name
        self.health = health
        self.__speed = speed 
        # self.info = "Nama : {}\nDarah : {}\nSpeed : {}".format(self.__name,self.health,self.speed)
        # Jika pakai varibale info di def __init__ hanya bisa berudah diawal jika akan mau di ubah 
        # salah satu variable maka saat di panggil info akan sama jadi jika ingin dapat beruba pakai method
        # yaitu dangan bantuan proprty

    @property
    def info(self):
        return "Nama : {}\nDarah : {}\nSpeed : {}".format(self.__name,self.health,self.__speed)

    @property # Dibuat fungsi dulu dengan property bergunaka untuk mendefinisikan / mengaktifkan
    def speed(self): # Baru bisa pakai property getter, setter, and deleter
        pass # dibuat pass aja atau kosongan
    
    @speed.getter # Jika varibale mau di buat property setter, getter, dan deleter makan varible tersebut harus di private
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, input):
        self.__speed = input

    @speed.deleter
    def speed(self):
        print("Armor di dalete")
        self.__speed = None


gunman = Hero("GunMan", 100, 15)
print(gunman.info)

# Property
gunman.health = 85
print(gunman.info)
print("ini Getter : " + str(gunman.speed))
print(gunman.__dict__) # Property di idct tidak ada karena bukan variable tapi memeliki sifat seperti variable

# Getter
# gunman.speed = 10 # Tidak bisa karena bersifat private atau encapsulasi jadi pakai setter jika ingin mengubah
print("ini Getter : " + str(gunman.speed))
print(gunman.info)
print(gunman.__dict__)
# Setter
gunman.speed = 10 # (angka 10 itu merupakan input dari argumen input di method porperty speed) # Untuk pengubahan penulisan setter propety sama dengan variable
print("ini Setter : " + str(gunman.speed))
print(gunman.info)
print(gunman.__dict__) # setiap kali di setter makan akan di dict pun nilai nya akan berubah
# Deleter
del gunman.speed # Pakai del untuk memanggil prperty deleter
print(gunman.info)
print(gunman.__dict__) # setiap kali di setter makan akan di dict pun nilai nya akan berubah
