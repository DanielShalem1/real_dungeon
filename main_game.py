import monsters
import human_classes
import fight

def main():
    hadar = human_classes.Cleric(25,5,5,5,"dark","Hadar")
    momo = monsters.Bullywug(speed=50,name="momo")
    carbarous = monsters.Hellhound()
    grimlock = monsters.Grimlock(hp=50)
    basiliks = monsters.Basiliks()
    fight.full_fight(basiliks, grimlock)

if __name__ == "__main__":
    main()
