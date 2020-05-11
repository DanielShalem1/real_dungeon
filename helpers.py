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
    statuses = [s.name for s in list(attacker.status.keys())]#extract statuses names

    bad_statuses = ["petrified"] # list of statuses which prevent attacking
    if any([y in bad_statuses for y in statuses]): #checks if one if one of the attacker's statuses is in the bad_statuses list
        print("{} is not able to attack".format(name_pick(attacker)))
        return False
    else:
        return True

def valid_value(value, len_choises):
    if not value.isnumeric():
        print("wrong value")
        return False
    elif int(value) > len_choises or int(value) < 0:
        print("wrong value")
        return False
    else:
        return True