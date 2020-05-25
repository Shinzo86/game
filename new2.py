position = {
    "current" : town_a
    "is_hostile" : current["hostile"]
    "is_level"   : current["level"]
    "north"      : current["n"]
    "south"      : current["s"]
    "east"       : current["e"]
    "west"       : current["w"]
           }

town_a = {
    "hostile" : False
    "level"   : 1
    "n"       : forrest_a
    "s"       : field_b
    "e"       : forrest_b
    "w"       : field_a
         }

town_b = {
    "hostile" : False
    "level"   : 1
    "n"       : False #marsh_a
    "s"       : False #beach_a
    "e"       : False #deep_forrest
    "w"       : forrest_b
         }

town_c = {
    "hostile" : False
    "level"   : 1
    "n"       : False
    "s"       : False #marsh_b
    "e"       : False
    "w"       : False
         }
         
town_d = {
    "hostile" : False
    "level"   : 1
    "n"       : False
    "s"       : False
    "e"       : False #plains
    "w"       : False #kingdom
         }
         
town_e = {
    "hostile" : False
    "level"   : 1
    "n"       : False #lowland_a
    "s"       : False
    "e"       : False #lowland_b
    "w"       : False
         }

town_f = {
    "hostile" : False
    "level"   : 1
    "n"       : False #beach_a
    "s"       : False
    "e"       : False
    "w"       : False #beach_b
         }

forrest_a = {
    "hostile" : True
    "level"   : 5
    "n"       : False #mountain
    "s"       : town_a
    "e"       : False
    "w"       : False
            }
            
forrest_b = {
    "hostile" : True
    "level"   : 10
    "n"       : False
    "s"       : False
    "e"       : town_b
    "w"       : town_a
            }
            
field_a = {
    "hostile" : True
    "level"   : 15
    "n"       : False
    "s"       : False
    "e"       : town_a
    "w"       : False #plains
          }
          
field_b = {
    "hostile" : True
    "level"   : 20
    "n"       : town_a
    "s"       : False #seaside
    "e"       : False
    "w"       : False
          }

roaming = True         
while roaming == True:
    if "current" in position:
        print("which way would you like to go")
        print("1: North ", 
               position["
    