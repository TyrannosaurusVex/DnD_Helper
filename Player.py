from Items import Items
from Items import Currency


class Person:
    name = "null"
    char_class = "null"
    race = "null"
    health = 8
    armor_class = 8
    movement = 30
    level = 1

    # inventory and related methods
    inventory = []

    # def check_inventory(self, item):

    money = Currency(0)

    # alignment - Switch key and value
    p_alignment = {
        "Lawful Good": "LG",
        "Neutral Good": "NG",
        "Chaotic Good": "CG",
        "Lawful Neutral": "LN",
        "True Neutral": "TN",
        "Chaotic Neutral": "CN",
        "Lawful Evil": "LE",
        "Neutral Evil": "NE",
        "Chaotic Evil": "CE"
    }

    # a way to recommend stats for certain classes in character creation
    best_class_stats = {
        "Barbarian": ["STR", "CON"],
        "Bard": ["CHA", "DEX"],
        "Wizard": ["INT", "DEX"]
    }


class Player(Person):
    # something
    inv_weight = 0
    spell_slots = 0

    # skills on the character sheet, holds skill and modifier for each one
    p_skills = {
        "Acrobatics": 0,
        "Animal Handling": 0,
        "Arcana": 0,
        "Athletics": 0,
        "Deception": 0,
        "History": 0,
        "Insight": 0,
        "Intimidation": 0,
        "Investigation": 0,
        "Medicine": 0,
        "Nature": 0,
        "Perception": 0,
        "Persuasion": 0,
        "Religion": 0,
        "Sleight of Hand": 0,
        "Stealth": 0,
        "Survival": 0
    }

    # stats on the character sheet, first value is the base value
    # and the second value is the modifier
    p_stats = {
        "Strength": [0, 0],
        "Dexterity": [0, 0],
        "Constitution": [0, 0],
        "Intelligence": [0, 0],
        "Wisdom": [0, 0],
        "Charisma": [0, 0]
    }

    # ability modifiers, used to determine the modifiers of different
    # base values of the stats
    p_modifiers = {
        "1": -5,
        "2": -4,
        "3": -4,
        "4": -3,
        "5": -3,
        "6": -2,
        "7": -2,
        "8": -1,
        "9": -1,
        "10": 0,
        "11": 0,
        "12": 1,
        "13": 1,
        "14": 2,
        "15": 2,
        "16": 3,
        "17": 3,
        "18": 4,
        "19": 4,
        "20": 5,
        "21": 5,
        "22": 6,
        "23": 6,
        "24": 7,
        "25": 7,
        "26": 8,
        "27": 8,
        "28": 9,
        "29": 9,
        "30": 10
    }

    # classes where the values are the Modifiers [Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma]
    p_race = {
        "Dwarf": [0, 0, 2, 0, 0, 0],
        "Elf": [0, 2, 0, 0, 0, 0],
        "Halfling": [0, 0, 0, 0, 0, 1],
        "Human": [1, 1, 1, 1, 1, 1],
        # Human Variant: +1 to two different stats of the player's choice and everything else is +0
        "Dragonborn": [2, 0, 0, 0, 0, 1],
        "Gnome": [0, 0, 0, 2, 0, 0],
        "Half-Elf": [0, 0, 0, 0, 0, 2],  # They also get +1 to two different stats of the player's choice
        "Half-Orc": [2, 0, 1, 0, 0, 0],
        "Tiefling": [0, 0, 0, 1, 0, 2],
        "Scourge Aasimar": [0, 0, 1, 0, 0, 2],
        "Protector Aasimar": [0, 0, 0, 0, 1, 2],
        "Fallen Aasimar": [1, 0, 0, 0, 0, 2],
        "Firbolg": [1, 0, 0, 0, 2, 0],
        "Goliath": [2, 0, 1, 0, 0, 0],
        "Kenku": [0, 2, 0, 0, 1, 0],
        "Lizardfolk": [0, 0, 2, 0, 1, 0],
        "Tabaxi": [0, 2, 0, 0, 0, 1],  # The Furry Race TM
        "Triton": [1, 0, 1, 0, 1, 0]
    }

    # uses the modifier dictionary to determine the second value of the stats dicitonary
    # needs to include calculating race
    def calc_modifiers(self):
        for i in self.p_stats:
            x = str(self.p_stats[i][0])
            self.p_stats[i][1] = self.p_modifiers[x]

    # calculates the race modifiers to be added to the stats dictionary
    # isn't working as of rn
    def calc_race(self):
        race_mods = self.p_race[self.race]
        print(race_mods)
        stat_list = self.p_stats.keys()
        for i in range(len(race_mods)):
            if race_mods[i] > 0:
                print(race_mods[i])
                arr = list(self.p_stats.keys())
                stat = arr[i]
                self.p_stats.get(stat)[0] += race_mods[i]


        # for key, value in race_mods.items():


    # constructor for setting name
    # need to modify to take more parameters such as race, class
    def __init__(self, name):
        self.name = name

# an object of enemy
# class Enemy(Person):

# an object of an npc that can be interacted with by players, has conversation elements
# class Npc(Person):

