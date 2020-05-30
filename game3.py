class Player:
    def __init__(self, chosen_name = "", player_stat[], exp, is_level_up = false, player_location):
        self.player_name       = chosen_name
        self.player_hp         = get_player_hp(player_stat[1])
        self.player_stat       = get_player_stat(player_stat)
        self.player_exp        = get_player_exp(exp)
        self.level_up          = Level_Up(is_level_up)
        self.player_location   = get_player_location(player_location)
        
    def get_player_hp(self, player_str):
        self.player_hp = player_str * 10
        return(player_hp)

    def get_player_stat(self, player_stat):
        self.level             = player_stat[0]
        self.strength          = player_stat[1]
        self.defense           = player_stat[2]
        self.magic_defense     = player_stat[3]
        self.attack            = player_stat[4]
        self.magic             = player_stat[5]
        self.speed             = player_stat[6]
        self.luck              = player_stat[7]
        self.crit_rate         = player_stat[8]
        self.crit_damage       = player_stat[9]
        self.accuracy          = player_stat[10]
        self.evasion           = player_stat[11]
        self.dodge             = player_stat[12]

    def get_player_location(self, current_location):
        player_location = current_location

    def Level_Up(self, is_level_up):
        if is_level_up == True:
            answer = "n"
            self.level += 1
            skill_points = 3
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
                strength_up      = int(input("Strength? "))
                defense_up       = int(input("Defense? "))
                magic_defense_up = int(input ("Magic Defense? "))
                attack_up        = int(input("Attack? "))
                magic_up         = int(input("Magic? "))
                speed_up         = int(input("Speed? "))
                luck_up          = int(input("Luck? "))
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
            self.strength      += strength_up
            self.defense       += defense_up
            self.magic_defense += magic_defense_up
            self.attack        += attack_up
            self.magic         += magic_up
            self.speed         += speed_up
            self.luck          += luck_up

class PlayerClass:
    def __init__ (self, class_name = "", class_attribute[], class_ability[]):
        self.class_name        = class_name
        self.level             = class_attribute[0]
        self.strength          = class_attribute[1]
        self.defense           = class_attribute[2]
        self.magic_defense     = class_attribute[3]
        self.attack            = class_attribute[4]
        self.magic             = class_attribute[5]
        self.speed             = class_attribute[6]
        self.luck              = class_attribute[7]
        self.crit_rate         = class_attribute[8]
        self.crit_damage       = class_attribute[9]
        self.accuracy          = class_attribute[10]
        self.evasion           = class_attribute[11]
        self.dodge             = class_attribute[12]
        self.ability_1_text    = class_ability[0]
        self.ability_1_damage  = class_ability[1]
        self.ability_2_text    = class_ability[2]
        self.ability_2_damage  = class_ability[3]

player_class = {}
player_class['Wizard']  = PlayerClass("Wizard",
                                     [1, 1, 1, 1, 5, 10, 1, 1, 75, 100, 75, 35, 50],
                                     ["Fire Ball", 5, "Freeze", 5]
                                     )
player_class["Warrior"] = PlayerClass("Warrior",
                                      [1, 5, 5, 5, 2, 1, 1, 1, 50, 100, 90, 35, 35],
                                      ["Defend", 5, "Counter Strike", 5]
                                      )
player_class["Ranger"]  = PlayerClass("Ranger",
                                     [1, 1, 1, 1, 5, 1, 10, 1, 50, 150, 50, 30, 35],
                                     ["Quick Shot", 5, "Arrow Storm", 5]
                                     )
'''                                    
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
'''
    

'''
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
'''

'''
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
''' 