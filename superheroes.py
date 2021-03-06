import random

class Hero:
    def __init__(self, name, starting_health=100):
        '''
        Initialize these values as instance variables:
        (Some of these values are passed in above, others will need to be set at a starting value.)
        abilities:List
        name:
        starting_health:
        current_health:
         '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

    def attack(self):
        '''
        Calculates damage from list of abilities.

        This method should call Ability.attack()
        on every ability in self.abilities and
        return the total.
        '''
        total = 0
        for ability in self.abilities:
            total += ability.attack()
        return total

    def is_alive(self):
        '''
        This function will
        return true if the hero is alive
        or false if they are not.
        '''
        if self.current_health > 0:
            return True
        else:
            print('{} died'.format(self.name))
            return False

    def fight(self, opponent):
        '''
        Refactor this method to update the
        number of kills the hero has when
        the opponent dies.
        Runs a loop to attack the opponent until someone dies.
        '''
        battling = True
        while battling:
            hero_attack = self.attack()
            opponent_attack = opponent.attack()

            opponent.take_damage(hero_attack)
            self.take_damage(opponent_attack)

            if self.is_alive() is False:
                opponent.kills += 1
                battling = False
            if opponent.is_alive() is False:
                self.kills += 1
                battling = False

    def add_armor(self, armor):
        '''
        Add armor to armors list.
        This method will also add the armor object that is passed in to this method
        to the list of armor objects defined in the initializer as self.armors.
        '''
        self.armors.append(armor)

    def defend(self):
        '''
        This method should run the block
        method on each piece of armor and
        calculate the total defense.

        If the hero's health is 0
        return 0
        '''
        total = 0
        if self.current_health <= 0:
            return 0
        else:
            #piece stands for piece of armor
            for piece in self.armors:
                total += Armor.block(piece)
            return total

    def take_damage(self, damage_amt):
        '''
        Refactor this method to use the new
        defend method before updating the
        hero's health.

        Update the number of deaths if the
        hero dies in the attack.
        '''
        self.current_health -= damage_amt
        if self.current_health <= 0:
            self.deaths += 1

    def add_kill(self, num_kills):
        '''
        This method should add the number
        of kills to self.kills
        '''
        self.kills += num_kills

    def add_weapon(self, weapon):
        '''
        This method will append the weapon object passed in as an argument to the
        list of abilities that already exists -- self.abilities.

        This means that self.abilities will be a list of abilities and weapons.
        '''
        self.abilities.append(weapon)

class Ability:
    def __init__(self, name, max_damage):
        '''
        Initialize the values passed into this
        method as instance variables.
         '''
        self.name = name
        self.max_damage = int(max_damage)

    def attack(self):
        '''
        Return a random attack value
        between 0 and max_damage.
        '''
        return random.randint(0, self.max_damage)

class Weapon(Ability):
    def attack(self):
        """
        This method should should return a random value
        between one half to the full attack power of the weapon.
        Hint: The attack power is inherited.
        """
        damage = random.randint(self.max_damage//2, self.max_damage)
        return damage

class Team:
    def __init__(self, team_name):
        '''Instantiate resources.'''
        self.name = team_name
        self.heroes = list()

    def add_hero(self, hero):
        '''Add Hero object to heroes list.'''
        self.heroes.append(hero)

    def remove_hero(self, name):
        '''
        Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        found = False
        for index, hero in enumerate(self.heroes):
            if name == hero.name:
                found = True
                self.heroes.pop(index)
        if not found:
            return 0

    def attack(self, other_team):
        '''
        This function should randomly select
        a living hero from each team and have
        them fight until one or both teams
        have no surviving heroes.

        Hint: Use the fight method in the Hero
        class.
        '''

        hero = random.choice(self.heroes)
        if not hero.is_alive():
            hero = random.choice(self.heroes)

        opponent = random.choice(other_team.heroes)
        if not opponent.is_alive():
            opponent = random.choice(other_team.heroes)

        hero.fight(opponent)

    def revive_heroes(self, starting_health=100):
        '''
        This method should reset all heroes
        health to their
        original starting value.
        '''
        for hero in self.name:
            self.current_health = starting_health

    def stats(self):
        '''
        This method should print the ratio of
        kills/deaths for each member of the
        team to the screen.

        This data must be output to the console.
        '''
        for hero in self.heroes:
            print('Kills {} /Deaths {}'.format(hero.name, hero.kills, hero.deaths))

    def view_all_heroes(self):
        '''Print out all heroes to the console.'''
        for hero in self.heroes:
            print(hero.name)

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate name and defense strength.'''
        self.name = name
        self.max_block = max_block


    def block(self):
        '''
        Return a random value between 0 and the
        initialized max_block strength.
        '''
        damage = random.randint(0, self.max_block)
        return damage

class Arena:
    def __init__(self):
        '''
        Declare variables
        '''
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        '''
        This method will allow a user to create an ability.
        Prompt the user for the necessary information to create a new ability object.
        return the new ability object.
        '''
        ability_name = input("You are creating a new Ability,\nName your ability: ")
        max_damage = input("What is the max damage?: ")
        ability = Ability(ability_name, max_damage)
        return ability

    def create_weapon(self):
        '''
        This method will allow a user to create a weapon.
        Prompt the user for the necessary information to create a new weapon object.
        return the new weapon object.
        '''
        weapon_name = input("You are creating a new Weapon,\nName your weapon: ")
        damage = input("What is the max damage?: ")
        weapon = Weapon(weapon_name, damage)
        return weapon

    def create_armor(self):
        '''
        This method will allow a user to create a piece of armor.
        Prompt the user for the necessary information to create a new armor object.
        return the new armor object.
        '''
        armor_name = input("You are creating a new Armor,\nName your armor: ")
        max_block = input("What is the max damage?: ")
        armor = Armor(armor_name, max_block)
        return armor

    def create_hero(self):
        '''
        This method should allow a user to create a hero.
        User should be able to specify if they want armors, weapons, and abilites. Call the methods
         you made above and use the return values to build your hero.
        return the new hero object
        '''
        name = input("You are creating a new Hero,\nName your hero: ")
        new_hero = Hero(name)
        new_hero.add_armor(self.create_armor())
        new_hero.add_weapon(self.create_weapon())
        new_hero.add_ability(self.create_ability())
        return new_hero

    def build_team_one(self):
        '''
        This method should allow a user to create team one.
        Prompt the user for the number of Heroes on team one and
        call self.create_hero() for every hero that the user wants to add to team one.

        Add the created hero to team one.
        '''
        team = input("You are creating a NEW team\nName team one: ")
        self.team_one = Team(team)
        num_heroes = input('How many heroes would you like on team one? ')
        num = 0
        while num < int(num_heroes):
            hero = self.create_hero()
            self.team_one.add_hero(hero)
            num += 1
        return team

    def build_team_two(self):
        '''
        This method should allow a user to create team two.
        Prompt the user for the number of Heroes on team two and
        call self.create_hero() for every hero that the user wants to add to team two.

        Add the created hero to team two.
        '''
        team = input("You are creating a NEW team\nName team two: ")
        self.team_two = Team(team)
        num_heroes = input('How many heroes would you like on team two? ')
        num = 0
        while num < int(num_heroes):
            hero = self.create_hero()
            self.team_two.add_hero(hero)
            num += 1
        return team

    def team_battle(self):
        '''
        This method should battle the teams together.
        Call the attack method that exists in your team objects to do that battle functionality.
        '''
        self.team_one.attack(self.team_two)
        self.team_two.attack(self.team_one)

    def show_stats(self):
        '''
        This method should print out battle statistics
        including each team's average kill/death ratio.

        Required Stats:
        Declare winning team
        Show both teams average kill/death ratio.
        Show surviving heroes.
        '''
        # print("Winning team: {}\nTeam One, kill/death ratio: {}\nTeam Two, kill/death ratio: {}\nSurviving heroes: {}".format())
        print(self.team_one.stats())
        print(self.team_two.stats())

if __name__ == "__main__":
    game_is_running = True

    #Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        replay = input('Play again? y/n: ')

        if replay == 'y':
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
        else:
            game_is_running = False
