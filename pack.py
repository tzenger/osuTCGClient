import math
import random
global common
global uncommon
global rare
common = {"GamingChair", "HigherScore", "RobStare", "BrainPower", "Swag", "Bide", "Stonks", "AscensionToHeaven", "Cultist", "ChangeOfPlans", "MikuBuff", "EcoRound", "HandOfAcillac", "JazzIsRad", "ChungisIsServed", "MasterOfLightning", "ComebackKid", "CaffeinePill"}
uncommon = {"Jester", "BossRush", "Safeguard", "Vanilla", "DifficultyAdjust", "Powerball", "Mirror", "RedPill", "SolarSystem", "TheIdiotStick", "Maestro", "ArtAppreciation", "Heist", "Endgame", "Chaos"}
rare = {"PointBottle", "TrickHand", "Equality", "TheSeer", "3636PakaPesos", "Psuedohost", "BluePill", "SaucedSpirit", "AlchemicalForge", "Smuggler", "DomainExpansion"}


# NOT USING THIS CLASS
class Card:
    def __init__(cardName, rarity, pattern):
        # 0 - common
        # 1 - uncommon
        # 2 - rare
        rarity = -1

        # 0 - none
        # 1 - holo
        # 2 - poly
        pattern = -1
        cardName = ""

# packType:
# 0 - Mini Pack
# 1 - Jumbo Pack
# 2 - Mega Pack

def checkHolo(packType, wins):
    if(packType == 0):
        return random.randint(1, 101) < (8 * (wins+1))
    elif(packType == 1):
        return random.randint(1, 101) < (12 * (wins+1))
    else:
        return random.randint(1, 101) < (24 * (wins+1))

def checkPoly(packType, wins):
    if(packType == 0):
        return random.randint(1, 101) < (2 * (wins+1))
    elif(packType == 1):
        return random.randint(1, 101) < (3 * (wins+1))
    else:
        return random.randint(1, 101) < (6 * (wins+1))
    
def rollSingle():
    collection = common + uncommon + rare
    return random.choice(list(collection)) + ".png"

def rollMiniPack(wins):
    packType = 0
    numRolls = 3
    pack = []
    obtained = {}
    for i in range(numRolls):
        randNum = random.randint(1, 101)
        # Roll for pattern-type
        Sheen = 0
        if(checkHolo(packType, wins)):
            Sheen = 1
        if(checkPoly(packType, wins)):
            Sheen = 2
        
        # Common Rolls (70%)
        if(randNum <= 70):
            card = random.choice(list(common)) + ".png"
            while(card in obtained):
                card = random.choice(list(common)) + ".png"
            obtained[card] = True
            pack.append((card, 0, Sheen))
            
        # Uncommon Rolls (25%)
        elif(randNum > 70 and randNum <= 95):
            card = random.choice(list(uncommon)) + ".png"
            while(card in obtained):
                card = random.choice(list(uncommon)) + ".png"
            obtained[card] = True
            pack.append((card, 1, Sheen))

            
        # Rare Rolls (5%)
        else:
            card = random.choice(list(rare)) + ".png"
            # reroll common card to avoid dupes
            while(card in obtained):
                card = random.choice(list(rare)) + ".png"
            obtained[card] = True
            pack.append((card, 2, Sheen))
    return pack
    


def rollJumboPack(wins):
    packType = 1
    numRolls = 5
    pack = []
    obtained = {}
    for i in range(numRolls):
        randNum = random.randint(1, 1001)
        # Roll for pattern-type
        Sheen = 0
        if(checkHolo(packType, wins)):
            Sheen = 1
        if(checkPoly(packType, wins)):
            Sheen = 2


        # Common Rolls
        if(randNum <= 650):
            card = random.choice(list(common)) + ".png"
            while(card in obtained):
                card = random.choice(list(common)) + ".png"
            obtained[card] = True
            pack.append((card, 0, Sheen))
            
        # Uncommon Rolls (25%)
        elif(randNum > 650 and randNum <= 900):
            card = random.choice(list(uncommon)) + ".png"
            while(card in obtained):
                card = random.choice(list(uncommon)) + ".png"
            obtained[card] = True
            pack.append((card, 1, Sheen))

            
        # Rare Rolls (10%)
        else:
            card = random.choice(list(rare)) + ".png"
            # reroll common card to avoid dupes
            while(card in obtained):
                card = random.choice(list(rare)) + ".png"
            obtained[card] = True
            pack.append((card, 2, Sheen))

    return pack


def rollMegaPack():
    packType = 2
    numRolls = 5
    pack = []
    obtained = {}
    for i in range(numRolls):
        randNum = random.randint(1, 101)
        # Roll for pattern-type
        Sheen = 0
        if(checkHolo(packType, 0)):
            Sheen = 1
        if(checkPoly(packType, 0)):
            Sheen = 2
        
        if(i == 0):
            card = random.choice(list(rare)) + ".png"
            while(card in obtained):
                card = random.choice(list(rare)) + ".png"
            obtained[card] = True
            pack.append((card, 2, Sheen))
            
        else:
            # Common Rolls (70%)
            if(randNum <= 65):
                card = random.choice(list(common)) + ".png"
                while(card in obtained):
                    card = random.choice(list(common)) + ".png"
                obtained[card] = True
                pack.append((card, 0, Sheen))    
                    
            # Uncommon Rolls (25%)
            elif(randNum > 65 and randNum <= 90):
                card = random.choice(list(uncommon)) + ".png"
                while(card in obtained):
                    card = random.choice(list(uncommon)) + ".png"
                obtained[card] = True
                pack.append((card, 1, Sheen))
                
            # Rare Rolls (5%)
            else:
                card = random.choice(list(rare)) + ".png"
                while(card in obtained):
                    card = random.choice(list(rare)) + ".png"
                obtained[card] = True
                pack.append((card, 2, Sheen))
    return pack
