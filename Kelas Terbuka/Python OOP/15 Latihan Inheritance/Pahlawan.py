class Hero:
    def __init__(self,name):
        self.movehealth = [0,100,200,300,400,500]
        self.moveattpower = [0,5,10,15,20,25]
        self.movearmor = [0,1,2,3,4,5]
        self.__name = name
        self.__level = 0
        self.__exp = 0
    
    def info(self):
        print(f"""Level        : {self.__level}
Nama         : {self.__name}
Health       : {self.__health}
Attack Power : {self.__attpower}
Armor        : {self.__armor}
""")

    @property
    def movehealth(self):
        pass
    @property
    def moveattpower(self):
        pass
    @property
    def movearmor(self):
        pass
    @property
    def upExp(self):
        pass
    @property
    def upLevel(self):
        pass

    @movehealth.setter
    def movehealth(self, input):
        self.__movehealth = input

    @moveattpower.setter
    def moveattpower(self, input):
        self.__moveattpower = input

    @movearmor.setter
    def movearmor(self, input):
        self.__movearmor = input
    
    @upExp.setter
    def upExp(self,input):
        self.__exp += input
        if (self.__exp > 100):
            self.upLevel = self.__exp // 100
            self.__exp %= 100
    
    @upLevel.setter
    def upLevel(self,input):
        if input > 5:
            input = 5

        self.__level = input
        self.__health = self.__movehealth[self.__level]
        self.__attpower = self.__moveattpower[self.__level]
        self.__armor = self.__movearmor[self.__level]

class HeroMagic(Hero):
    def __init__(self,name):
        super().__init__(name)
        self.movehealth = [0,75,150,225,300,375]
        self.moveattpower = [0,5,10,15,20,25]
        self.movearmor = [0,3,6,9,12,15]
        self.upLevel = 1

class HeroTank(Hero):
    def __init__(self,name):
        super().__init__(name)
        self.movehealth = [0,100,200,300,400,500]
        self.moveattpower = [0,2,4,6,8,10]
        self.movearmor = [0,5,10,15,20,25]
        self.upLevel = 1
