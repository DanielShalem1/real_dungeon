class Living:
    """
    base class for all living things.
    All living things have: hp, speed, armor, power, type_of_creature and name
    """
    def __init__(self, hp, speed, armor, power, type_of_creature, name=""):
        """
        :param hp: health
        :param speed: speed, used for attacks and turn order
        :param armor: armor
        :param power: power, used for attacks
        :param type_of_creature: via the different classes
        :param name: a living thing has no name by default. If it has a name it is considered unique
        """
        if name != "":
            self.is_unique = True
            self.name = name
        else:
            self.is_unique = False
        self.name = name
        self.hp = hp
        self.speed = speed
        self.armor = armor
        self.power = power
        self.type_of_creature = type_of_creature
        self.status = {}

    def talk(self):
        """
        prints the type and name. most of the time it is overridded
        """
        print("I am a {}".format(self.type_of_creature))
        if self.is_unique:
            print("and my name is: {}".format(self.name))






