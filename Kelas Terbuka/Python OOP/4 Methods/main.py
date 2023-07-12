# BELAJAR PYTHON OOP METHODS

class Hero:
    # Class variable
    jumblah_hero = 0

    def __init__(self, name, power, health): # Tanda self pada method __iniit__ sebagai tamplate self
        self.name = name
        self.power = power
        self.nyawa = health

        Hero.jumblah_hero += 1
    # Void function, method tanpa return, tanpa argumen
    def name_hero(self): # Self selain ini dapat mengubah atribut dari self pusat/__init__ jika tidak dikasih self maka tidak bisa
        print("Hero " + self.name)

    # Method dengan argumen, tanpa return
    def up_power(self, power):
        self.power += power

    # Method dengan return 
    def add_health(self, add:int) -> int:
        self.nyawa += add
        return self.nyawa
    def hela(self):
        self.name = "Marksman"


hero1 = Hero("Tank", 50, 100)
hero2 = Hero("Assasin", 100, 50)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero1.nyawa)

print(Hero("Mage", 75,50).nyawa)

Hero("Support", 70, 70).name_hero()
hero1.name_hero()

hero1.up_power(10)
print(hero1.power)

hero2.add_health(25)
print(hero2.nyawa)

hero1.hela()
print(hero1.__dict__)