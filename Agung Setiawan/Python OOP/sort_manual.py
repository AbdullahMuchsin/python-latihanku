class Sort:
    def __init__(self,lst):
        self.ls = lst.copy()
        
        isRun = len(self.ls)
        while isRun:
            for x in range(len(self.ls)):
                if x + 1 < len(self.ls):
                    if self.ls[x]<self.ls[x + 1]:
                        a = self.ls[x]
                        b = self.ls[x + 1]
                        self.ls[x + 1] = a
                        self.ls[x] = b
            isRun -= 1

    def info(self):
        print(self.ls)

numbers = [2,4,9,8,3,23,35,5,52,52,6,322,3,2,2,3,4]
eats = ["Sosis","Tempura","Batagor","Bakso","Cireng"]

sNum = Sort(numbers)
sEat = Sort(eats)

sNum.info()
sEat.info()