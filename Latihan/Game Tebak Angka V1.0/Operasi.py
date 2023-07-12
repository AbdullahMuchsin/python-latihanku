import random as rand
class Game:
    def __init__(self,batas_bottom,batas_up):
        self.batas_bottom = batas_bottom
        self.batas_up = batas_up

    def rand(self,inp):
        self.number = rand.randint(self.batas_bottom,self.batas_up)
        self.salah(inp,self.number)

    def salah(self,inp,number):
        while inp != number:
            if inp > number:
                print("Angka salah, yang anda masukan terlalu besar")
            if inp < number:
                print("Angka salah, yang anda masukan terlalu kecil")
            try:
                inp = int(input("Coba Lagi dari 1-10 : "))
            except:
                print("Angka tidak valid")
        print("Tebakan anda Benar !!!")
    def mulai(self):
        try:
            self.inp = int(input("Tabak angka dari 1-10 : "))
        except:
            print("Angka tidak valid")
        self.rand(self.inp)
        