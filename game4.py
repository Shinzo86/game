import operator

class MapGroup:
    def __init__(self, map_id, room_dict):
        self.map_id = map_id
        self.rooms = room_dict
        self.room_coord_list = self._get_all_room_coords()
        self.bound_x, self.bound_y = self._get_bounds()
        self.map = self._build_map(self.bound_x, self.bound_y)
    
    def _get_all_room_coords(self):
        coord_list = []
        for room in self.rooms.values():
            coord_list.append((room.coord_x - 1, room.coord_y - 1))

        return coord_list

    def draw_map(self):
        self._get_player_pos()
        for row in range(self.bound_y + 1):
            map_str = ""
            for col in range(self.bound_x + 1):
                map_str += self.map[row][col]
            print(map_str)
                        
    def _build_map(self, index_x, index_y):
        temp_dict = {}
        for row in range(index_y + 1):
            temp_dict[row] = []
            for col in range(index_x + 1):
                if (col, row) in self.room_coord_list:
                    temp_dict[row].append("[ ]")
                else:
                    temp_dict[row].append("   ")

        return temp_dict

    def _get_player_pos(self):
        for room in self.rooms.values():
            if room.player_in_room:
                self.map[room.coord_y - 1][room.coord_x - 1] = "[x]"
            else:
                self.map[room.coord_y - 1][room.coord_x - 1] = "[ ]"

    def _get_bounds(self):
        
        return (max(self.room_coord_list)[0], max(self.room_coord_list, key=operator.itemgetter(1))[1])

    @staticmethod
    def generate_map(map_name):
        room_dict = {}
        # for row in range(y):
        #     for col in range(x):
        #         room_dict[(col,row)] = Room()
        room_dict[map_name] = Room(map_name,
                         "Not Hostile",
                         [False, False, False, False],
                         1,1
                        )

        return MapGroup(map_name, room_dict)



class Room:
    def __init__ (self, name = "", environment = "", links = [], room_coord_x=-1, room_coord_y=-1):
        self.name          = name
        self.environment   = environment
        self.north         = links[0]
        self.south         = links[1]
        self.east          = links[2]
        self.west          = links[3]

        self.coord_x  = room_coord_x
        self.coord_y  = room_coord_y

        self.player_in_room = False
        
    def display_paths(self):
        if self.north != False:
            print(f"There is a path to the north in {self.name}")
        
        if self.south != False:
            print(f"There is a path to the south in {self.name}")
        
        if self.east != False:
            print(f"There is a path to the east in {self.name}")
            
        if self.west != False:
            print(f"There is a path to the west in {self.name}")
    
    def _leave_room(self):
        self.player_in_room = False

    def _enter_room(self):
        self.player_in_room = True




class Player:
    def __init__(self, chosen_name="", player_stat=[], player_location=None, inventory=[]):
        self.player_name       = chosen_name
        self.player_hp         = player_stat[1] * 10
        self.get_player_stat(player_stat)
        self.player_exp        = 0
        self.player_location   = player_location
        self.inventory         = inventory

        self.player_location._enter_room()  

        
        
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

    def change_room(self, dest_room):
        self.player_location._leave_room()
        self.player_location = dest_room
        self.player_location._enter_room()

    def level_up(self):
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
            magic_defense_up = int(input("Magic Defense? "))
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

    def get_player_location(self, current_location):
        player_location = current_location

    def get_inventory(self):
        return(self.inventory)

class PlayerClass:
    def __init__ (self, class_name = "", class_attribute=[], class_ability=[]):
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

world = {} 
world['MainRoom'] = Room("MainRoom",
                         "Not Hostile",
                         ["Room_A", "Room_C", "Room_D", "Room_B"],
                         2,2
                        )
world["Room_A"] = Room("Room A",
                       "Hostile",
                       [False, "MainRoom", False, False],
                       2,1
                      )
world["Room_B"] = Room("Room B",
                       "Not Hostile",
                       [False, False, "MainRoom", False],
                       1,2
                      )
world["Room_C"] = Room("Room_C",
                       "Hostile",
                       ["MainRoom", False, False, False],
                       2,3
                      )
world["Room_D"] = Room("Room_D",
                       "Not Hostile",
                       [False, False, False, "MainRoom"],
                       3,2
                      )

starting_map = MapGroup("starting_map", world)

forest_map = MapGroup.generate_map("underground")


# player = Player(
#         "Boshi",
#         [1, 1, 1, 1, 5, 1, 10, 1, 50, 150, 50, 30, 35],
#         starting_map.rooms["MainRoom"])

player = Player(
        "Boshi",
        [1, 1, 1, 1, 5, 1, 10, 1, 50, 150, 50, 30, 35],
        forest_map.rooms["underground"])

leaving = False
while not leaving:
    player.player_location.display_paths()
    print("You are currently in:\n",
          "Room Name        : ", player.player_location.name, "\n",
          "Room Enviornment : ", player.player_location.environment
          )
    print()
    # starting_map.draw_map()
    forest_map.draw_map()
    print()
    print("Where would you like to go?")
r
    path_choices = {1: player.player_location.north,
                    2: player.player_location.south,
                    3: player.player_location.east,
                    4: player.player_location.west
                   }
    print("1: North\n2: South\n3: East\n4: West")

    choice = int(input("? "))

    if path_choices[choice] != False:
        print(path_choices[choice])
        #location = location[f"{path_choices[choice]}"]
        player.change_room(starting_map.rooms[path_choices[choice]])
    else:
        print("can't go that way")

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