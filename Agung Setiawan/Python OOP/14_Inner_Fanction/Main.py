class Hero:
    def __init__(self,name,health): # Magic Method adalah code khusus yang dipangil secara khusus yang codenya ditandai __nama__
        self.name = name
        self.health = health
    
    def info(self):
        def view_name():
            return f"Nama : {self.name}"
        def view_health():
            return f"Health : {self.health}"

        return view_name, view_health()
        
Tank = Hero("Banteng",100)

name, health = Tank.info()
print(name(),"\n" + health)

