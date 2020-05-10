import sys
sys.path.append(r'/home/daniel/dungeon/lib/python3.6/site-packages/')
import human_classes
import attacks
import pytest
import main_game
import fight
import monsters

def test_human_creation():
    bob = human_classes.Cleric(10, 10, 10, 10, "dark", "Bob")
    assert bob.hp == 10

def test_heal():
    bob = human_classes.Cleric(10, 10, 10, 10, "dark", "Bob")
    heal = attacks.Heal()
    heal.execute(bob)
    assert bob.hp == 15

def test_bite():
    bob = human_classes.Cleric(10, 10, 10, 10, "dark", "Bob")
    hound = monsters.Hellhound(speed=10)
    bite = attacks.Bite()
    bite.execute(attacker=hound,defender=bob)
    assert True

def test_NPC_interface_not_implemented():
    with pytest.raises(Exception):
        assert human_classes.Human(10, 10, 10, 10, "dark", "Bob") # the Human class does not implement "interact", so Exception should raise

"""
def test_spear_attack():
    momo = monsters.Bullywug(speed=20, name="momo") #all the bullywugs have 12 power
    spear_attack = attacks.Spear_attack()
    assert spear_attack.execute(momo) == 16 #the damage should be the average of power(12) and speed (20)
"""

