class Karyawan:
    def __init__(self,name,status):
        self.name = name
        self.status = status
    
    def work(self):
        print(f"{self.skill} : Jangan lupa semangat")

    def Note(self):
        print("Semangat semangat !!!")
    
class Editing(Karyawan):
    def __init__(self,name,status,skill):
        Karyawan.__init__(self,name,status)
        self.skill = skill
    
    def info(self):
        print(f"{self.name}\n\tStatus : {self.status}\n\tSkill : {self.skill}")
        Karyawan.work(self)
    
arto = Karyawan("Arto",True)
arto.Note()
Karyawan.Note(Karyawan)

Hedi = Editing("Hedi",False,"Editing Foto")
Hedi.info()
Hedi.Note()
