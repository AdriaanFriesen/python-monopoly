import random, time

# list of spaces in the format: [name, [buy price, house price, morgage money], [no set, complete set, 1 house, 2 houses, 3 houses, 4 houses, hotel]] for regular properties, [name, [buy price, morgage money], [if 1 owned, 2 owned, 3 owned, 4 owned]] for railroads, and [name, [tax due]] for taxes. all others are done with separate data.
spaces = {0: ["GO"], 1: ["Mediterranean Avenue", [60, 50, 30], [2, 4, 10, 30, 90, 160, 250]], 2: ["Community Chest"], 3: ["Baltic Avenue", [60, 50, 30], [4, 8, 20, 60, 180, 320, 450]], 4: ["Income Tax", [200]], 5: ["Reading Railroad", [200, 100], [25, 50, 100, 200]], 6: ["Oriental Avenue", [100, 50, 50], [6, 12, 30, 90, 270, 400, 550]], 7: ["Chance"], 8: ["Vermont Avenue", [100, 50, 50], [6, 12, 30, 90, 270, 400, 550]], 9: ["Connecticut Avenue", [120, 50, 60], [8, 16, 40, 100, 300, 450, 600]], 10: ["Jail", [50]], 11: ["St. Charles Place", [140, 100, 70], [10, 20, 50, 150, 450, 625, 750]], 12: ["Electric Company", [150, 75]], 13: ["States Avenue", [140, 100, 70], [10, 20, 50, 150, 450, 625, 750]], 14: ["Virginia Avenue", [160, 100, 80], [12, 24, 60, 180, 500, 700, 900]], 15: ["Pennsylvania Railroad", [200, 100], [25, 50, 100, 200]], 16: ["St. James Place", [180, 100, 90], [14, 28, 70, 200, 550, 750, 950]], 17: ["Community Chest"], 18: ["Tennessee Avenue", [180, 100, 90], [14, 28, 70, 200, 550, 750, 950]], 19: ["New York Avenue", [200, 100, 100], [16, 32, 80, 220, 600, 800, 1000]], 20: ["Free Parking"], 21: ["Kentucky Avenue", [220, 150, 110], [18, 36, 90, 250, 700, 875, 1050]], 22: ["Chance"], 23: ["Indiana Avenue", [220, 150, 110], [18, 36, 90, 250, 700, 875, 1050]], 24: ["Illinois Avenue", [240, 150, 120], [20, 40, 100, 300, 750, 925, 1100]], 25: ["B&O Railroad", [200, 100], [25, 50, 100, 200]], 26: ["Atlantic Avenue", [260, 150, 130], [22, 44, 110, 330, 800, 975, 1150]], 27: ["Ventnor Avenue", [260, 150, 130], [22, 44, 110, 330, 800, 975, 1150]], 28: ["Water Works", [150, 75]], 29: ["Marvin Gardins", [280, 150, 140], [24, 48, 120, 360, 850, 1025, 1200]], 30: ["Go To Jail"], 31: ["Pacific Avenue", [300, 200, 150], [26, 52, 130, 390, 900, 1100, 1275]], 32: ["North Carolina Avenue", [300, 200, 150], [26, 52, 130, 390, 900, 1100, 1275]], 33: ["Community Chest"], 34: ["Pennsylvania Avenue", [320, 200, 160], [28, 56, 150, 450, 1000, 1200, 1400]], 35: ["Short Line", [200, 100], [25, 50, 100, 200]], 36: ["Chance"], 37: ["Park Place", [350, 200, 175], [35, 70, 175, 500, 1100, 1300, 1500]], 38: ["Luxury Tax", [100]], 39: ["Boardwalk", [400, 200, 200], [50, 100, 200, 600, 1400, 1700, 2000]]}
normalSpaces = [1, 3, 6, 8, 9, 11, 13, 14, 16, 18, 19, 21, 23, 24, 26, 27, 29, 31, 32, 34, 37, 39]
railroads = [5, 15, 25, 35]
chests = [2, 17, 33]
chances = [7, 22, 36]
taxes = [4, 38]
utilities = [12, 28]
playerList = list()

def userInput(prompt, numberOfChoices):
    error = True
    while error:
        errored = False
        try:
            choice = int(input(prompt))
        except ValueError:
            input("Input a number 1-" + str(numberOfChoices) + ".\nPress enter to try again.")
            errored = True
        if not errored and isinstance(choice, int) and (choice > numberOfChoices or choice < 1):
            input("Input a number 1-" + str(numberOfChoices) + ".\nPress enter to try again.")
        elif not errored:
            error = False
    return(choice)

def clr(lines = 150):
    print ("\n" * lines)


class Board:
    def __init__(self):
        self.money = 20580
        self.houses = 32
        self.hotels = 12
        self.choice = int()
        self.playerNames = list()
        self.auctionPlayers = list()
        self.auctionTemp = int()
        self.auctionIndex = int()
        self.auctionPrice = int()

    def auction(self, property, auctioneer):
        self.auctionPlayers = list()
        # self.auctionPlayers.append(playerList.index(auctioneer) + 1)
        self.auctionTemp = playerList.index(auctioneer) + 1
        while self.auctionTemp <= len(playerList):
            self.auctionPlayers.append(self.auctionTemp)
            self.auctionTemp += 1
        self.auctionTemp = 1
        while self.auctionTemp != playerList.index(auctioneer) + 1:
            self.auctionPlayers.append(self.auctionTemp)
            self.auctionTemp += 1
        input(auctioneer.name + " is auctioning " + spaces[property][0] + " for a starting price of $10!")
        self.auctionPrice = 10
        while len(self.auctionPlayers) > 1:
            # print(auctioneer.name, spaces[property][0], str(self.auctionPlayers), str(self.auctionPrice), str(self.auctionIndex), str(self.auctionTemp))
            self.auctionIndex = 0
            while len(self.auctionPlayers) > 1 and self.auctionIndex < len(self.auctionPlayers):
                # print("\n" * 150)
                # print(self.auctionPlayers, self.auctionIndex)
                self.choice = userInput(playerList[self.auctionPlayers[self.auctionIndex] - 1].name + ", the current price is $" + str(self.auctionPrice) + "! How much more would you like to bid? (you would have $" + str(playerList[self.auctionPlayers[self.auctionIndex] - 1].money - self.auctionPrice) + " left if you were to win the auction now.)\n1 - 1\n2 - 10\n3 - 100\n4 - drop out\n", 4)
                if self.choice == 1 and playerList[self.auctionPlayers[self.auctionIndex] - 1].money >= self.auctionPrice + 1:
                    self.auctionPrice += 1
                elif self.choice == 2 and playerList[self.auctionPlayers[self.auctionIndex] - 1].money >= self.auctionPrice + 10:
                    self.auctionPrice += 10
                elif self.choice == 3 and playerList[self.auctionPlayers[self.auctionIndex] - 1].money >= self.auctionPrice + 100:
                    self.auctionPrice += 100
                elif self.choice == 4:
                    input(playerList[self.auctionPlayers[self.auctionIndex] - 1].name + " has dropped out of the auction.")
                    del self.auctionPlayers[self.auctionIndex]
                if self.choice != 4:
                    self.auctionIndex += 1
        playerList[self.auctionPlayers[0] - 1].money -= self.auctionPrice
        self.money += self.auctionPrice
        playerList[self.auctionPlayers[0] - 1].append(property)
        input(playerList[self.auctionPlayers[0] - 1].name + " has won the auction! They get " + spaces[property][0] + " for $" + str(self.auctionPrice) + ".")
                
    def gameStart(self):
        self.choice = userInput("How many players are playing? (max 8)\n", 8)
        clr()
        for instance in range(1, self.choice + 1):
            self.playerNames.append(str(input("What is player " + str(instance) + "'s name?\n")))
            clr()
        for player in self.playerNames:
            player = Player(player)
            self.money -= 1500

class Player:
    def __init__(self, newName):
        self.name = newName
        self.money = 1500
        self.consecutiveDoubles = 0
        self.prevRoll = 0
        self.currRoll = 0
        self.prevSpace = 0
        self.currSpace = 0
        self.properties = list()
        self.inJail = False
        self.canBuy = False
        self.choice = int()
        self.owesTo = None
        self.auctionMoney = int()
        playerList.append(self)


    def salaryCheck(self):
        if self.prevSpace > self.currSpace and not self.inJail:
            self.money += 200
     
    def rollDice(self):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        if roll1 == roll2:
            self.consecutiveDoubles += 1

    def jailCheck(self):
        if self.currSpace == 30 or self.consecutiveDoubles == 3:
            self.inJail = True
            self.currSpace = 10
    
    def land(self):
        if self.currSpace in normalSpaces:
            self.canBuy = True
            for player in playerList:
                if self.currSpace in player.properties:
                    self.canBuy = False
            if self.canBuy == True:
                self.choice = userInput(self.name + ", what would you like to do with this unowned property? (you currently have $" + str(self.money) + ")\n1 - buy for $" + str(spaces[self.currSpace][1][0]) + "\n2 - auction\n3 - do nothing\n", 3)
                clr()
                if self.choice == 1:
                    self.properties.append(self.currSpace)
                    self.money -= spaces[self.currSpace][1][0]
                    playingBoard.money += spaces[self.currSpace][1][0]
                elif self.choice == 2:
                    playingBoard.auction(self.currSpace, self)
            else:
                for player in playerList:
                    if self.currSpace in player.properties:
                        self.owesTo = player
                        input("You owe " + self.owesTo.name + " $" + str(spaces[self.currSpace][2][0]) + ".") # todo: add detection for sets and houses/hotels
                        

clr()
playingBoard = Board()
# me = Player("me")
# me.currSpace = 3
# me.land()
# you = Player("you")
# you.properties = [3]
playingBoard.gameStart()
# print("\n" * 10)
# for player in playerList:
#     print(player.name)
# print(playingBoard.money)
# print("\n" * 10)
# print(playerList)
# input()
playerList[3].currSpace = 3
playerList[2].properties.append(3)
playerList[3].land()