import random
import helpers
class Status():
    def __init__(self, duration=3, name=""):
        self.duration = duration
        self.name = name

    def active_effect(self, creature):
        pass

class Petrify(Status):
    def __init__(self):
        super().__init__(3,"petrified")

class Burn(Status):
    def __init__(self):
        super().__init__(2,"Burn")

    def active_effect(self, creature):
        print("{} burned".format(helpers.name_pick(creature)))
        creature.hp -= 3

class Curse(Status):
    def __init__(self):
        super().__init__(5, "Cursed")

    def active_effect(self, creature):
        random_curse_index = random.randrange(4)
        if (random_curse_index) == 3:
            print("hp curse")
            creature.hp = int(creature.hp*0.8)
        elif (random_curse_index) == 2:
            print("armor curse")
            creature.armor = int(creature.armor*0.8)
        elif (random_curse_index) == 1:
            print("speed curse")
            creature.speed = int(creature.speed*0.8)
        elif (random_curse_index) == 0:
            print("power curse")
            creature.power = int(creature.power*0.8)
