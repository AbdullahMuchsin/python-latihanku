# Membuat game Tic tac toe
import random, os

# Atribute
papan = ["-","-","-",
         "-","-","-",
         "-","-","-"]

pemain = "X"
winner = None
gameRun = True

# Membuat papan permainan
def papanGame(papan):
    os.system("cls")
    print("GAME TIC TAC TOE")
    print("==========")
    print(papan[0] + " | " + papan[1] + " | " + papan[2])
    print("----------")
    print(papan[3] + " | " + papan[4] + " | " + papan[5])
    print("----------")
    print(papan[6] + " | " + papan[7] + " | " + papan[8])
    print("==========")

# Membuat input user
def userMilih(papan):
    while True:
        try:
            inp = int(input("Masukan pilihan dari 1-9 :"))
            if inp < 1 or inp > 9 or papan[inp - 1] != "-":
                inp = inp/0
            break
        except:
            print("Input tidak valid")

    if inp >= 1 and inp <= 9 and papan[inp-1] == "-":
        papan[inp - 1] = pemain
    else:
        print("Nomor sudah ada !!!")

# Cek Menang horizontal, vertikal, and diagonal
def cekHorizontal(papan):
    global winner
    if papan[0] == papan[1] == papan[2] and papan[1] != "-":
        winner = papan[1]
        return True
    elif papan[3] == papan[4] == papan[5] and papan[4] != "-":
        winner = papan[4]
        return True
    elif papan[6] == papan[7] == papan[8] and papan[7] != "-":
        winner = papan[7]
        return True

def cekVertika(papan):
    global winner
    if papan[0] == papan[3] == papan[6] and papan[3] != "-":
        winner = papan[3]
        return True
    elif papan[1] == papan[4] == papan[7] and papan[4] != "-":
        winner = papan[4]
        return True
    elif papan[2] == papan[5] == papan[8] and papan[5] != "-":
        winner = papan[5]
        return True

def cekDiag(papan):
    global winner
    if papan[0] == papan[4] == papan[8] and papan[4] != "-":
        winnner = papan[4]
        return True
    elif papan[2] == papan[4] == papan[6] and papan[4] != "-":
        winner = papan[4]
        return True

# Cek Winner
def cekWin():
    global gameRun
    if cekHorizontal(papan) or cekVertika(papan) or cekDiag(papan):
        papanGame(papan)
        print("Winner is " + str(winner))
        option()
        

# Cek seri
def cekSeri(papan):
    global gameRun
    if "-" not in papan:
        papanGame(papan)
        print("Game berakhir dengan seri")
        option()

# Kontrol
def kontrol():
    global pemain
    if pemain == "X":
        pemain = "O"
    else:
        pemain = "X"

# Kontrol Komputer
def Komputer(papan):
    while pemain == "O":
        rand = random.randint(0, 8)
        if papan[rand] == "-":
            papan[rand] = "O"
            kontrol()
        elif "-" not in papan:
            break

# Exit
def option():
    global gameRun, papan
    inp = input("Apakah Mau bermain Lagi(y/n) :")
    if inp in ("Y","y"):
        papan = ["-","-","-",
                "-","-","-",
                "-","-","-"]
        main()
    else:
        gameRun = False

# Main
def main():
    while gameRun:
        papanGame(papan)
        userMilih(papan)
        kontrol()
        Komputer(papan)
        cekWin()
        cekSeri(papan)

main()