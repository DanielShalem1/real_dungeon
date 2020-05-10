import monsters
import human_classes
import fight

def main():
    bob = human_classes.Cleric(35,10,10,10,"dark","Bob")
    momo = monsters.Bullywug(speed=50,name="momo")
    carbarous = monsters.Hellhound()
    grimlock = monsters.Grimlock(hp=50)
    basiliks = monsters.Basiliks()
    fight.full_fight(bob, grimlock)

if __name__ == "__main__":
    main()
