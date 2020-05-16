'''
    class_name = "Wizard"
    Level = Player current level. Used to determine multiple stats.
    HP = Level * Strength
    Strength    
        Stat determines overall HP of monsters and players.
        Will also be used to determine if character can use certain items.
    Defense
        Stat determines Physical Attack damage reduction.
        Total DMG = PA_DMG - Defense
    Magic_Defense
        Stat determines Magic Attack dmg reduction.
        Total DMG = MA_DMG - M. Defense
    Attack
        Stat determines base Physical Attack dmg
        PA_DMG = Attack + Weapon bonus + Skill Bonus
    Magic
        Stat determines base Magic Attack damage
        MG_DMG = Magic + Weapon bonus + Skill Bonus
    Speed
        Stat determines speed of attack bar fill rate
        atk_bar_fill_rate = Speed *.1
    Luck
        Stat determines loot chance rarity after combat ends
        chance_item_drop = luck * 10
        loot_rarity = luck
    Crit_Rate
        Stat determines chance for Critical Strike chance
        chance_crit = Crit_Rate
    Crit_Damage
        Stat determines percentage extra damage if Critical Strike
        Total DMG = (PA_DMG * (Crit_Damage * .01)) + (MA_DMG * (Crit_Damage * .01))
    Accuracy = 75
    Evasion = 35
    Dodge = 50
    Ability_1_Text = "Fire Ball"
    Ability_1_Damage = Magic + Level 
    Ability_2_Text = "Freeze"
    Ability_2_Damage = Magic + Level
'''
import os
import os.path
import random
level_up_max = {
    1 : 10,
    2 : 25,
    3 : 64,
    4 : 160,
    5 : 400,
    6 : 1000,
    7 : 2500,
    8 : 6250,
    9 : 15625,
    10 : 39062
               }

class PlayerOne:
    def __init__(self, chosen_class, chosen_name):
        self.class_name = chosen_class.class_name
        self.level = chosen_class.Level
        self.strength = chosen_class.Strength
        self.defense = chosen_class.Defense
        self.magic_defense = chosen_class.Magic_Defense
        self.attack = chosen_class.Attack
        self.magic = chosen_class.Magic
        self.speed = chosen_class.Speed
        self.luck = chosen_class.Luck
        self.crit_rate = chosen_class.Crit_Rate
        self.crit_damage = chosen_class.Crit_Damage
        self.accuracy = chosen_class.Accuracy
        self.evasion = chosen_class.Evasion
        self.dodge = chosen_class.Dodge
        self.ability_1_text = chosen_class.Ability_1_Text
        self.ability_1_damage = chosen_class.Ability_1_Damage
        self.ability_2_text = chosen_class.Ability_2_Text
        self.ability_2_damage = chosen_class.Ability_2_Damage
        self.player_exp = chosen_class.Player_Exp
        self.player_name = chosen_name
        
    def Level_Up(self):
        answer = "n"
        self.level = self.level + 1
        while answer != "y":
            print("\n-----------LEVEL UP-------------")
            print("\nYou have earned 3 skill points!\n")
            print("\nLevel         :", self.level,
                  "\nStrength      :", self.strength,
                  "\nDefense       :", self.defense,
                  "\nMagic Defense :", self.magic_defense,
                  "\nAttack        :", self.attack,
                  "\nMagic         :", self.magic,
                  "\nSpeed         :", self.speed,
                  "\nLuck          :", self.luck
                 )
            strength_up = int(input("Strength? "))
            defense_up = int(input("Defense? "))
            magic_defense_up = int(input ("Magic Defense? "))
            attack_up = int(input("Attack? "))
            magic_up = int(input("Magic? "))
            speed_up = int(input("Speed? "))
            luck_up = int(input("Luck? "))
            print("\nStrength      +", strength_up,
                  "\nDefense       +", defense_up,
                  "\nMagic Defense +", magic_defense_up,
                  "\nAttack        +", attack_up,
                  "\nMagic         +", magic_up,
                  "\nSpeed         +", speed_up,
                  "\nLuck          +", luck_up,
                 )
            print("\nWould you like to save changes?\n(Y) yes or (N) no")
            answer = input("? ")
        self.strength = self.strength + strength_up
        self.defense = self.defense + defense_up
        self.magic_defense = self.magic_defense + magic_defense_up
        self.attack = self.attack + attack_up
        self.magic = self.magic + magic_up
        self.speed = self.speed + speed_up
        self.luck = self.luck + luck_up

class Wizard:
    class_name = "Wizard"
    Level = 1
    Strength = 1
    Defense = 1
    Magic_Defense = 1
    Attack = 5
    Magic = 10
    Speed = 1
    Luck = 1
    Crit_Rate = 75
    Crit_Damage = 100
    Accuracy = 75
    Evasion = 35
    Dodge = 50
    Ability_1_Text = "Fire Ball"
    Ability_1_Damage = Magic + Level 
    Ability_2_Text = "Freeze"
    Ability_2_Damage = Magic + Level
    Player_Exp = 0
    
class Warrior:
    class_name = "Warrior"
    Level = 1
    Strength = 5
    Defense = 5
    Magic_Defense = 5
    Attack = 2
    Magic = 1
    Speed = 1
    Luck = 1
    Crit_Rate = 50
    Crit_Damage = 100
    Accuracy = 90
    Evasion = 35
    Dodge = 35
    Ability_1_Text = "Defend"
    Ability_1_Damage = 0
    Ability_2_Text = "Counter"
    Ability_2_Damage = Strength * 2
    Player_Exp = 0

class Ranger:
    class_name = "Ranger"
    Level = 1
    Strength = 1
    Defense = 1
    Magic_Defense = 1
    Attack = 5
    Magic = 1
    Speed = 10
    Luck = 1
    Crit_Rate = 50
    Crit_Damage = 150
    Accuracy = 50
    Evasion = 30
    Dodge = 35
    Ability_1_Text = "Quick Shot"
    Ability_1_Damage = Speed + Attack
    Ability_2_Text = "Arrow Storm"
    Ability_2_Damage = Attack + Speed
    Player_Exp = 0
    
class Monster:
    Level = 1
    Strength = 1
    Defense = 1
    Magic_Defense = 1
    Attack = 1
    Magic = 1
    Speed = 1
    Luck = 1
    Crit_Rate = 10
    Crit_Damage = 10
    Accuracy = 50
    Evasion = 30
    Dodge = 35
    
def Fight_Simulator(Player, Monster):
    os.system("cls")
    monster_hp = Monster.Strength * 10
    player_hp = Player.strength * 10
    print("***WARNING MONSTER APPROACHES!!!***\n")
    print("You have encountered a Monster!\n")
    if Player.speed > Monster.Speed:
        print("You are faster than the monster!\nYou attack first!\n")
        turn = True
    else:          
        print("The monster is faster than you and they attack first!\n")
        turn = False
    
    while monster_hp > 0 or player_hp > 0:
        if turn == True:            
            choice = int(input("1) Attack\n2) " + 
                      Player.ability_1_text + "\n3) " +
                      Player.ability_2_text + "\n"))
            if choice == 1:
                turn_damage = Player.attack
                try_crit = Roll_Dice(Player.crit_rate)
                if try_crit == True:
                    turn_damage = int(turn_damage + ((Player.crit_damage * .01) * turn_damage))
                    print("You hit the monster for", 
                           turn_damage, 
                           " critical damage!\n")
                else:
                    print("You hit the monster for", 
                          turn_damage, 
                          " damage!\n")
                
            elif choice == 2:
                turn_damage = Player.ability_1_damage
                try_crit = Roll_Dice(Player.crit_rate)
                if try_crit == True:
                    turn_damage = int(turn_damage + ((Player.crit_damage * .01) * turn_damage))
                    print("You hit the monster for", 
                           turn_damage, 
                           " critical damage!\n")
                else:
                    print("You hit the monster for", 
                          turn_damage, 
                          " damage!\n")
                      
            elif choice == 3:
                turn_damage = Player.ability_2_damage
                try_crit = Roll_Dice(Player.crit_rate)
                if try_crit == True:
                    turn_damage = int(turn_damage + ((Player.crit_damage * .01) * turn_damage))
                    print("You hit the monster for", 
                           turn_damage, 
                           " critical damage!\n")
                else:
                    print("You hit the monster for", 
                          turn_damage, 
                          " damage!\n")      
            else:
                print("Invalid choice")
            monster_hp = monster_hp - turn_damage                
            print("You have ", player_hp, " left\nThe monster has ", monster_hp, " left\n")
            if monster_hp <= 0:
                break
            else:
                turn = False
        else:
            turn_damage = Monster.Attack
            try_crit = Roll_Dice(Monster.Crit_Rate)
            if try_crit == True:
                turn_damage = int(turn_damage + ((Monster.Crit_Damage * .01) * turn_damage))
                print("The monster hit you for", 
                       turn_damage, 
                       " critical damage!\n")
            else:
                print("The monster hit you for", 
                      turn_damage, 
                      " damage!\n")      
            player_hp = player_hp - turn_damage            
            print("You have ", player_hp, " left\nThe monster has ", monster_hp, " left\n")
            if player_hp == 0:
                break
            else:
                turn = True
            
    if player_hp > monster_hp:
        exp_gain = (Monster.Level * .5) + Monster.Level
        Player.player_exp = Player.player_exp + exp_gain
        print("You gained ", 
               exp_gain, 
               " experience points!\n"
               "You have a total of ", 
               Player.player_exp, 
               " experience points"
              )
        return True
    else:
        return False

'''TODO
Add a way to display stats and description of classes
'''                      
def Select_Class(player_name):
    class_choices = {1: Wizard, 2: Warrior, 3: Ranger}
    initial_class_selection = int(input("1) Wizard\n2) Warrior\n3) Ranger\nChoose your class: "))
    print(f"Your selection is {class_choices[initial_class_selection].class_name}!")
    print("Welcome to Blah Blah,", player_name, "!")
    input("Press a key to continue...")
    return PlayerOne(class_choices[initial_class_selection], player_name)

def Roll_Dice(threshold):
    random_number = random.randint(1, 100)
    if random_number <= threshold:
        return True
    else:
        return False

'''TODO
Story needs to filled out along with all corresponding chapters
'''

def chapter_one_prologue(save):
    

    os.system("cls")
    save["chapter"][1]["started"] = True

    print("<INSERT GAME PROLOGUE>")
    auto_save(save, Player)

def auto_save(save, my_player):
    save["player_stats"] = {
            "class_name"       : my_player.class_name,
            "level"            : my_player.level,
            "strength"         : my_player.strength,
            "defense"          : my_player.defense,
            "magic_defense"    : my_player.magic_defense,
            "attack"           : my_player.attack,
            "magic"            : my_player.magic,
            "speed"            : my_player.speed,
            "luck"             : my_player.luck,
            "crit_rate"        : my_player.crit_rate,
            "crit_damage"      : my_player.crit_damage,
            "accuracy"         : my_player.accuracy,
            "evasion"          : my_player.evasion,
            "dodge"            : my_player.dodge,
            "ability_1_text"   : my_player.ability_1_text,
            "ability_1_damage" : my_player.ability_1_damage,
            "ability_2_text"   : my_player.ability_2_text,
            "ability_2_damage" : my_player.ability_2_damage,
            "player_exp"       : my_player.player_exp,
            "player_name"      : my_player.player_name
            }
    
    # for x in save_data

chapter_one = {
    "started"         : False,
    "main_story"      : False,
    "sub_story_one"   : False,
    "sub_story_two"   : False,
    "sub_story_three" : False
              } 
              
chapter_two = {
    "started"         : False,
    "main_story"      : False,
    "sub_story_one"   : False,
    "sub_story_two"   : False,
    "sub_story_three" : False
              }
    
chapter_three = {
    "started"         : False,
    "main_story"      : False,
    "sub_story_one"   : False,
    "sub_story_two"   : False,
    "sub_story_three" : False
                }
    
chapter_four = {
    "started"         : False,
    "main_story"      : False,
    "sub_story_one"   : False,
    "sub_story_two"   : False,
    "sub_story_three" : False
               } 
    
chapter_five = {
    "started"         : False,
    "main_story"      : False,
    "sub_story_one"   : False,
    "sub_story_two"   : False,
    "sub_story_three" : False
               }   
               
chapter = {
    1 : chapter_one,
    2 : chapter_two,
    3 : chapter_three,
    4 : chapter_four,
    5 : chapter_five
          }            

save_data = {
             "player_name" : None,
             "player_stats" : None,
             "chapter" : chapter
            }   

'''TODO
Main Menu screen needs to updated with Character function and View character function
'''
viewing_main_menu = True
while viewing_main_menu:
    print("Welcome to Blah Blah\n",
          "Main Menu\n",
          "1: Start New Game\n",
          "2: Load Character\n",
          "3: Exit Game\n"
          )
    choice = int(input("? "))
    if choice == 1:
        print("Hello, please select a name.")
        player_name = input()
        Player = Select_Class(player_name)
        chapter_one_prologue(save_data)
        viewing_main_menu = False
    else:
        exit()

    

choice = "y"
while choice != "n":
    print("Would you like to batlle?")
    choice = input("(Y) Yes or (N) No\n")

    if choice == "y":
        outcome = Fight_Simulator(Player, Monster)
        if outcome == True:
            print("You won!\n")
            if Player.player_exp >= level_up_max[Player.level] :
                Player.Level_Up()
        else:
            print("Why'd you lose?\n")
               

            
        