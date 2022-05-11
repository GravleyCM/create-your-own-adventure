def create_adventure():

    while True:
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

        def set_fighter(attack):
            Character.health = 100
            Character.strength = 8
            Character.mana = 0
            Character.defense = 7
            Character.magic_power = 0
            Character.char_class = "Fighter"
            Character.attack = attack

            return f"Health = {Character.health}\
                    Strength = {Character.strength}\
                    Mana = {Character.mana}\
                    Defense = {Character.defense}\
                    Magic Power = {Character.magic_power}\
                    Class = Fighter\
                    Attack = {attack}"

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

        start = input("Select your character: (Fighter/Wizard/Bard) ").capitalize().strip()
        if start == "Fighter":

            weapon = input("Choose your weapon: (Longsword/Greataxe/Bow) ").capitalize().strip()

            if weapon == "Longsword":
                print(set_fighter("Longsword"))
                break


            elif weapon == "Greataxe":
                print(set_fighter("Greataxe"))
                break


            elif weapon == "Bow":
                print(set_fighter("Bow"))
                break

        elif start == "Wizard":
            Character.char_class = "Wizard"
            print(f'Your chosen class is {Character.char_class.upper()}')

            spell = input("Choose your spell: (Firestrike/Icestrike/Windstrike) ").capitalize().strip()

        elif start == "Bard":
            Character.char_class = "Bard"
            print(f'Your chosen class is {Character.char_class.upper()}')

            song = input("Choose your song: (Sleep/Blind/Deafen) ").capitalize().strip()


create_adventure()
