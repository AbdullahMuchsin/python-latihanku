import random,os
class Bahan:
    isTrue = True
    def __init__(self,user):
        self.user = user
        self.win = None
    def papan_game(self):
        os.system("cls")
        print("GAME TIC TAC TOE")
        print("=========")
        print(self.papan[0] + " | " + self.papan[1] + " | " + self.papan[2])
        print(self.papan[3] + " | " + self.papan[4] + " | " + self.papan[5])
        print(self.papan[6] + " | " + self.papan[7] + " | " + self.papan[8])
        print("=========")

class Tictactoe(Bahan):
    papan = ["-","-","-","-","-","-","-","-","-"]
    def __init__(self, user = "X"):
        super().__init__(user)
    def input_game(self):
        while True:
            try:
                self.inp = int(input("Pilih Nomor 1-9 : "))
                if self.inp < 1 or self.inp > 9:
                    self.inp /= 0
            except:
                print("Input Tidak Valid")
        
            if self.inp >= 1 and self.inp <= 9 and self.papan[self.inp - 1] == "-":
                self.papan[self.inp - 1] = self.user
                break
            else:
                print("Error Game !!!")
    def komputer_input(self):
        if self.user == "X" and "-" in self.papan:
            self.user = "O"
            while True:
                self.inp = random.randint(0,8)
                if self.inp > 0 and self.inp < 9 and self.papan[self.inp] == "-":
                    self.papan[self.inp] = self.user
                    self.user = "X"
                    break
        else:
            self.user = "X"
    def cekHorizontal(self):
        if self.papan[0] == self.papan[1] == self.papan[2] and self.papan[1] != "-":
            self.win = self.papan[1]
            return True
        elif self.papan[3] == self.papan[4] == self.papan[5] and self.papan[4] != "-":
            self.win = self.papan[4]
            return True
        elif self.papan[6] == self.papan[7] == self.papan[8] and self.papan[7] != "-":
            self.win = self.papan[7]
            return True
    def cekVertika(self):
        if self.papan[0] == self.papan[3] == self.papan[6] and self.papan[3] != "-":
            self.win = self.papan[3]
            return True
        elif self.papan[1] == self.papan[4] == self.papan[7] and self.papan[4] != "-":
            self.win = self.papan[4]
            return True
        elif self.papan[2] == self.papan[5] == self.papan[8] and self.papan[5] != "-":
            self.win = self.papan[5]
            return True
    def cekDiag(self):
        if self.papan[0] == self.papan[4] == self.papan[8] and self.papan[4] != "-":
            self.win = self.papan[4]
            return True
        elif self.papan[2] == self.papan[4] == self.papan[6] and self.papan[4] != "-":
            self.win = self.papan[4]
            return True
    def cekWin(self):
        if self.cekHorizontal() or self.cekVertika() or self.cekDiag():
            self.papan_game()
            print("Winner is " + str(self.win))
            self.option()
            self.papan = ["-","-","-","-","-","-","-","-","-"]
            os.system("cls")
    def seri(self):
        if "-" not in self.papan:
            self.papan_game()
            print("Hasilnya Seri")
            self.option()
            self.papan = ["-","-","-","-","-","-","-","-","-"]
            os.system("cls")
    def option(self):
        inp = input("Apakah mau main lagi[?] (y/n) :")
        if inp in ("n","N"):
            self.isTrue = False

data = Tictactoe()
while data.isTrue:
    data.papan_game()
    data.input_game()
    data.komputer_input()
    data.cekWin()
    data.seri()
