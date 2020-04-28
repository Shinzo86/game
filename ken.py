class Wizard:
    strength = 10
    intellect = 40
    evade = 5

class Warrior:
    strength = 45
    intellect = 4
    evade = 20

class Ranger:
    strength = 20
    intellect = 20
    evade = 50

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

        self.print_class_stats(initial_class)

    def print_class_stats(self, selected_class):
        print(selected_class.strength)
        print(selected_class.intellect)
        print(selected_class.evade)


player = SelectClass()
