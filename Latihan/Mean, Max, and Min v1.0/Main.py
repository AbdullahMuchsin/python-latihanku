import os

class View:
    def __init__(self,array,panjang):
        self.array = array
        self.panjang = panjang
        self.hasil = 0

    def view_input(self):
        print(str(self.array) + " Panjang : " + str(self.panjang))

    def mean(self):
        for i in range(0,len(self.array)):
            self.hasil += self.array[i]
        
        self.hasil /= self.panjang
        print("Hasil Rata-Rata nya Adalah : " + str(self.hasil))
    
    def maxmin(self):
        isRun = len(self.array)
        while isRun:
            for x in range(0, len(self.array) - 1):
                    if self.array[x] > self.array[x + 1]:
                        a = self.array[x]
                        b = self.array[x + 1]
                        self.array[x + 1] = a
                        self.array[x] = b
            isRun -= 1

        print("Min-Max   : " + str(self.array))
        print("Nilai Max : " + str(self.array[-1]))
        print("Nilai Min : " + str(self.array[0]))    

def first():
    array = []

    # Input
    while True:
        os.system("cls")
        try:
            angka = int(input("Masukan Angka ke List : "))
        except:
            print("Hanya angka saja")

        array.append(angka)
        panjang = len(array)

        print(str(array) + " Panjang : " + str(panjang))

        isOption = input("Apakah selesai (y/n) : ")
        if isOption == "y" or isOption == "Y":
            break

    return array,panjang
    
def main():
    array, panjang = first()
    ViewResult = View(array,panjang)

    os.system("cls")
    
    ViewResult.view_input()
    ViewResult.mean()
    ViewResult.maxmin()

main()