# BELAJAR OOP PYTHON YAITU CLASSMETHOD AND STATICMETHOD

'''
        Variable private di class variable tidak akan bisa di akses lawat fungsi object
    Jadi jika ingin mengakses variable tersebut maka pakai fungsi class atau bisa dengan 
    "classmethod or staticmethod" fungsi nya adalah menghubungkan dengan class agar bisa akses
    apa yang ada dalam class tersebut. 
        Perbedaan classmethod dan staticmethod adalah jika menambahkan classmethod maka akan
    dapat menambahkan argumen seperti self di fungsi, jika menambahkan staticmethod maka tidak
    akan bisa menambahkan argumen seperti self di fungsi

'''

class Math:
    # Class variables
    __hasil = 0

    def __init__(self,name,angka):
        self.name = name
        self.angka = angka
        Math.__hasil += angka
    
    # Method ini berlaku untuk object
    def hasilClass(self):
        return Math.__hasil
    
    # # Method ini tidak berlaku untuk object tapi berlaku untuk class
    # def hasilClass(): 
    #     return Math.__hasil
    
    # classmethod
    @classmethod
    def classHasil(matematika):
        return matematika.__hasil
    
    # staticmethod
    @staticmethod
    def classHasil1():
        return Math.__hasil

object1 = Math("Tambah",12)
obejct2 = Math("Tambah2",12)

print(obejct2.hasilClass()) # Ternyata diversi sekarang bisa di akses

# classmethod
print(object1.classHasil())
print(Math.classHasil())

# staticmehtod
print(object1.classHasil1())
print(Math.classHasil1())

