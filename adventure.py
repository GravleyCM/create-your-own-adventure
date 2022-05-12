from random import choices
import time

# rand_char = choices(["Warrior", "Mage", "Archer"])
# print(rand_char)

class Character:
            def __init__(self, health, strength, mana, defense, magic_power, char_class, attack):
                self.health = health
                self.strength = strength
                self.mana = mana
                self.defense = defense
                self.magic_power = magic_power
                self.char_class = char_class
                self.attack = attack

            def __str__(self):
                return f"Health = {self.health}\
                        Strength = {self.strength}\
                        Mana = {self.mana}\
                        Defense = {self.defense}\
                        Magic Power = {self.magic_power}\
                        Class = {self.char_class}\
                        Attack = {self.attack}"

def create_character():

    start = input("Select your character: (Fighter/Wizard/Bard) ").capitalize().strip()

    while True:

        def set_fighter(attack):
            Character.health = 100
            Character.strength = 8
            Character.mana = 0
            Character.defense = 7
            Character.magic_power = 0
            Character.char_class = "Fighter"
            Character.attack = attack
            # print(f"Health = {Character.health}\
            #         Strength = {Character.strength}\
            #         Mana = {Character.mana}\
            #         Defense = {Character.defense}\
            #         Magic Power = {Character.magic_power}\
            #         Class = Fighter\
            #         Attack = {attack}")
            return Character

            # return f"Health = {Character.health}\
            #         Strength = {Character.strength}\
            #         Mana = {Character.mana}\
            #         Defense = {Character.defense}\
            #         Magic Power = {Character.magic_power}\
            #         Class = Fighter\
            #         Attack = {attack}"

        def set_wizard(attack):
            Character.health = 100
            Character.strength = 4
            Character.mana = 8
            Character.defense = 3
            Character.magic_power = 8
            Character.char_class = "Wizard"
            Character.attack = attack

            return f"Health = {Character.health}\
                    Strength = {Character.strength}\
                    Mana = {Character.mana}\
                    Defense = {Character.defense}\
                    Magic Power = {Character.magic_power}\
                    Class = Wizard\
                    Attack = {attack}"

        def set_bard(attack):
            Character.health = 100
            Character.strength = 4
            Character.mana = 6
            Character.defense = 5
            Character.magic_power = 7
            Character.char_class = "Bard"
            Character.attack = attack

            return f"Health = {Character.health}\
                    Strength = {Character.strength}\
                    Mana = {Character.mana}\
                    Defense = {Character.defense}\
                    Magic Power = {Character.magic_power}\
                    Class = Bard\
                    Attack = {attack}"


        if start == "Fighter":

            weapon = input("Choose your weapon: (Longsword/Greataxe/Bow) ").capitalize().strip()

            if weapon == "Longsword":
                print("Preparing for your adventure")
                time.sleep(3)
                return character

            elif weapon == "Greataxe":
                print("Preparing for your adventure")
                time.sleep(3)
                print(set_fighter("Greataxe"))
                break

            elif weapon == "Bow":
                print("Preparing for your adventure")
                time.sleep(3)
                character = set_fighter("Bow")
                return character

        elif start == "Wizard":

            spell = input("Choose your spell: (Firestrike/Icestrike/Windstrike) ").capitalize().strip()

            if spell == "Firestrike":
                print("Preparing for your adventure")
                time.sleep(3)
                print(set_wizard("Firestrike"))
                break

            elif spell == "Icestrike":
                print("Preparing for your adventure")
                time.sleep(3)
                print(set_wizard("Icestrike"))
                break

            elif spell == "Windstrike":
                print("Preparing for your adventure")
                time.sleep(3)
                print(set_wizard("Windstrike"))
                break

        elif start == "Bard":

            song = input("Choose your song: (Sleep/Blind/Deafen) ").capitalize().strip()

            if song == "Sleep":
                print("Preparing for your adventure")
                time.sleep(3)
                print(set_bard("Sleep"))
                break

            elif song == "Blind":
                print("Preparing for your adventure")
                time.sleep(3)
                print(set_bard("Blind"))
                break

            elif song == "Deafen":
                print("Preparing for your adventure")
                time.sleep(3)
                print(set_bard("Deafen"))
                break

def create_story(stats):
    print(f"Health = {stats.health}\
            Strength = {stats.strength}\
            Mana = {stats.mana}\
            Defense = {stats.defense}\
            Magic Power = {stats.magic_power}\
            Class = Fighter\
            Attack = {stats.attack}")
    for key, value in vars(Character).items():
        if not key.startswith('__'):
            print(f"{key} = {value}")

def your_own_adventure():
    create_story(create_character())

your_own_adventure()