import random

class Ability:
    def __init__(self, name, max_damage):
        '''Create Instance Variables:
           name: String
           max_damage: Integer
        '''
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        attack = random.randint(0, self.max_damage)
        return attack

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate Instance Properties:
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block
    
    def block(self):
        ''' Return a random value between 0 and the initialized max_block strength. '''
        block = random.randint(0, self.max_block)
        return block

class Hero:
    def __init__(self, name, starting_health = 100):
        '''Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        self.name = name
        self.abilities = []
        self.armors = []
        self.starting_health = starting_health
        self.current_health = starting_health
    
    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)
    
    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: Armor Object
        '''
        self.armors.append(armor)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
            return: total:Int
        '''
        total_attack = 0

        for ability in self.abilities:
            attack = ability.attack()
            total_attack = total_attack + attack
        
        return total_attack


    def defend(self, incoming_damage):
        '''Runs `block` method on each armor.
            Returns sum of all blocks
        '''
        total_armor = 0

        for armor in self.armors:
            block = armor.block()
            total_armor = total_armor + block
        
        return total_armor

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense. '''
        self.current_health = self.current_health - damage

        return self.current_health

    def is_alive(self):
        ''' Return True or False depending on whether the hero is alive or not. '''
        if self.current_health < 1:
            return False
        else:
            return True

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.'''
        while self.is_alive() == True and opponent.is_alive() == True:
            if len(self.abilities) > 0 or len(opponent.abilities) > 0:
                self_turn = self.attack()
                opponent.take_damage(self_turn)

                opponent_turn = opponent.attack()
                self.take_damage(opponent_turn)
                
                if opponent.is_alive() == False:
                    print(self.name + ' wins!')
                else: #self.is_alive() == False:
                    print(opponent.name + " wins!")    
            else:
                print("Draw!")
                return False

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 20)
    ability3 = Ability("Wizard Wand", 300)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)