#Create player_profile.txt

import create_new_character
class new_character:
    def __init__(self, 
                 player_id, 
                 player_class):
        print("Please select a character to view stats:")
        print("1) Wizard")
        print("2) Ranger")
        print("3) Warrior")
        choice = input("?")
        print()
    
        if choice == "1":
            player_class = "Wiz"
            print("Wizard, a caster who specializes in AOE (Area of Effect) damage")
            print()
            print("Stats     :")
            print("Strength  :  1")
            print("Defense   :  1")
            print("M. Defense:  1")
            print("Attack    :  5")
            print("Magic     :  10")
            print("Speed     :  1")
            print("Luck      :  1")
            print("Crit Rate :  75%")
            print("Crit Dmg  :  100%")
            print("Accuracty :  75%")
            print("Evasion   :  35%")
            print("Dodge     :  50%")
            
            x = True
            while x == True:
                print()
                print("Select (a) to go back or (s) to select")
                choice = input("?")
                
                if choice == "a":
                    player = new_character()
                    
                elif choice == "s":
                    print("Are you sure you would like to select the ", player_class, "?")
                    choice = input("(y)es or (n)o")
                    if choice == "y":
                        player = create_new_character(player_id, 
                                                      player_class)
                        x = False                                          
                else:
                    print("INVALID CHOICE")
        
        elif choice == "2":
            player_class = "Ran"
            print("Ranger, a quick physical attacker that specializes ")
            print("in Dodge and Critical Damage")
            print()
            print("Stats     :")
            print("Strength  :  1")
            print("Defense   :  1")
            print("M. Defense:  1")
            print("Attack    :  5")
            print("Magic     :  1")
            print("Speed     :  10")
            print("Luck      :  1")
            print("Crit Rate :  50%")
            print("Crit Dmg  :  150%")
            print("Accuracty :  50%")
            print("Evasion   :  30%")
            print("Dodge     :  35%")
            
            x = True
            while x == True:
                print()
                print("Select (a) to go back or (s) to select")
                choice = input("?")
                
                if choice == "a":
                    player = new_character()
                    
                elif choice == "s":
                    print("Are you sure you would like to select the ", player_class, "?")
                    choice = input("(y)es or (n)o")
                    if choice == "y":
                        player = create_new_character(player_id,
                                                      player_class)
                        x = False                                            
                else:
                    print("INVALID CHOICE")
        
        elif choice == "3":
            player_class = "War"
            print("Warrior, a tough physical attacker that ")
            print("specializes in status effects")
            print()
            print("Stats     :")
            print("Strength  :  5")
            print("Defense   :  5")
            print("M. Defense:  5")
            print("Attack    :  2")
            print("Magic     :  1")
            print("Speed     :  1")
            print("Luck      :  1")
            print("Crit Rate :  50%")
            print("Crit Dmg  :  100%")
            print("Accuracty :  90%")
            print("Evasion   :  35%")
            print("Dodge     :  35%")
            
            x = True
            while x == True:
                print()
                print("Select (a) to go back or (s) to select")
                choice = input("?")
                
                if choice == "a":
                    player = new_character()
                    
                elif choice == "s":
                    print("Are you sure you would like to select the ", player_class, "?")
                    choice = input("(y)es or (n)o")
                    if choice == "y":
                        player = create_new_character(player_id,
                                                      player_class)
                        x = False                                            
                else:
                    print("INVALID CHOICE")
    
                   
