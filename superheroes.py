from random import randint, choice

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
        attack = randint(0, self.max_damage)
        return attack

class Weapon(Ability):
    def attack(self):
        '''This method returns a random value between one half to the full attack power of the weapon'''
        weapon_attack = randint(self.max_damage//2, self.max_damage)
        return weapon_attack

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
        block = randint(0, self.max_block)
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
        self.deaths = 0
        self.kills = 0
    
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

    def defend(self):
        '''Runs `block` method on each armor.
            Returns sum of all blocks
        '''
        total_armor = 0

        for armor in self.armors:
            total_armor = total_armor + armor.block()
        
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
    
    def add_kill(self, num_kills):
        '''Update kills with num_kills'''
        self.kills = self.kills + num_kills
    
    def add_deaths(self, num_deaths):
        '''Update deaths with num_deaths'''
        self.deaths = self.deaths + num_deaths

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.'''
        while self.is_alive() == True and opponent.is_alive() == True:
            if len(self.abilities) > 0 or len(opponent.abilities) > 0:
                self_turn = self.attack()
                opponent.take_damage(self_turn)

                opponent_turn = opponent.attack()
                self.take_damage(opponent_turn)
                
                if opponent.is_alive() == False:
                    self.add_kill(1)
                    opponent.add_deaths(1)
                    print(self.name + ' wins!')
                else:
                    self.add_deaths(1)
                    opponent.add_kill(1)
                    print(opponent.name + " wins!")    
            else:
                print("Draw!")
                return False

class Team:
    def __init__(self, name):
        '''Initialize your team with its team name'''
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        self.heroes.append(hero)

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        for hero in self.heroes:
            if name == hero.name:
                self.heroes.remove(hero)
        return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        for hero in self.heroes:
            print('{}'.format(hero.name))

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        # Hint: Use the fight method in the Hero class.
        
        hero = choice(self.survivors())
        opponent = choice(other_team.survivors())

        hero.fight(opponent)

    def survivors(self):
        living = [hero for hero in self.heroes if hero.is_alive()]
        return living

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            print("Hero: " + hero.name)
            print("Kills: " + str(hero.num_kills))
            print("Death: " + str(hero.num_deaths))

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