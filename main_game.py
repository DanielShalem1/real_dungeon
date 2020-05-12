import monsters
import human_classes
import fight
from inventory import *
import merchant
def main():
    bob = human_classes.Cleric(35,10,10,10,"dark","Bob")
    bob.money = 5
    momo = monsters.Bullywug(speed=50,name="momo")
    carbarous = monsters.Hellhound()
    grimlock = monsters.Grimlock(hp=50)
    basiliks = monsters.Basiliks()
    soro = human_classes.Warlock(40,30,35,20,"light","soro")
    soro.inventory = {Elixir:2, Clarity_Water:1}
    soro.money = 5
    merchant.buying(soro, bob)
    fight.full_fight(soro, carbarous)

if __name__ == "__main__":
    main()
