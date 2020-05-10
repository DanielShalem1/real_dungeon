def name_pick(creature):
    if creature.name == "":
        return creature.type_of_creature
    else:
        return creature.name

def able_to_attack(attacker):
    """
    :param attacker: the next creature to attack
    checks if the next creature to attack has a status preventing it from attacking
    :return: True if tha attacker can attack and False if not
    """
    statuses = list(attacker.status.keys())

    bad_statuses = ["petrified"] # list of statuses which prevent attacking
    if any([y in bad_statuses for y in statuses]): #checks if one if one of the attacker's statuses is in the bad_statuses list
        return False
    else:
        return True