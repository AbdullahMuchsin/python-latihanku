import random,os

# Atribute
randomSelelct = ['Batu','Kertas','Gunting']
scorWin = 0

# Header
def header():
    print(" [B]atu [K]ertas [G]unting ".center(35,"="))
    print("YOU WIN : {}".format(scorWin))

def main():
    while True:
        # Intro
        global scorWin
        header()
        print("START GAME")
        isRun = input("Klik (N) Untuk Berhenti Bermain ^_^ : " ).lower()
        if isRun == 'n':
            break

        # Main
        os.system("cls")
        header()
        isSelect = input("Pilih [B]atu [K]ertas [G]unting : ").lower()
        isRand = random.randint(0,2)

        if isSelect[0] == randomSelelct[isRand][0].lower():
            print("Lawan memilih {} Hasilnya Seri".format(randomSelelct[isRand]))
            continue
        elif isSelect[0] == 'g' and randomSelelct[isRand] == 'Kertas':
            print("Lawan Memilih {}".format(randomSelelct[isRand]))
            print("Horee Kamu Menang ^0^")
            scorWin += 1
        elif isSelect[0] == 'b' and randomSelelct[isRand] == 'Gunting':
            print("Lawan Memilih {}".format(randomSelelct[isRand]))
            print("Horee Kamu Menang ^0^")
            scorWin += 1
        elif isSelect[0] == 'k' and randomSelelct[isRand] == 'Batu':
            print("Lawan Memilih {}".format(randomSelelct[isRand]))
            print("Horee Kamu Menang ^0^")
            scorWin += 1
        else:
            print("Lawan Memilih {}".format(randomSelelct[isRand]))
            print("kamu Kalah Huhuhu T_T")
            scorWin -= 1
# Run
if __name__ == '__main__':
    main()