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
        attack = randint(0, int(self.max_damage))
        return attack

class Weapon(Ability):
    def attack(self):
        '''This method returns a random value between one half to the full attack power of the weapon'''
        return randint(self.max_damage//2, self.max_damage)

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
        return randint(0, int(self.max_block))

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
    
    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)
    
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

    def defend(self, damage_amount=0):
        '''Runs `block` method on each armor.
            Returns sum of all blocks
        '''
        total_armor = 0

        for armor in self.armors:
            total_armor = total_armor + armor.block()

        result = total_armor - damage_amount
        
        return result

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense. '''

        self.current_health = int(self.current_health) - damage

    def is_alive(self):
        ''' Return True or False depending on whether the hero is alive or not. '''
        if int(self.current_health) <= 0:
            return False
        else:
            return True
    
    def add_kill(self, num_kills):
        '''Update kills with num_kills'''
        self.kills += num_kills
    
    def add_deaths(self, num_deaths):
        '''Update deaths with num_deaths'''
        self.deaths += num_deaths
        
    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.'''

        while self.is_alive() == True and opponent.is_alive() == True:
            if len(self.abilities) == 0 or len(opponent.abilities) == 0:
                return "Draw!"
            else:
                self_turn = self.attack()
                opponent_turn = opponent.attack()

                self.take_damage(opponent_turn)
                opponent.take_damage(self_turn)
                
                if opponent.is_alive() == False:
                    self.winner = self.name
                    self.add_kill(1)
                    opponent.add_deaths(1)
                    break
                else:
                    self.winner = opponent.name
                    self.add_deaths(1)
                    opponent.add_kill(1)
                    break
                
                return self.winner

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
        
        while len(self.survivors()) > 0 or len(other_team.survivors() > 0):
            hero = choice(self.survivors())
            opponent = choice(other_team.survivors())

            return hero.fight(opponent)
            
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
            print("Kills: " + str(hero.kills))
            print("Death: {} \n".format(hero.deaths))

class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        self.team_one = None
        self.team_two = None
        self.winner = None
    
    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''

        new_ability = input('What is your hero\'s ability?: ')
        new_ability_level = input('How strong is this ability?: ')
        
        return Ability(new_ability, new_ability_level)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        
        new_weapon = input('What is your hero\'s weapon?: ')
        new_weapon_level = input('How strong is this weapon?: ')
        
        return Ability(new_weapon, new_weapon_level)
    
    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        new_armor = input('What is your hero\'s armor?: ')
        new_armor_level = input('How much damage does this armor protect from? ')

        return Armor(new_armor, new_armor_level)
    
    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        new_hero = input('Who is your champion?: ')
        self.starting_health = input('Set your Hero\'s hitpoints (Default: 100): ' )
        
        hero = Hero(new_hero, self.starting_health)

        load_em_up = True
        while load_em_up == True:
            equip_choices = input('Please press:\nA to add an Ability\nR to equip Armor\nW to equip a Weapon\nF to Finish creating your champion: ')
            if equip_choices == "A":
                ability = self.create_ability()
                hero.add_ability(ability)
            elif equip_choices == "R":
                armor = self.create_armor()
                hero.add_armor(armor)
            elif equip_choices == "W":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif equip_choices == "F":
                load_em_up = False          
            else:
                print("Please select one of the available options.")
        
        return hero

    def build_team_one(self):
        '''Prompt the user to build teams'''
        name = input('What\'s your team name? ')
        self.team_one = Team(name)

        build_time = True
        while build_time == True:
            hero_count = input('How many heroes are on your team? ')
            if hero_count.isdigit() == False:
                print('Unrecognized input. Please enter an integer.')
            elif hero_count == "0":
                print('You need at least one hero on your team.')
            else:
                count = 0
                while int(hero_count) > count:
                    hero = self.create_hero()
                    self.team_one.add_hero(hero)
                    count += 1
                build_time = False
        
        self.team_one.view_all_heroes()
        return self.team_one
    
    def build_team_two(self):
        '''Prompt the user to build teams'''
        name = input('What\'s your team name? ')
        self.team_two = Team(name)
        
        build_time = True
        while build_time == True:
            hero_count = input('How many heroes are on your team? ')
            if hero_count.isdigit() == False:
                print('Unrecognized input. Please enter an integer.')
            elif hero_count == "0":
                print('You need at least one hero on your team.')
            else:
                count = 0
                while int(hero_count) > count:
                    hero = self.create_hero()
                    self.team_two.add_hero(hero)
                    count += 1
                build_time = False
        
        self.team_two.view_all_heroes()
        return self.team_two
    
    def team_battle(self):
        '''Battle team_one and team_two together.'''
        self.team_one.attack(self.team_two)
        if len(self.team_one.survivors()) > 0 and len(self.team_two.survivors()) == 0:
            self.winner = self.team_one.name
            return self.winner
        else:
            self.winner = self.team_two.name
            return self.winner

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        print(self.team_battle() + " wins!" )

        self.team_one.stats()
        self.team_two.stats()

        if len(self.team_one.survivors()) > 0 and len(self.team_two.survivors) == 0:
            for hero in self.team_one.survivors():
                print("Survivor: " + hero.name)
        elif len(self.team_two.survivors()) > 0 and len(self.team_one.survivors) == 0:
            for hero in self.team_two.survivors():
                print("Survivor: " + hero.name)
        else:
            print("No survivors")

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()