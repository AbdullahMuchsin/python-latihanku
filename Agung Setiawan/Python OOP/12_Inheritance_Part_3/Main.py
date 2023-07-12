class Karyawan:
    def __init__(self,name,status):
        self.name = name
        self.status = status
    
    def work(self):
        print(f"{self.name} Semangat iyaaa (*^_^*)")

    def Note(self):
        print("Semangat semangat !!!")
    
class Editing(Karyawan):
    def __init__(self,name,status,skill="-"):
        Karyawan.__init__(self,name,status)
        self.skill = skill
    
    def info(self):
        print(f"{self.name}\n\tStatus : {self.status}\n\tSkill : {self.skill}")
        Karyawan.work(self)
    
    def work(self):
        print(f"{self.name} Semangat kerja {self.skill}")
    
class Effect(Editing):
    def __init__(self,name,status,skill,position="-"):
        super().__init__(name,status,skill)
        self.position = position
    
    def work(self):
        print(f"{self.name} kamu keren bekerja di {self.position}")

arto = Karyawan("Arto",True)
Hedi = Editing("Hedi",False,"Editing Foto")
Muchsin = Effect("Muchsin",True,"Coding","Technical Engineer")

def info(clss): # Ini dinamakan polimerfisem
    clss.work()

class Hero:
    def __init__(self,name):
        self.name = name
    def work(self):
        print(f"{self.name} Kerennnn !!!")

Tank = Hero("Banteng")

info(Tank)

info(arto)
info(Hedi)
info(Muchsin)
