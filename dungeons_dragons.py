import random

mob_list = ["Goblin", "Naga", "Human", "Bandit", "White Walker",
            "Twin-headed Orc", "Flaming Tree Bandit", "Blue-Eyed Dragon",
            "Jehovah"]

item_drop_easy = ["Health Potion", "(Weapon): Wooden Sword", "(Weapon): Shoddy Axe"]
item_drop_medium = ["Health Potion(med)", "(Weapon): Battle Sword", "(Weapon): Flame Scepter"]
item_drop_rare = ["Health Potion(Full)", "Ring of Force", "Sleiphnir"]
#Items
class Item(object):
    def __init__(self, name, item_type):
        self.name = name
        self.item_type = None
    def set_item_type(self):
        if self.name.startswith("Health Potion"):
            self.item_type = "consumable"
        if self.name.startswith("(Weapon"):
            self.item_type = "weapon"
        if self.name.startswith("Ring of F") or self.name.startswith("Slei"):
            self.item_type = "OP"
                                
    

#Class
class Class(object):
    __slots__ = ["name", "class_name", "hp", "dmg", "skills", "inventory"]
    def __init__(self, name, class_name):
        self.name = name
        self.class_name = class_name
        self.hp = 0
        self.dmg = random.randint(2,15)
        self.skills = []
        self.inventory = []
    def set_hp(self):
        if class_name.lower() == "thief" or class_name.lower() == "archer" or class_name.lower() == "mage":
            self.hp = random.randint(2,10)
        elif class_name.lower() == "warrior":
            self.hp = random.randint(5,15)
    def battle(self, mob):
        if self.hp <= 0:
            return "I'm dead!"
        print "\n{} vs. {}".format(self.name, mob.name)
        print "{} deals {} dmg to {}".format(self.name, self.dmg, mob.name)
        mob.hp = mob.hp-self.dmg
        if mob.hp <= 0:
            mob.hp = 0
            self.inventory.append(mob.drops)
            print "found {} on {}'s body!".format(mob.drops, mob.name)
            return "{} is dead.".format(mob.name)
        print "{} has {} hp left.".format(mob.name, mob.hp)
    def print_things(self):
        try:
            if self.hp == 0:
                print "You are dead! Wait for someone to resurrect you!"
                return
            print "Name: {} Class: {}".format(self.name, self.class_name)
            print "HP: {}  DMG {}".format(self.hp,self.dmg)
            if len(self.skills) == 0:
                print "No skills currently learned"
            else:
                print "Your current skills: {}".format(self.skills)
            if len(self.inventory) == 0:
                print "You have no items"
            else:
                print "Items: {}".format(self.inventory)
        except:
            print "Error during print"
#Mob class
class Mob(object):
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.is_boss = False
        self.hp = 0
        self.dmg = 0
        self.drops = []
    def battle(self, character):
        if self.hp <= 0:
            return "{} is dead.".format(self.name)
        print "{} deals {} dmg to {}.".format(self.name, self.dmg, character.name)
        character.hp = self.dmg - character.hp
        if character.hp <= 0:
            character.hp = 0
            return "{} is dead.".format(mob.name)
        print "{} has {} hp left.".format(character.name, character.hp)
        
    def init_mob(self):
        self.set_drops()
        self.set_hp()
        self.set_dmg()
        
    def set_drops(self):
        item_roll = random.randint(0,10)
        if self.difficulty == "easy":
            if item_roll <= 2:
                self.drops = item_drop_medium[random.randint(0,len(item_drop_medium)-1)]
            elif item_roll > 9:
                self.drops = item_drop_rare[random.randint(0,len(item_drop_rare)-1)]
            else:
                self.drops = item_drop_easy[random.randint(0,len(item_drop_easy)-1)]
        elif self.difficulty == "med":
            if item_roll <= 2:
                self.drops = item_drop_easy[random.randint(0,len(item_drop_easy)-1)]
            elif item_roll > 9:
                self.drops = item_drop_rare[random.randint(0,len(item_drop_rare)-1)]
            else:
                self.drops = item_drop_medium[random.randint(0,len(item_drop_medium)-1)]

        elif self.difficulty == "hard":
            if item_roll <= 2:
                self.drops = item_drop_medium[random.randint(0,len(item_drop_medium)-1)]
            elif item_roll > 9:
                self.drops = item_drop_easy[random.randint(0,len(item_drop_easy)-1)]
            else:
                self.drops = item_drop_rare[random.randint(0,len(item_drop_rare)-1)]

        if self.is_boss == True:
            self.drops.append(item_drop_rare[random.randint(0,len(item_drop_rare)-1)])
            self.drops.append(item_drop_rare[random.randint(0,len(item_drop_rare)-1)])
    
    def set_hp(self):       
        if self.difficulty == "easy":
            self.hp = random.randint(8,20)
        elif self.difficulty == "med":
            self.hp = random.randint(25,50)
        elif self.difficulty == "hard":
            self.hp = random.randinit(75,120)
        if self.is_boss == True:
            self.hp *= 2.5
    def set_dmg(self):       
        if self.difficulty == "easy":
            self.dmg = random.randint(2, 12)
        elif self.difficulty == "med":
            self.dmg = random.randint(4,18)
        elif self.difficulty == "hard":
            self.dmg = random.randinit(8,26)
        if self.is_boss == True:
            self.dmg *= 1.65
    def print_mob(self):
        print "Name: {}\nDifficulty: {}".format(self.name, self.difficulty)
        print "HP: {} Dmg: {}".format(self.hp, self.dmg)
    


def start_game(character_list):
    welcome_str = character_list[0].name
    for char in character_list[1:]:
        welcome_str += "," + char.name
    return welcome_str
            
if __name__ == "__main__":
    fight_count = 0
    num_players = int(raw_input("Input number of players: "))
    character_list = []
    for i in range(num_players):
        user = raw_input("Input player {}'s name: ".format(i+1))
        print "_______________"
        print "Character List:\nWarrior\nMage\nThief\nArcher"
        print "_______________"
        class_name = raw_input("What class do you wish to play as: ")
        #create class and assign stats, print outcome
        if class_name.lower() in ("thief", "archer", "mage", "warrior"):
            character = Class(user, class_name)
            character.set_hp()
        else:
            break
        character.print_things
        character_list.append(character)
    
    print "Best of luck on your journey {}".format(start_game(character_list))
    #randomly generate mobs that get stronger every fight
    difficulty = "easy"
    
    player_turn = random.randint(0,len(character_list)-1)

    #switch turns
    while player_turn < len(character_list):
        player_turn += 1
        if player_turn == len(character_list):
            player_turn = 0

        mob = Mob(mob_list[random.randint(0, len(mob_list)-1)], difficulty)
        print "You're fighting a {}".format(mob.name)
        #print mob stuff
        mob.init_mob()
        mob.print_mob()
        while mob.hp > 0:
            character_list[player_turn].battle(mob)
            print"\nAfter Battle Info!"
        character_list[player_turn].print_things()
        #show command list
        fight_again = raw_input("\nFight again? (Y/N)")
        
        if fight_again.upper() == "Y":
            fight_count += 1
        else:
            break


           
