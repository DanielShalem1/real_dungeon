def name_pick(creature):
    if creature.name == "":
        return creature.type_of_creature
    else:
        return creature.name

def able_to_attack(attacker):
    statuses = list(attacker.status.keys())
    print(statuses)
    bad_statuses = ["petrified"]
    if any([y in bad_statuses for y in statuses]):
        return False
    else:
        return True