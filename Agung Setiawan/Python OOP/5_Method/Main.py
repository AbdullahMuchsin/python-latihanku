class Hero:
    def update_health(self,uphealth):
        if self.health < 100:
            self.health = uphealth + 100
            
    def info(self):
        print(f"{self.name}:\n\tHealth : {self.health}\n\tAttPower : {self.attpower}")

    def __init__(self,name,health,attpower):
        self.name = name
        self.health = health
        self.attpower = attpower

tank = Hero("Banteng",100,15)
tank.update_health(50)
tank.info()

archer = Hero("GunMan",85,25)
archer.update_health(50)
archer.info()
