import monsters
import human_classes
import fight

def main():
    bob = human_classes.Cleric(35,10,10,10,"dark","Bob")
    momo = monsters.Bullywug(speed=50,name="momo")
    carbarous = monsters.Hellhound()
    grimlock = monsters.Grimlock(hp=50)
    basiliks = monsters.Basiliks()
    soro = human_classes.Warlock(40,30,35,20,"light","soro")
    fight.full_fight(soro, basiliks)

if __name__ == "__main__":
    main()
