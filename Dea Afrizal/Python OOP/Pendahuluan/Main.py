class Hero:
    def __init__(self,name,health = 100,energy = 100):
        self.name = name
        self.health = health
        self.energy = energy
    
    def attack(self,target, damage = 1):
        target.health -= damage
        self.energy -= damage
        print(f"{self.name} menyerang {target.name} sebesar {damage}")
        
        if target.is_attack(self):
            self.health -= target.damage
        else:
            print(f"{target.name} ZZZzzzz")
    
    def show_info(self):
        print(f"================={self.name:^7}================")
        print(f"Health {self.name} : {self.health}")
        print(f"Energy {self.name} : {self.energy}")
        print(f"========================================")


class Moster:
    def __init__(self,name,health=100):
        self.name = name
        self.health = health
        self.health_statis = health
        self.damage = 10

    def is_attack(self, name_back):
        print(f"{self.name} Menyerang balik kepada {name_back.name} sebesar {self.damage}")
        return self.health < self.health_statis
    
    def show_info(self):
        print(f"================={self.name:^7}================")
        print(f"Health {self.name} : {self.health}")
        print(f"========================================")
    
pencil = Hero(name="Pencil")
bag = Hero(name="Bag",health=200)
bird = Moster(name="Bird",health=500)

pencil.attack(target=bird,damage=25)
bag.attack(target=bird,damage=10)
pencil.show_info()
bag.show_info()
bird.show_info()