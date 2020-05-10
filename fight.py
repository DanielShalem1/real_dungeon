import sound
import pygame
import helpers

def status_duration_dec(list_of_living):
    for living in list_of_living:
        print(helpers.name_pick(living) + " : " + str(living.status))
        if living.status != {}: #checks if the living creature is affected by a status change
            statuses = list(living.status.keys())
            for status_effect in statuses:
                if living.status[status_effect] == 1:
                    del living.status[status_effect]
                else:
                    living.status[status_effect] -= 1

def fight_turn(attacker, defender):
    """
    :param attacker: the creature who is executing the attack
    :param defender: the creature who is being attack
    :return:
    """
    status_duration_dec([attacker, defender])
    attacker.attack(defender=defender)
    def_name = helpers.name_pick(defender)
    attck_name = helpers.name_pick(attacker)
    print("{} hp is: {} ; {} hp is: {}".format(attck_name, attacker.hp, def_name, defender.hp))


def full_fight(creature_a, creature_b):
    #sound.play_sound(r"/home/daniel/PycharmProjects/dungeon/music/Chase - AShamaluevMusic.mp3")

    # checking who is first by their speed
    if creature_a.speed >= creature_b.speed:
        attacker = creature_a
        defender = creature_b
    else:
        attacker = creature_b
        defender = creature_a
#hello
    while creature_b.hp > 0 and creature_a.hp > 0:  # as long as none of them died
        fight_turn(attacker, defender)  # fight turn
        if helpers.able_to_attack(defender):
            attacker, defender = defender, attacker  # swaping the attacker and defender

    # check who won
    if creature_b.hp >= 0:
        winner = helpers.name_pick(creature_b)
    elif creature_a.hp >= 0:
        winner = helpers.name_pick(creature_a)
    else:
        winner = "none!"

    print("the winner is: {}".format(winner))


