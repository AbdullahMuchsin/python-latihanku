class Hero:
    def __init__(self,name,health,attpower):
        self.__name = name
        self.__health = health
        self.__attpower = attpower

    def update_health(self,uphealth):
        if self.__health < 100:
            self.__health = uphealth + 100
            
    def getHealth(self):
        return self.__health
    
    def info(self):
        print(f"{self.__name}:\n\tHealth : {self.__health}\n\tAttPower : {self.__attpower}")


tank = Hero("Banteng",100,15)
tank.update_health(50)
tank.info()

archer = Hero("GunMan",85,25)
archer.update_health(50)
archer.info()
