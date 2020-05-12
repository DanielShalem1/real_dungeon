from living import Living
import attacks
import pdb
import random

class Monster(Living):
    """
    The base monseter class, inherits from the Living class.
    Monsters have weakness and attacks list with different attacks objects from the attacks.py
    """
    def __init__(self, hp, speed, armor, power, type_of_creature, weakness="", name="", magic=0):
        self.weakness = weakness

        super().__init__(hp, speed, armor, power, type_of_creature, name, magic)
        self.attacks = [attacks.Paw_attack()]

    def roar(self):
        """
        prints the roar of the monster
        if the total of power, speed and hp is more than 60 the monster is considered powerfull and declares it.
        """
        monster_roar = "I am a monster"
        if self.power + self.speed + self.hp > 100:
            monster_roar += " and i am powerfull"
        print(monster_roar)

    def attack(self, **kwargs):
        """
        randomly execute an attack fromt he attacks list
        :return: the damage of the attack
        """
        attack_index = random.randrange(len(self.attacks))
        return self.attacks[attack_index].execute(damage=0,attacker=self, **kwargs)


class Bullywug(Monster):
    def __init__(self, hp=11, speed=20, armor=15, power=12, type_of_creature="Bullywug", weakness="electricity", name=""):
        super().__init__(hp, speed, armor, power, type_of_creature, weakness, name)
        self.attacks += [attacks.Spear_attack(), attacks.Heal()]

class Hellhound(Monster):
    def __init__(self, hp=45, speed=50, armor=15, power=17, type_of_creature="Hell Hound", weakness="light", name=""):
        super().__init__(hp, speed, armor, power, type_of_creature, weakness, name, magic=5)
        self.attacks += [attacks.Bite(), attacks.Fire_breath()]

class Grimlock(Monster):
    def __init__(self, hp=12, speed=30, armor=11, power=17, type_of_creature="Grimlock", weakness="", name=""):
        super().__init__(hp, speed, armor, power, type_of_creature, weakness, name)
        self.attacks += [attacks.Club_attack(), attacks.Spiked_bone()]

class Basiliks(Monster):
    def __init__(self, hp=52, speed=25, armor=17, power=16, type_of_creature="Basiliks", weakness="", name=""):
        super().__init__(hp, speed, armor, power, type_of_creature, weakness, name, magic=10)
        self.attacks = [attacks.Spiked_bone(), attacks.Petrifying_gaze()]

if __name__ == "__main__":
    kapa = Monster(10,10,10,10,"Kapa")
    kapa.talk()
    kapa.roar()
    legendary_kapa = Monster(15, 50, 20, 10, "Kapa", "kopo")
    legendary_kapa.talk()
    legendary_kapa.roar()
    legendary_bullywug = Bullywug(speed=80, name="momo")
    print(kapa.attack())
    legendary_bullywug.talk()
    legendary_bullywug.roar()
    print(legendary_bullywug.attack())
    print(legendary_bullywug.attack())
    print(legendary_bullywug.attack())
    print(legendary_bullywug.hp)
