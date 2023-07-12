# BELAJAR OOP PYTHON DIAMOND PROBLEM

class A:
    def show(self):
        print("Ini adalah class A")
class B(A):
    def show(self):
        print("Ini adalah class B")
class C(A):
    def show(self):
        print("Ini adalah class C")
class D(B,C):
    pass
    # def show(self):
    #     print("Ini adalah class D")

d = D()
# help(d) # Untuk melihat urutan 
d.show()