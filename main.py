import random
from Player import Player
from Party import Party


# creates the starting party as you enter names, adding stats to each member
def starting_party():
    party = Party()
    name = input("Enter names, N to stop: ")
    while name != "N":
        member1 = Player(name)
        party.party_members.append(member1.name)
        character_creation(member1)
        name = input("Enter names, N to stop: ")
    print(party.party_members)


# rolls any sided die
def roll_dice(die_sides):
    return random.randint(1, die_sides)


# rolls the dice for stats which is 3 d6
# can be changed to other dice if needed, global variable?
# returns an array with all the dice rolls
def stat_roll():
    stat_options = []
    total = 0
    for x in range(6):
        for y in range(3):
            total += roll_dice(6)

        stat_options.append(total)
        total = 0

    return stat_options


# determines the highest roll out of an array of rolls
# should be CHANGED to grab any nth highest roll
# used for recommending stats based on race picked
def highest_roll(rolls):
    highest = rolls[0]
    for i in rolls:
        if rolls[i] > highest:
            highest = rolls[i]
    return highest


# the main method that is responsible for creating every aspect of a character
# could be BROKEN up to be more modular
def character_creation(player):
    character_class_creation(player)
    character_race_creation(player)

    print("Allocate your stats")

    stats = stat_roll()

    # Constitution
    # print(recommend_stat(char_class, stats, "CON"))
    player.constitution = stat_pick("Constitution? ", stats)
    player.p_stats["Constitution"][0] = player.constitution

    # Dexterity
    # print(recommend_stat(char_class, stats, "DEX"))
    player.dexterity = stat_pick("Dexterity? ", stats)
    player.p_stats["Dexterity"][0] = player.dexterity

    # Wisdom
    # print(recommend_stat(char_class, stats, "WIS"))
    player.wisdom = stat_pick("Wisdom? ", stats)
    player.p_stats["Wisdom"][0] = player.wisdom

    # Intelligence
    # print(recommend_stat(char_class, stats, "INT"))
    player.intelligence = stat_pick("Intelligence? ", stats)
    player.p_stats["Intelligence"][0] = player.intelligence

    # Strength
    # print(recommend_stat(char_class, stats, "STR"))
    player.strength = stat_pick("Strength? ", stats)
    player.p_stats["Strength"][0] = player.strength

    # Charisma
    # print(recommend_stat(char_class, stats, "CON"))
    player.charisma = stat_pick("Charisma? ", stats)
    player.p_stats["Charisma"][0] = player.charisma

    print(player.p_stats)


def character_class_creation(player):
    # sets character class, SEE RACE CHANGE
    char_class = input("What class would you like your character to be? ")
    player.char_class = char_class


def character_race_creation(player):
    # sets character race, CHANGE to own method, make it usable to any person obj that needs a race
    race = input("What race would you like your character to be? ")
    player.race = race


# simple method to create characters with any value passed
# used to skip long character creation process
def character_creation_test(player, value):
    character_class_creation(player)
    character_race_creation(player)
    player.p_stats["Constitution"][0] = value
    player.p_stats["Dexterity"][0] = value
    player.p_stats["Wisdom"][0] = value
    player.p_stats["Intelligence"][0] = value
    player.p_stats["Strength"][0] = value
    player.p_stats["Charisma"][0] = value


# broadly allows you to pick numbers/stats from an array, could be RENAMED
def stat_pick(prompt, stats):
    print(stats)
    answer = int(input(prompt))
    index = stats.index(answer)
    if index != -1:
        stats.pop(index)
        return answer


# should recommend stats to pick based on the class you picked
# and the highest rolls available
# def recommend_stat(char_class, stats, stat_type):
#     match char_class:
#         case['Bard'] if stat_type == "CHA":
#             return highest_roll(stats)
#         case['Wizard'] if stat_type == "INT":
#             return highest_roll(stats)
#         case['Barbarian'] if stat_type == "STR":
#             return highest_roll(stats)
#         case _:
#             return 0

# start by creating a party of characters and creating each character

player1 = Player("Test")
character_creation_test(player1, 22)
player1.calc_modifiers()
player1.calc_race()
print(player1.p_stats)
# player1.money.add_money(0, 0, 0, 0, 500)
# print(player1.money)
player1.p_stats
