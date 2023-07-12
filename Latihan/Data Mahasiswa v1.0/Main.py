# Program data mahasiswa
print("Nama  : Abdullah Muchsin")
print("Kelas : 12 IPA")
print("NIM   : 00440234098\n")

import os

part_data = []
data_mahasiswa = []
class Mahasiswa:
    def __init__(self,pd,dm):
        self.__part_data = pd.copy()
        self.__data_mahasiswa = dm.copy()
        self.__number = 0
    def input_part(self):
        while (not False):
            self.__name = input("Masukana nama : ")
            self.__part_data.append(self.__name)
            self.__kelas = input("Masukan kelas : ")
            self.__part_data.append(self.__kelas)
            try:
                self.__nim = int(input("Masukan NIM   : "))
                self.__part_data.append(self.__nim)
            except:
                print("NIM Tidak Valid !")
                self.__part_data.clear()
                continue
            try:
                self.__ipk = float(input("Masukan IPK   : "))
                self.__part_data.append(self.__ipk)
            except:
                print("IPK Tidak Valid !")
                self.__part_data.clear()
                continue
            self.__part_data.append(self.__nim)

            self.__part_asli = self.__part_data.copy()
            self.__data_mahasiswa.append(self.__part_asli)
            self.__number += 1
            self.__part_data.clear()
            isOption = input("Apakah nambah lagi (y/n) : ")
            if isOption == "n" or isOption == "N":
                os.system("cls")
                break
            os.system("cls")
            print(f"Total data mahasiswa : {self.__number}")
    
    def output_data(self):
        print(f"Total data mahasiswa : {self.__number}")
        for i in range(0,len(self.__data_mahasiswa)):
            number = self.__data_mahasiswa[i][3]
            if number >= 3.5:
                print(f"============= Data Mahasiswa ke-{i + 1} =============")
                print(f"Nama  : {self.__data_mahasiswa[i][0]}")
                print(f"Kelas : {self.__data_mahasiswa[i][1]}")
                print(f"NIM   : {self.__data_mahasiswa[i][2]}")
                print(f"IPK   : {self.__data_mahasiswa[i][3]}\n")

def main():
    mahasiswa = Mahasiswa(part_data, data_mahasiswa)
    mahasiswa.input_part()
    mahasiswa.output_data()

main()
