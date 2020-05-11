import sound
import pygame
import helpers
import statuses
def status_duration_dec(list_of_living):
    for living in list_of_living:
        print(helpers.name_pick(living) + " : " + str(living.status))
        if living.status != {}: #checks if the living creature is affected by a status change
            statuses = list(living.status.keys())
            for status_effect in statuses:
                status_effect.active_effect(living)
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
    attacker.attack(defender=defender)
    def_name = helpers.name_pick(defender)
    attck_name = helpers.name_pick(attacker)
    print("{} attr: hp={} speed={} armor={} power={}, magic={} ".format(attck_name, attacker.hp, attacker.speed, attacker.armor, attacker.power, attacker.magic))
    print("{} attr: hp={} speed={} armor={} power={}, magic={} ".format(def_name, defender.hp, defender.speed, defender.armor, defender.power, defender.magic))


def full_fight(creature_a, creature_b):
    sound.play_sound(r"/home/daniel/PycharmProjects/dungeon/music/Chase - AShamaluevMusic.mp3")

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
        status_duration_dec([attacker, defender])

    # check who won
    if creature_b.hp > 0:
        winner = helpers.name_pick(creature_b)
    elif creature_a.hp > 0:
        winner = helpers.name_pick(creature_a)
    else:
        winner = "none!"

    print("the winner is: {}".format(winner))


