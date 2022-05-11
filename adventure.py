def create_adventure():

    while True:
        start = input("Select your character: (Fighter/Wizard/Bard) ").capitalize().strip()
        if start == "Fighter":
            weapon = input("Choose your weapon: (Longsword/Greataxe/Bow) ").capitalize().strip()
            if weapon == "Longsword":
                print("You sheith the weapon")
                break

        elif start == "Wizard":
            spell = input("Choose your spell: (Firestrike/Icestrike/Windstrike) ").capitalize().strip()

        elif start == "Bard":
            song = input("Choose your song: (Sleep/Blind/Deafen) ").capitalize().strip()

create_adventure()
