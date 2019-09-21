class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        pass

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    
    def block(self):
        pass

class Hero:
    def __init__(self, name, starting_health):
        self.name = name
        self.starting_health = 100
    
    def add_ability(self, ability):
        pass

    def attack(self):
        pass

    def defend(self, incoming_damage):
        pass

    def take_damage(self, damage):
        pass

    def is_alive(self):
        pass

    def fight(self, opponent):
        pass
