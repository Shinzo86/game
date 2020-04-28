##import new_character #imports new_character class
import os.path 
global player_select
'''
check_for_file = os.path.isfile("player_profile1.txt")) #returns true or false if file does or doesn't exit
if check_for_file == True:

    print("Which character would you like to load?")
    print("(W) Warrior")
    print("(S) Wizard")
    print("(R) Ranger")
    choice = input("?")
    if choice == "w":
        while x != ".":
            read
        player.character = load_character(player)
        
    



else:
    player = new_character(player_id, player_class)
'''

class MyClass:
    def __init__(self, chosen_class):
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
    Ability_2_Damage = Attack + Level + Speed
    
class Monster:
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

def FightSimulator(player, monster):
    monster_hp = monster.Strength * 10
    player_hp = player.strength * 10
    print("***WARNING MONSTER APPROACHES!!!***\n")
    print("You have encountered a Monster!\n")
    if player.speed > monster.Speed:
        print("You are faster than the monster!\nYou attack first!\n")
        turn = True
    else:          
        print("The monster is faster than you and they attack first!")
        turn = False
    
    while monster_hp > 0 or player_hp > 0:
        if turn == True:            
            choice = int(input("1) Attack\n2) " + 
                      player.ability_1_text + "\n3) " +
                      player.ability_2_text + "\n"))
            if choice == 1:
                turn_damage = player.attack
                monster_hp = monster_hp - turn_damage
                print("You hit the monster for", 
                       turn_damage, 
                       " damage!")
                
            elif choice == 2:
                turn_damage = player.ability_1_damage
                monster_hp = monster_hp - turn_damage
                print("You hit the monster for",
                      turn_damage,
                      " damage!")
                      
            elif choice == 3:
                turn_damage = player.ability_2_damage
                monster_hp = monster_hp - turn_damage
                print("You hit the monster for",
                      turn_damage,
                      " damage!")            
            else:
                print("Invalid choice")
                
            if monster_hp <= 0:
                break
            else:
                turn = False
        else:
            turn_damage = Monster.Attack
            print("The monster attacks you for",
                  turn_damage,
                  " damage!\n")
            player_hp = player_hp - turn_damage
            print("You have",
                  player_hp,
                  " health left!")
            if player_hp == 0:
                break
            else:
                turn = True
            
    if player_hp > monster_hp:
        return True
    else:
        return False
            
def select_class():
    class_choices = {1: Wizard, 2: Warrior, 3: Ranger}
    initial_class_selection = int(input("1) Wizard\n2) Warrior\n3) Ranger\nChoose your class: "))
    print(f"Your selection is {class_choices[initial_class_selection].class_name}!")

    return MyClass(class_choices[initial_class_selection])

        
player = select_class()

print("Would you like to batlle?")
choice = input("(Y) Yes or (N) No\n")

if choice == "y":
    outcome = FightSimulator(player, Monster)
    if outcome == True:
        print("Congratulations on winning your first fight")
    else:
        print("Why'd you lose?")

