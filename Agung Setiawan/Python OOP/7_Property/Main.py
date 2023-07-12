class Hero:
    def __init__(self,name,health,attpower):
        self.__name = name
        self.__health = health
        self.__attpower = attpower

    def info(self):
        print(f"{self.__name}:\n\tHealth : {self.__health}\n\tAttPower : {self.__attpower}")
            
    @property        
    def health(self):
        pass
    
    @health.setter
    def health(self,uphealth):
        if self.__health < 100:
            self.__health = uphealth + 100
    
    @health.getter
    def health(self):
        return self.__health

tank = Hero("Banteng",100,15)
tank.health = 50
tank.info()

archer = Hero("GunMan",85,25)
archer.health = 50
archer.info()
