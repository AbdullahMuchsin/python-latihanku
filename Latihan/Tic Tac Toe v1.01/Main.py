import os,random

hasil = 0
base  = ["-","-","-",
        "-","-","-",
        "-","-","-","-"]
base_x =f"GAME TIC TAC TOE\n=============\n| - | - | - |\n| - | - | - |\n| - | - | - |\n============="

# Break
isRuning = True
def isRun():
    global base
    isOption = input("[?]Apakah Mau bermain lagi (y/n): ")
    os.system("cls")
    if isOption in ("n","N"):
        return False
    else:
        return True

# Header
os.system("cls")
while isRuning:

    # Input
    print(base_x)

    print("Score Kamu :",hasil) 
    try:
        select = int(input("Pilih Nomor[1-9] Berapa : "))
        if select >= 10 or select <= 0:
            x = select/0
    except:
        os.system("cls")
        continue

    while True:
        select_rand = random.randint(0,10)
        if select_rand == 10:
            for i in base:
                if i == "-":
                    tes -= 1
            if tes == 2:
                break
            continue
        elif select != select_rand and base[select_rand - 1] == "-":
            break

    os.system("cls")

# Seleksi
    if base[select_rand - 1] == "-" and base[select - 1] == "-" and select != select_rand:
        base[select - 1] = "X"
        base[select_rand - 1] = "O"
        base_x =f"GAME TIC TAC TOE\n=============\n| {base[0]} | {base[1]} | {base[2]} |\n| {base[3]} | {base[4]} | {base[5]} |\n| {base[6]} | {base[7]} | {base[8]} |\n============="
    else:
        print("Maaf User Input sama atau sudah ada coba lagi !!!\n")

# Kondisi
    if base[:3] == ["X","X","X"] or base[3:6] == ["X","X","X"] or base[6:9] == ["X","X","X"]:
        print("You Win")
        hasil -= 1
        base  = ["-","-","-","-","-","-","-","-","-"]
        base_x =f"GAME TIC TAC TOE\n=============\n| - | - | - |\n| - | - | - |\n| - | - | - |\n============="
        isRuning = isRun()

    elif base[0:7:3] == ["X","X","X"] or base[1:8:3] == ["X","X","X"] or base[2:9:3] == ["X","X","X"]:
        print("You Win")
        hasil -= 1
        base  = ["-","-","-","-","-","-","-","-","-"]
        base_x =f"GAME TIC TAC TOE\n=============\n| - | - | - |\n| - | - | - |\n| - | - | - |\n============="
        isRuning = isRun()

    elif base[0:10:4] == ["X","X","X"] or base[2:7:2] == ["X","X","X"]:
        print("You Win")
        hasil -= 1
        base  = ["-","-","-","-","-","-","-","-","-"]
        base_x =f"GAME TIC TAC TOE\n=============\n| - | - | - |\n| - | - | - |\n| - | - | - |\n============="
        isRuning = isRun()

    elif base[:3] == ["O","O","O"] or base[3:6] == ["O","O","O"] or base[6:9] == ["O","O","O"]:
        print("You Lose")
        hasil -= 1
        base  = ["-","-","-","-","-","-","-","-","-"]
        base_x =f"GAME TIC TAC TOE\n=============\n| - | - | - |\n| - | - | - |\n| - | - | - |\n============="
        isRuning = isRun()

    elif base[0:7:3] == ["O","O","O"] or base[1:8:3] == ["O","O","O"] or base[2:9:3] == ["O","O","O"]:
        print("You Lose")
        hasil -= 1
        base  = ["-","-","-","-","-","-","-","-","-"]
        base_x =f"GAME TIC TAC TOE\n=============\n| - | - | - |\n| - | - | - |\n| - | - | - |\n============="
        isRuning = isRun()

    elif base[0:10:4] == ["O","O","O"] or base[2:7:2] == ["O","O","O"]:
        print("You Lose")
        hasil -= 1
        base  = ["-","-","-","-","-","-","-","-","-"]
        base_x =f"GAME TIC TAC TOE\n=============\n| - | - | - |\n| - | - | - |\n| - | - | - |\n============="
        isRuning = isRun()

    else:
        tes = 0
        for i in base:
            if i == "-":
                tes -= 1
        if tes == 1:
            print("Hasilnya Seri")
            base  = ["-","-","-","-","-","-","-","-","-"]
            base_x =f"GAME TIC TAC TOE\n=============\n| - | - | - |\n| - | - | - |\n| - | - | - |\n============="
            isRuning = isRun()

