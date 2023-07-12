# BELAJAR OOP PYTHON MULTIPLE INHERITANCE

class A:
    def showA(self):
        print("Ini class A")

class B:
    def showB(self):
        print("Ini class B")

class C(A,B):
    def __init__(self):
        super().showA()
        super().showB()

ab = C()
# ab.showA()
# ab.showB()