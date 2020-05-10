def fight_turn(attacker, defender):
    """
    :param attacker: the creature who is executing the attack
    :param defender: the creature who is being attack
    :return:
    """
    damage = attacker.attack()
    real_damage = damage - defender.armor #how much damage is passing through the armor
    if real_damage < 0:
        real_damage = 0
    defender.hp -= real_damage
    print("{} hp is: {} ; {} hp is: {}".format(attacker, attacker.hp, defender, defender.hp))

def full_fight(creature_a, creature_b):
    #checking who is first by their speed
    if creature_a.speed >= creature_b.speed:
        attacker = creature_a
        defender = creature_b
    else:
        attacker = creature_b
        defender = creature_a

    while creature_b.hp > 0 and creature_a.hp > 0: #as long as none of them died
        fight_turn(attacker, defender) #fight turn
        attacker, defender = defender, attacker # swaping the attacker and defender

    #check who won
    if creature_b.hp != 0:
        winner = creature_b.name
    elif creature_a.hp != 0:
        winner = creature_a.name
    else:
        winner = "none!"
        
    print("the winner is: {}".format)


