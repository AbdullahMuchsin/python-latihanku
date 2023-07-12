class Hero():
    def __init__(self,role="-",name="-",skill="-"):
        self.role = role
        self.name = name
        self.skill = skill

tank = Hero("Tank","Banteng","Diam")
archer = Hero(name="Fish", skill="Speed-Up")

print("===================")
print(tank.role)
print(tank.name)
print(tank.skill)
print("-------------------")
print(archer.role)
print(archer.name)
print(archer.skill)
print("===================")
