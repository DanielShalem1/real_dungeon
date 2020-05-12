import functools
from playsound import playsound
import sound
import helpers
import random
import statuses
def hp_checker(attack_func):
    """
    :param attack_func: the attack execute function
    checks if the executener is dead, if it is, return damage = 0
    :return: the new execute function
    """

    @functools.wraps(attack_func) # preserving the function name
    def hp_checker_wrapper(self, attacker, *args, **kwargs):
        if attacker.hp <= 0:
            print(self.name)
            return 0
        else:
            return(attack_func(self, attacker, *args, **kwargs))
    return hp_checker_wrapper

def damage_armor_calc(damage, defender):
    real_damage = damage - defender.armor  # how much damage is passing through the armor
    if real_damage < 0:
        real_damage = 0
    return real_damage


class Attack:
    """
    base class for all the attacks of the humans and monsters
    """
    def __init__(self, name="", description = "", element=""):
        """
        :param name: the name of the attack
        """
        self.name = name
        self.description = description
        self.element=element

    def execute(self, damage ,attacker, **kwargs):
        """
        prints the attack name
        :param damage: the damage formula
        :return: the damage of the attack
        """
        print(helpers.name_pick(attacker) + " used " +self.name)
        return damage

class Spear_attack(Attack):
    """
    attack that involve speed, therefore the damage is the average of the speed and attack
    """
    def __init__(self):
        desc = "attack that involve speed, therefore the damage is the average of the speed and attack"
        super().__init__("spear attack", desc)

    @hp_checker
    def execute(self, attacker, defender, **kwargs):
        damage = super().execute(int((attacker.power+attacker.speed)/2), attacker=attacker)
        playsound(r"music/epic-sword-clang-2.wav")
        defender.hp -= damage_armor_calc(damage, defender)
        return damage

class Paw_attack(Attack):
    """
    the most basic attack of all the monsters, using raw power
    """

    def __init__(self):
        desc = "the most basic attack of all the monsters, using raw power"
        super().__init__("paw attack", desc)

    @hp_checker
    def execute(self, attacker, defender, **kwargs):
        damage = super().execute(attacker.power, attacker=attacker)
        playsound(r"/home/daniel/PycharmProjects/dungeon/music/punch-02.wav")
        defender.hp -= damage_armor_calc(damage, defender)
        return damage

class Punch(Attack):
    """
    the most basic attack of all the humans, using raw power
    """

    def __init__(self):
        desc = "the most basic attack of all the humans, using raw power"
        super().__init__("punch", desc)

    @hp_checker
    def execute(self, attacker, defender, **kwargs):
        damage = super().execute(attacker.power, attacker=attacker)
        playsound(r"/home/daniel/PycharmProjects/dungeon/music/PUNCH.wav")
        defender.hp -= damage_armor_calc(damage, defender)
        return damage

class Heal(Attack):
    def __init__(self):
        """
        heal the user
        """
        desc = "heal the"
        super().__init__("heal", desc)

    @hp_checker
    def execute(self, attacker, **kwargs):
        attacker.hp += 8 + int(attacker.magic * 0.8)
        damage = super().execute(0, attacker=attacker)
        playsound(r"/home/daniel/PycharmProjects/dungeon/music/healpop.wav")
        return damage

class Soul_burst(Attack):
    def __init__(self):
        """
        attack that deal 150% of the user hp plus the user attack power as light damage, but halves the user hp after use, pierce armor
        """
        desc = "use your own life energy as a weapon, light damage"
        super().__init__("soul burst", desc,"light")

    @hp_checker
    def execute(self, attacker, defender, **kwargs):
        damage = super().execute(int(attacker.hp*1.5)+attacker.power, attacker=attacker)
        attacker.hp -= int(attacker.hp*0.5)
        defender.hp -= damage
        playsound(r"/home/daniel/PycharmProjects/dungeon/music/Explosion+4.wav")
        return damage

class Fire_breath(Attack):
    def __init__(self):
        """
        attack that deal 50% of the user hp plus the user attack power as fire damage, pierce armor
        """
        desc = "attack that deal 50% of the user hp plus the user attack power as fire damage"
        super().__init__("fire breath", desc,"fire")

    @hp_checker
    def execute(self, attacker, defender, **kwargs):
        damage = super().execute(int(attacker.hp*0.4)+int(attacker.power*0.2)+int(attacker.magic*0.4), attacker=attacker)
        defender.hp -= damage
        applied_status = statuses.Burn()
        defender.status[applied_status] = applied_status.duration
        playsound(r"/home/daniel/PycharmProjects/dungeon/music/burning.wav")
        return damage

class Bite(Attack):
    def __init__(self):
        """
        attack with speed and power, chances to bite depends on speed
        """
        desc = "attack with speed and power, chances to bite depends on speed"
        super().__init__("bite", desc)

    @hp_checker
    def execute(self, attacker, defender, **kwargs):
        damage = super().execute(int(attacker.speed * 0.3) + attacker.power*0.5, attacker=attacker)
        playsound(r"/home/daniel/PycharmProjects/dungeon/music/deepbark.wav")
        if attacker.speed < defender.speed:
            damage = 0
            print("bite failed due to speed")
        defender.hp -= damage_armor_calc(damage, defender)
        return damage

class Spiked_bone(Attack):
    def __init__(self):
        """
        attack that deal pierce armor
        """
        desc = "attack that deal 0.8 of the user armor as pierce damage"
        super().__init__("Spiked_bone", desc)

    @hp_checker
    def execute(self, attacker, defender, **kwargs):
        damage = super().execute(int(attacker.armor*0.7), attacker=attacker)
        playsound(r"/home/daniel/PycharmProjects/dungeon/music/spikes.wav")
        defender.hp -= damage
        return damage

class Club_attack(Attack):
    """
    the using raw power combined with club to double the damage
    """

    def __init__(self):
        desc = "the using raw power combined with club to double the damage"
        super().__init__("Club attack", desc)

    @hp_checker
    def execute(self, attacker, defender, **kwargs):
        damage = super().execute(attacker.power*2, attacker=attacker)
        playsound(r"/home/daniel/PycharmProjects/dungeon/music/club.wav")
        defender.hp -= damage_armor_calc(damage, defender)
        return damage

class Petrifying_gaze(Attack):
    def __init__(self):
        """
        magical earth attack which petrifies the defender on failed escapes
        """
        desc = "magical earth attack which petrifies the defender on failed escapes"
        super().__init__("petrifying gaze", desc, "earth")

    @hp_checker
    def execute(self, attacker, defender, **kwargs):
        damage = super().execute(int(attacker.power * 0.5), attacker=attacker)

        petrify_check = False

        #calc the chances of patrifying
        if attacker.speed < defender.speed:
            speed_def = defender.speed - attacker.speed
            petrify_chance = random.randrange(int(speed_def*0.5))
            if petrify_chance == 0:
                petrify_check = True
        else:
            petrify_check = True

        #checking if the petrify succeded
        if petrify_check:
            playsound(r"/home/daniel/PycharmProjects/dungeon/music/FastLava.wav")
            print("{} is petrified".format(helpers.name_pick(defender)))
            defender.hp -= damage
            applied_status = statuses.Petrify()
            defender.status[applied_status] = applied_status.duration
        else:
            damage = 0
            print("petrifies failed due to speed")
        return damage

class Curse(Attack):
    """
    apply curse status to the target which has random effects
    """

    def __init__(self):
        desc = "apply curse status to the target"
        super().__init__("Curse", desc)

    @hp_checker
    def execute(self, attacker, defender, **kwargs):
        damage = super().execute(0, attacker=attacker)
        playsound(r"/home/daniel/PycharmProjects/dungeon/music/wickedmalelaugh1.wav")
        applied_status = statuses.Curse()
        defender.status[applied_status] = applied_status.duration
        return damage

class Dark_magic(Attack):
    """
    uses life energy and magic to apply pierce damage
    """

    def __init__(self):
        desc = "uses life energy and magic to apply pierce damage"
        super().__init__("dark magic", desc)

    @hp_checker
    def execute(self, attacker, defender, **kwargs):
        damage = super().execute(attacker.magic + int(attacker.hp*0.1) , attacker=attacker)
        playsound(r"/home/daniel/PycharmProjects/dungeon/music/black.wav")
        attacker.hp -= int(attacker.hp*0.1)
        defender.hp -= damage
        return damage