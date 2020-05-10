from living import Living
import attacks
from interfaces import *

def choosing_attack_index(attacks):
    attack_names = []  # list to hold all the attacks' names for the picking screen
    for attack in attacks:
        attack_names.append(attack.name)
    attack_index = int(input("chose attack number: {}".format(attack_names + ['attacks description'])))
    real_attack_index = attack_index - 1  # the player choose a number with the minimum of 1,\
    # however our list start with the index 0
    while real_attack_index == len(attacks): #the user choose the to show the attacks description
        for attack in attacks:
            print(attack.name + ": " + attack.description)
        attack_index = int(input("chose attack number: {}".format(attack_names + ['attacks description'])))
        real_attack_index = attack_index - 1
    return real_attack_index

class Human(Living, NPC_interface):
    """
    the base human class, inherits from the Living class.
    """
    def __init__(self, hp, speed, armor, power, fear="", name=""):
        self.fear = fear
        self.attacks = [attacks.Punch()]
        super().__init__(hp, speed, armor, power, "Human", name)

    def talk(self):
        print("Hi! my name is {} what is your name?".format(self.name))
        given_name = input()
        print("hi {} nice to meet you!!".format(given_name))

    def attack(self,**kwargs):
        """
        let the player to choose between the different attacks of the human and executing them
        :return:
        """

        real_attack_index = choosing_attack_index(self.attacks)
        damage = self.attacks[real_attack_index].execute(attacker=self, **kwargs)
        if self.hp <= 0:
            print("{} is dead.. :(".format(self.name))
        return damage

class Cleric(Human):
    """
    the base divine powers class
    """
    def __init__(self, hp, speed, armor, power, fear="", name=""):
        super().__init__(hp, speed, armor, power, fear, name)
        self.attacks += [attacks.Soul_burst(), attacks.Heal()]

    def interact(self):
        heal_option = input("what a holly day, do you want me to heal you? Y/N")
        if heal_option.upper() == 'Y':
            pass #need to fill the heal

if __name__ == "__main__":

    bob_stats = {'speed':5, 'hp':3, 'armor':10, 'power':5, 'fear':"dark", 'name':"bob"}
    print(bob_stats['hp'])
    bob = Cleric(**bob_stats)
    print(issubclass(Human, NPC_interface))
    print(issubclass(Cleric, NPC_interface))