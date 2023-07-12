import os

def operasi(sandi):
        hasil = 0
        for i in range(len(sandi)):
            if sandi[i].islower():
                hasil += 1
                break
        for i in range(len(sandi)):
            if sandi[i].isupper():
                hasil += 1
                break
        for i in range(len(sandi)):
            if sandi[i].isnumeric():
                hasil += 1
                break
        for i in range(len(sandi)):
            if sandi[i].isalnum() != True:
                hasil += 1
                break
        return hasil

def view(sandi):
    print("Scor Untuk Sandi Anda Adalah :",operasi(sandi))

if __name__ == '__main__':
    while True:
        os.system("cls")
        sandi = input("Masukan sandi Minimal 8 Karakter :")
        if len(sandi) < 8:
            continue
        view(sandi)
        isOpstion = input("[?]Coba Lagi (y/n) : ")
        if isOpstion in ('n',"N"):
            break