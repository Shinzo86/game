class Wizard:
    health = 10

class MyClass:
    def __init__(self, chosen_class):
        self.health = chosen_class.health


player_a = MyClass(Wizard)

print(player_a.health)

Wizard.health = 20

print(player_a.health)


