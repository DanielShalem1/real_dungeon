import interfaces
from playsound import playsound
import helpers
import human_classes
class Elixir(interfaces.item):
    def __init__(self):
        self.name = "Elixir"
        self.description = "increase hp"

    def active_effect(self, creature):
        print("{} used Elixir".format(helpers.name_pick(creature)))
        #playsound(r"/home/daniel/PycharmProjects/dungeon/music/healpop.wav")
        creature.hp += 20

class Clarity_Water(interfaces.item):
    def __init__(self):
        self.name = "Clarity Water"
        self.description = "increase magic"

    def active_effect(self, creature):
        print("{} used Clarity Water".format(helpers.name_pick(creature)))
        #playsound(r"/home/daniel/PycharmProjects/dungeon/music/healpop.wav")
        creature.magic += 10

def handle_inventory(creature, inventory):
    items = list(inventory.keys())
    items_names = [item.name for item in items]
    user_input = input("chose item number: {}".format(items_names + ['attacks', 'item description']))
    while not helpers.valid_value(user_input, len(items)+2):
        user_input = input("chose item number: {}".format(items_names + ['attacks', 'item description']))
    item_index = int(user_input)
    real_item_index = item_index -1
    while real_item_index == len(items)+1: #the user choose the to show the items' description
        for item in inventory.keys():
            print(item.name + ": " + item.description + " | number left: " + str(inventory[item]))
        user_input = input("chose item number: {}".format(items_names + ['attacks', 'item description']))
        while not helpers.valid_value(user_input, len(items) + 2):
            user_input = input("chose item number: {}".format(items_names + ['attacks', 'item description']))
        item_index = int(user_input)
        real_item_index = item_index - 1
    if real_item_index == len(items):  # the user chose to return to the attacks screen
        return human_classes.choosing_attack_index(creature.attacks, creature, inventory)
    else:
        items[real_item_index].active_effect(creature)
        if inventory[items[real_item_index]] == 1:
            del inventory[items[real_item_index]]
        else:
            inventory[items[real_item_index]] -= 1
        return -1
"""
    if real_item_index == len(attacks): #the user chose to return to the attacks screen
        real_item_index = choosing_attack_index(self.attacks)
"""

