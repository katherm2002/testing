class Character:
    def __init__(self,name):
        self.name = name
    def introduce(self):
        print(f"My name is {self.name}")

class MarioCharacter(Character):
    def __init__(self,name, lives_attribute):
        super().__init__(name)
        self.lives_attribute = lives_attribute

    def jump(self):
        print(f"{self.name} jumps")

class FireMario(MarioCharacter):
    def __init__(self,name, lives_attribute):
        super().__init__(name,lives_attribute)

    def throw_fireball(self):
        print(f"{self.name} throws a fireball")

class SuperMario(MarioCharacter):
    def __init__(self, name, lives_attribute):
        super().__init__(name,lives_attribute)
    def yell(self):
        print(f"{self.name}: 'Mamma Mia!'")

class SuperFireMario(SuperMario,FireMario):
    def __init__(self,name,lives_attribute):
        super().__init__(name,lives_attribute)

# main program
mario = MarioCharacter("Mario",3)
fire = FireMario("Fire Mario", 5)
super_fire = SuperFireMario("Super Fire Mario",10)

mario.introduce()
mario.jump()
print()

fire.introduce()
fire.jump()
fire.throw_fireball()
print()

super_fire.introduce()
super_fire.jump()
super_fire.throw_fireball()
super_fire.yell()
