# BELAJAR OOP PYTHON LATIHAN INHERITANCE
import Pahlawan

mage = Pahlawan.HeroMagic("Mage")
tank = Pahlawan.HeroTank("Tank")

mage.info()
tank.info()

mage.upExp = 1000
tank.upExp = 300
mage.info()
tank.info()
