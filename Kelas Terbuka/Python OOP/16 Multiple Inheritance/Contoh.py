class Tipe_hero:
    def tipeHero(self,tipe):
        self.tipe = tipe
    def showTipe(self):
        return self.tipe

class Team:
    def teamHero(self,team):
        self.team = team
    def showTeam(self):
        return self.team

class Hero(Tipe_hero,Team):
    def __init__(self,name,health):
        self.__name = name
        self.__health = health
    def info(self):
        print(f"""Name   : {self.__name}
Health : {self.__health}
Tipe   : {super().showTipe()}
Team   : {super().showTeam()}
        """)

hero1 = Hero("Archer", 100)
hero1.tipeHero("Mage")
hero1.teamHero("Biru")

hero1.info()