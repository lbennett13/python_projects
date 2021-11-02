from random import *
import time

def roll_a_d4(modifier = 0):
    d4 = randint(1,4)
    return (d4 + modifier)

def roll_a_d6(modifier = 0):
    d6 = randint(1,6)
    return(d6 + modifier)

def roll_a_d8(modifier = 0):
    d8 = randint(1,8)
    return(d8 + modifier)

def roll_a_d10(modifier = 0):
    d10 = randint(1,10)
    return(d10 + modifier)

def roll_a_d12(modifier = 0):
    d12 = randint(1,12)
    return(d12 + modifier)

def roll_a_d20(modifier = 0):
    d20 = randint(1,20)
    return(d20 + modifier)


def roll_a_character():
    #asks for a name
    name = input("What is your name adventurer? ")
    #prints a greeting and begins rolling attributes.
    print("Welcome " + name + ", let's roll some attributes: ")
    print('')
    time.sleep(1)
    strength = 6 + roll_a_d6() + roll_a_d6()
    print("STRENGTH: " + str(strength))
    print('')
    time.sleep(1)
    dexterity = 6 + roll_a_d6() + roll_a_d6()
    print("DEXTERITY: " + str(dexterity))
    print('')
    time.sleep(1)
    constitution = 6 + roll_a_d6() + roll_a_d6()
    print("CONSTITUTION: " + str(constitution))
    print('')
    time.sleep(1)
    intelligence = 6 + roll_a_d6() + roll_a_d6()
    print("INTELLIGENCE: " + str(intelligence))
    print('')
    time.sleep(1)
    wisdom = 6 + roll_a_d6() + roll_a_d6()
    print("WISDOM: " + str(wisdom))
    print('')
    time.sleep(1)
    charisma = 6 + roll_a_d6() + roll_a_d6()
    print("CHARISMA: " + str(charisma))
    print('')
    character_information = {'name': name, 'class':'', 'STR': strength, 'DEX': dexterity, 'CON':constitution, 'INT': intelligence,'WIS': wisdom, 'CHA':charisma}
    return character_information



def class_selection(character):
    print("Choose your class: Soldier (Strong and Durable), Rogue (Quick and Charming), Wizard (Smart and Powerful), or Cleric (Wise and Pious).")
    print('')
    choice = input("What will you choose, S for Soldier, R for Rogue, W for Wizard, or C for Cleric: ")
    choice = choice.lower()
    if choice == "s":
        character['STR'] += 2
        character['CON'] += 2
        character['class'] = "Soldier"
        print("""
        Your spirit is one of a true warrior, 
        many battles over the years have left
        your body scarred 
        those same battles have prepared you
        for an adventurer's journey!
        STR +2
        CON +2
        """)
    elif choice == "r":
        character['DEX'] += 2
        character['CHA'] += 2
        character['class'] = "Rogue"
        print("""
        The road you traveled was not an easy one
        but has prepared your wits and reactions 
        for anything life can throw at you.
        The shadow is your friend,
        try as they might they will never catch you
        and if they do,
        you'll smooth talk your way out of there
        before they as much as lay a finger on you.
        DEX +2
        CHA +2
        """)
    elif choice == "w":
        character['INT'] += 3
        character['DEX'] += 1
        character['class'] = 'Wizard'
        print("""
        The arcane arts have always caught your eye
        it may have been the mystery that lies within
        its strange powers.
        Either way the power it supplies
        is intoxicating.
        With magic enemies don't stand a chance
        and even without the magic
        you could outsmart any dumb beast in your way!
        INT +3
        DEX +1
        """)
    elif choice == "c":
        character['WIS'] += 2
        character['CON'] += 1
        character['STR'] += 1
        character['class'] = 'Cleric'
        ("""
        Others think of you as snobby or a prude.
        Let them judge as they wish,
        for true judgement comes from the hand of God.
        And you are his axe.
        You carry out the will of Him above
        Magic or Warhammer, which ever the situation calls for.
        A light to those trapped in darkness,
        guiding them home.
        A nightmare for the darkness,
        that preys on your God's people!
        WIS +2
        CON +1
        STR +1
        """)
    else:
        print("Sorry, there was an error with your selection. Please try again.")

def find_ability_modifiers(ability_scores):
    modifiers = {}
    for key in ability_scores:
        if ability_scores[key] < 10:
            modifiers[key] = -1
        elif ability_scores[key] <= 11:
            modifiers[key] = 0
        elif ability_scores[key] <= 13:
            modifiers[key] = 1
        elif ability_scores[key] <= 15:
            modifiers[key] = 2
        elif ability_scores[key] <= 17:
            modifiers[key] = 3
        elif ability_scores[key] <= 19:
            modifiers[key] = 4
        elif ability_scores[key] == 20:
            modifiers[key] = 5
    return modifiers

while True:
    #greeting to players
    print("""
    Welcome to DND lite!
    This game is a work in progress.
    I hope you enjoy!
    """)
    adventurer = roll_a_character()
    time.sleep(1)
    class_selection(adventurer)
    time.sleep(1)
    ability_score_lst = {}
    for key in adventurer:
        if 'name' not in key and 'class' not in key:
            ability_score_lst[key] = adventurer[key]
    ability_modifiers = find_ability_modifiers(ability_score_lst)
    adventurer['level'] = 1
    adventurer['HP'] = 10 + ability_modifiers['CON']
    health = adventurer['HP']
    print("So your adventure begins. Best of luck to you " + adventurer['name'] + ", the " + adventurer['class'] + ".")
    while health > 0:
        print("""

        As you make your way to Phandalen seeking to meet with Grimgar,
        who gave you a pretty penny to make sure his caravan arrived on time.
        You slow your pace as something appears to be blocking the way.
        As you get closer you realize it is a horse.
        The horse has arrows sticking out of its body.

        """)

        time.sleep(1)

        choice_a = input("""

        How do you proceed?:
        a.) I get closer to get a better look at the horse.
        b.) I prepare for intruders, arrows don't grow out of horses.
        c.) I try and move the horse, as sad as it is I have a mission.

        """)

        print('')
        
        if choice_a == "a":
            print("You realize that the wounds are relatively fresh. The horse is no longer breathing, but the wounds are recent. The enemies must be nearby.")
        elif choice_a == "b":
            print("You listen intently for movement amongst the bushes... For a moment you swear you are alone. THERE! You hear rustling and the you notice the ghoulish green face of goblins.")
        elif choice_a == "c":
            strength_check = roll_a_d20(ability_modifiers['STR'])
            if strength_check >= 12:
                print("Success! You move the horse out of the way. Before you can get back to the caravan, from the woods a metal tipped arrow comes whistling at you.")
                dex_check = roll_a_d20(ability_modifiers['DEX'])
                print("You attempt to roll out of the way. Dexterity Check: " + str(dex_check))
                if dex_check <= 12:
                    damage = roll_a_d4(1)
                    print("You take " + str(damage) + " points of damage")
                    adventurer['HP'] -= damage
                else:
                    print("Your nimbly dodge the arrow. You are not alone. Goblins have returned looking for their next kill.")
            else:
                print("Try as you might, the beast will not move. As you head back to the caravan, a metal tipped arrow comes whistling toward you.")
                dex_check = roll_a_d20(ability_modifiers['DEX'])
                print("You attempt to roll out of the way. Dexterity Check: " + str(dex_check))
                if dex_check <= 15:
                    damage = roll_a_d4(1)
                    print("Unsuccessful. You take " + str(damage) + " points of damage")
                    adventurer['HP'] -= damage
                else: print("You nimbly dodge the arrow. You are not alone. Goblins have returned looking for their next kill.")
        break
    break