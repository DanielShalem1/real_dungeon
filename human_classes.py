from living import Living
import attacks
from interfaces import *
from inventory import *
import helpers


def choosing_attack_index(attacks, creature, inventory):
    attack_names = []  # list to hold all the attacks' names for the picking screen
    for attack in attacks:
        attack_names.append(attack.name)
    user_input = input("chose attack number: {}".format(attack_names + ['inventory', 'attacks description']))
    while not helpers.valid_value(user_input, len(attacks) + 2):
        user_input = input("chose attack number: {}".format(attack_names + ['inventory', 'attacks description']))
    attack_index = int(user_input)
    real_attack_index = attack_index - 1  # the player choose a number with the minimum of 1,\
    # however our list start with the index 0
    while real_attack_index == len(attacks)+1: #the user choose the to show the attacks description
        for attack in attacks:
            print(attack.name + ": " + attack.description)
        user_input = input("chose attack number: {}".format(attack_names + ['inventory', 'attacks description']))
        while not helpers.valid_value(user_input, len(attacks) + 2):
            user_input = input("chose attack number: {}".format(attack_names + ['inventory', 'attacks description']))
        attack_index = int(user_input)
        real_attack_index = attack_index - 1
    if real_attack_index == len(attacks):  # the user chose inventory
        return handle_inventory(creature, inventory)
    return real_attack_index

class Human(Living, NPC_interface):
    """
    the base human class, inherits from the Living class.
    """
    def __init__(self, hp, speed, armor, power, fear="", name="", magic=0):
        self.fear = fear
        self.attacks = [attacks.Punch()]
        self.inventory = {}
        self.level = 1
        self.money = 0
        super().__init__(hp, speed, armor, power, "Human", name, magic)

    def talk(self):
        print("Hi! my name is {} what is your name?".format(self.name))
        given_name = input()
        print("hi {} nice to meet you!!".format(given_name))

    def attack(self,**kwargs):
        """
        let the player to choose between the different attacks of the human and executing them
        :return:
        """

        real_attack_index = choosing_attack_index(self.attacks, self, self.inventory)
        if real_attack_index != -1:
            damage = self.attacks[real_attack_index].execute(attacker=self, **kwargs)
        else:
            damage = 0
        if self.hp <= 0:
            print("{} is dead.. :(".format(self.name))
        return damage

class Cleric(Human):
    """
    the base divine powers class
    """
    def __init__(self, hp, speed, armor, power, fear="", name="", magic=10):
        super().__init__(hp, speed, armor, power, fear, name, magic)
        self.attacks += [attacks.Soul_burst(), attacks.Heal()]

    def interact(self):
        heal_option = input("what a holly day, do you want me to heal you? Y/N")
        if heal_option.upper() == 'Y':
            pass #need to fill the heal

class Warlock(Human):
    """
    the base divine powers class
    """
    def __init__(self, hp, speed, armor, power, fear="", name="", magic=15):
        super().__init__(hp, speed, armor, power, fear, name, magic)
        self.attacks += [attacks.Dark_magic(), attacks.Curse()]

    def interact(self):
        heal_option = input("what a bad day, do you want me to curse you? Y/N")
        if heal_option.upper() == 'Y':
            print("abada cadabra")

if __name__ == "__main__":

    bob_stats = {'speed':5, 'hp':3, 'armor':10, 'power':5, 'fear':"dark", 'name':"bob"}
    print(bob_stats['hp'])
    bob = Cleric(**bob_stats)
    print(issubclass(Human, NPC_interface))
    print(issubclass(Cleric, NPC_interface))