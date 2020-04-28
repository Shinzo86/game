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

class Wizard:
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
    player_hp = player.Strength * 10
    print("***WARNING MONSTER APPROACHES!!!***\n")
    print("You have encountered a Monster!\n")
    if player.Speed > monster.Speed:
        print("You are faster than the monster!\nYou attack first!\n")
        turn = True
    else:          
        print("The monster is faster than you and they attack first!")
        turn = False
    
    while monster_hp > 0 or player_hp > 0:
        if turn == True:            
            choice = int(input("1) Attack\n2)" + 
                      player.Ability_1_Text + "\n3)" +
                      player.Ability_2_Text + "\n"))
            if choice == 1:
                turn_damage = player.Attack
                monster_hp = monster_hp - turn_damage
                print("You hit the monster for ", 
                       turn_damage, 
                       " damage!")
                turn = False
                check_current_health(player_hp, monster_hp)    
            elif choice == 2:
                turn_damage = player.Ability_1_Damage
                monster_hp = monster_hp - turn_damage
                print("You hit the monster for ",
                      turn_damage,
                      " damage!")
                turn = False
                check_current_health(player_hp, monster_hp)
            elif choice == 3:
                turn_damage = player.Ability_2_Damage
                monster_hp = monster_hp - turn_damage
                print("You hit the monster for ",
                      turn_damage,
                      " damage!")
                turn = False
                check_current_health(player_hp, monster_hp)               
            else:
                print("Invalid choice")
        
        else:
            turn_damage = Monster.Attack
            print("The monster attacks you for ",
                  turn_damage,
                  " damage!\n")
            player_hp = player_hp - turn_damage
            print("You have ",
                  player_hp,
                  " health left!")
            check_current_health(player_hp, monster_hp)
            turn = True

def check_current_health(player_hp, monster_hp):
    if player_hp > monster_hp:
        return True
    else:
        return False
                
class SelectClass:
    def __init__(self):
        initial_class_selection = input("1) Wizard\n2) Warrior\n3) Ranger\nChoose your class: ")
        print(f"Your selection is {initial_class_selection}!")
        if initial_class_selection == "1":
            initial_class = Wizard
        elif initial_class_selection == "2":
            initial_class = Warrior
        elif initial_class_selection == "3":
            initial_class = Ranger
            
        print("Would you like to batlle?")
        choice = input("(Y) Yes or (N) No\n")

        if choice == "y":
            outcome = FightSimulator(initial_class, Monster)
            if outcome == True:
                print("Congratulations on winning your first fight")
            else:
                print("Why'd you lose?")
                    


player = SelectClass()

