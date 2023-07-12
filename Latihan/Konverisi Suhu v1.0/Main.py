from abc import ABC,abstractmethod
import os

class Suhu(ABC):

    @property
    def suhu(self):
        self.__suhu = self.suhu
        return self.__suhu
    
    @abstractmethod
    def view(self):
        pass

class Celcius(Suhu):
    def suhu(self, value):
        self.__creamur = ((4/5) * value)
        self.__cfahrenheit = ((9/5) * value) + 32 
        self.__ckelvin = value + 273

    def view(self):
        print("============== CELCIUS ==============")
        print(f"Reamur      : {self.__creamur:.2f}")
        print(f"Fahrenheit  : {self.__cfahrenheit:.2f}")
        print(f"Kelvin      : {self.__ckelvin}")
        print("=====================================")

class Reamur(Suhu):
    def suhu(self, value):
        self.__rcelcius = ((5/4) * value)
        self.__rfahrenheit = ((9/4) * value) + 32 
        self.__rkelvin = ((5/4) * value) + 273

    def view(self):
        print("============== REAMUR ==============")
        print(f"Celcius     : {self.__rcelcius:.2f}")
        print(f"Fahrenheit  : {self.__rfahrenheit:.2f}")
        print(f"Kelvin      : {self.__rkelvin:.2f}")
        print("=====================================")

class Fahrenheit(Suhu):
    def suhu(self, value):
        self.__fcelcius = (5/9) * (value - 32)
        self.__freamur = (4/9) * (value - 32)
        self.__fkelvin = (5/9) * (value - 32) + 273

    def view(self):
        print("============= FAHRENHEIT ============")
        print(f"Celcius     : {self.__fcelcius:.2f}")
        print(f"Reamur      : {self.__freamur:.2f}")
        print(f"Kelvin      : {self.__fkelvin:.2f}")
        print("=====================================")

class Kelvin(Suhu):
    def suhu(self, value):
        self.__kcelcius = value - 273
        self.__kreamur = (4/5) * (value - 273)
        self.__kfahrenheit = (9/5) * (value - 273) + 32

    def view(self):
        print("============== KELVIN ===============")
        print(f"Celcius     : {self.__kcelcius:.2f}")
        print(f"Reamur      : {self.__kreamur:.2f}")
        print(f"Fahrenheit  : {self.__kfahrenheit:.2f}")
        print("=====================================")

def match(value,x):
    match value:
        case "1": 
            celcius = Celcius()
            celcius.suhu(x)
            celcius.view()
        case "2": 
            reamur = Reamur()
            reamur.suhu(x)
            reamur.view()
        case "3": 
            fahrenheit = Fahrenheit()
            fahrenheit.suhu(x)
            fahrenheit.view()
        case "4": 
            kelvin = Kelvin()
            kelvin.suhu(x)
            kelvin.view()
        case _:
            print("Nomor tidak valid :(")
def main():
    isRun = True
    while (isRun is not False):
        os.system("cls")
        print("="*5,"KONVERSI SUHU","="*5)
        print("1. Celcius")
        print("2. Reamur")
        print("3. Fahrenheit")
        print("4. Kelvin\n")
        select = input("Pilih Nomor : ")
        try:
            valsuhu = float(input("Masukan besar suhu : "))
            match(select,valsuhu)
        except:
            continue

        isOption = input("Apakah coba lagi (y/n) ?")
        if isOption == "n" or isOption == "N":
            isRun = False

main()