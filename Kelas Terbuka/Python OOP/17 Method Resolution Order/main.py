# BELAJAR OOP PYTHON METHOD RESOLUTION ORDER

'''
    Method Resolution Order adalah urutan jika siapa yang dieksekusi dahulu
    jika ada fungsi yang sama pada multiple inheritance dapat juga dengan 
    help(nama class)
'''
class A:
    def show(self):
        print("Ini adalah class A")
    
class B:
    def show(self):
        print("Ini adalah class B")

class C(B,A):
    def show(self):
        print("Ini adalah class C")

c = C()
c.show()
# help(c)