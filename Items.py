class Items:
    name = "null"
    hex_code = 0


class Weapons(Items):
    damage = 0
    weapon_type = "null"


class Currency(Items):
    platinum_coin = 0
    electrum_coin = 0
    gold_coin = 0
    silver_coin = 0
    copper_coin = 0
    # needs to be FINISHED, adds all the coins together into copper coins, used for price checking
    # could check based on highest coin and whether or not you have one equal or higher
    total_coins = platinum_coin * 1000 + electrum_coin + gold_coin + silver_coin + copper_coin

    # initializes a starting value of copper coins for a player, the amount will automatically be shuffles
    def __init__(self, copper_coins):
        self.copper_coin = copper_coins
        self.shuffle_money()

    # a to string method that neatly prints out the amount of each coins the player has
    def __str__(self):
        return "pp: {} ep: {} gp: {} sp: {} cp: {} ".format(self.platinum_coin, self.electrum_coin, self.gold_coin, self.silver_coin, self.copper_coin)

    # can be used to add or subtract money from player
    def add_money(self, plat, elec, gold, silv, copp):
        self.platinum_coin += plat
        self.electrum_coin += elec
        self.gold_coin += gold
        self.silver_coin += silv
        self.copper_coin += copp
        self.shuffle_money()

    # when subtracting tests if there's enough money to pay a shop/person
    def is_enough_money(self, price):
        if price > self.total_coins:
            return False
        else:
            return True

    # converts all money to their best valued coin, some values may be incorrect
    # called everytime money is added or subtracted from a player
    def shuffle_money(self):
        copp = self.copper_coin
        if copp >= 100:
            self.silver_coin += copp / 100
            self.copper_coin = copp % 100
        silv = self.silver_coin
        if silv >= 100:
            self.gold_coin += silv / 100
            self.silver_coin = silv % 100
        gold = self.gold_coin
        if gold >= 100:
            self.electrum_coin += gold / 100
            self.gold_coin = gold % 100
        elec = self.electrum_coin
        if elec >= 100:
            self.platinum_coin += elec / 100
            self.electrum_coin = elec % 100

