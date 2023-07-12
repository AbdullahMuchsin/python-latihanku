class Hero:
    def __init__(self,name,health): # Magic Method adalah code khusus yang dipangil secara khusus yang codenya ditandai __nama__
        self.name = name
        self.health = health
        print("Ini Magic Method")
    
    def __str__(self):
        return f"{self.name} - Health {self.health}"
    
    def __eq__(self,other) -> bool:
        return self.name == other.name

    def __gt__(self,other) -> bool:
        return self.health > other.health
    
    def __add__(self,other):
        return self.health - other.health

Tank = Hero("Banteng",100)
Archer = Hero("GunMan",75)

print(Archer + Tank)