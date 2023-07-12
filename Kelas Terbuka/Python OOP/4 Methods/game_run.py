# MEMBUAT GAME SEDERHANA DENGAN OOP
import os, random

def karakter():
    name = input("Masukan nama karakter : ")
    return name

class Game:
    def __init__(self,name,nyawa):
        while (True):
            self.name = name
            self.nyawa = nyawa
            os.system("cls")
            print("GAME RUN")
            print("========")
            print("Nyawa Tinggal : " + str(nyawa))
            
            soal1 = random.randint(1,10)
            soal2 = random.randint(1,10)
            operasi = random.randint(1,3)
            hasil = 0

            if operasi == 1:
                print(f"Hasil dari {soal1} + {soal2} adalah : ")
                hasil = soal1 + soal2
            elif operasi == 2:
                print(f"Hasil dari {soal1} - {soal2} adalah : ")
                hasil = soal1 - soal2       
            elif operasi == 3:
                print(f"Hasil dari {soal1} * {soal2} adalah : ")
                hasil = soal1 * soal2

            try:
                jawaban = int(input("Jawab pertanyaan berikut dengan benar: "))
            except:
                print("Jawaban Harus Angka")

            if jawaban == hasil:
                nyawa += 5
                if nyawa == 200:
                    print(name + " Selamat Kamu Menang !!!")
                    break
            elif jawaban != hasil:
                nyawa -= 10
                if nyawa < 0:
                    print("Anda Kalah T_T")
                    break

while (True):
    print("GAME RUN")
    print("========")
    print('''1. Mulai
2. Exit
    ''')

    isSelect = input("Pilih Nomor : ")
    match isSelect:
        case "1": Game(karakter(),100)
        case "2": break
    break

print("\nPROGRAM BERAKHIR")