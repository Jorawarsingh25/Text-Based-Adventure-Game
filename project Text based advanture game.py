                              ##TEXT BASED GAME##                      
import random

class Player: #create  1st class Player
    def __init__(self,name):
        self.name=name
        self.hp=100
        self.skills=[]
        self.inventory=[]

    def display_status(self): #create display status function
        print(f'the name is {self.name} and HP: {self.hp}')
        print('Skill:',','.join(self.skills))
        print('Inventory:',self.inventory)
        print('**************')
        
    def take_damage(self,damage): #create damage function
        self.hp -=damage
        if self.hp <=0: 
            print(f'{self.name} has been loser..')
            return False
        else:
            print(f'{self.name} receive {damage} damage')
            self.display_status()
            return True
        
    def add_skill(self,skill): #add skill
        self.skills.append(skill)
        print(f'{self.name} lean {skill}')

    def add_inventory(self,item): #add inventory
        self.inventory.append(item)
        print(f'{item} add to inventory')
    
    def use_item(self,item): #use item in inventory
        if item in self.inventory:
            print(f'{self.name} use the {item}')
            self.inventory.remove(item)
        else:
            print(f"you don't have {item} in your inventory")

class Game: #create 2nd class Game
    def __init__(self): 
        self.player=None
        self.create_player()
        self.run_game()

    def create_player(self): #create function create_player
        print('*****Welcome to the Text-Based Advanture Game..!!*****')
        name=input('Enter your name: ')
        self.player=Player(name)
        print(f'Welcome, {self.player.name}')
        self.player.add_skill('Archery')#archery mean tirangdazi!

    def run_game(self): # create function run_game
        print('you find yourself in a mysterious land...')
        while self.player.hp>0:
            print('\n what do you want to do ?')
            print('1. Explore')
            print('2. Check Inventory')
            print('3. Quit')
            choice=input('Enter your choice: ')

            if choice=='1':
                self.explore()
            elif choice=='2':
                self.player.display_status()
            elif choice=='3':
                print('Exit the game...')
                break
            else:
                print('Invalid input! Please try again...')
    def explore(self): #create exploring function
        print('you choose the exploring..')
        outcome=random.randint(1,3)
        
        if outcome==1:
            self.treasure()
        elif outcome==2:
            self.monster()
        else:
            print('are you not interseted..')

    def treasure(self): #create function in treasure
        print('you choose the treasure ')
        loot=random.choice(['Gold','Health Potion','Magic item'])
        self.player.add_inventory(loot)
        print(f'if you received {loot}')

    def monster(self): #create function in monster
        while True:
            print('\nwhat do you want to do ?')
            print('1. Fight')
            print('2. Use item')
            print('3. Go to home ')
            choice=input('Enter the choice: ')
            
            if choice=='1':
                self.fight_monster()
                break
            elif choice=='2':
                self.use_item()
            elif choice=='3':
                print('go to your home now')
                break
            else:
                print('Invalid input!Please correct choice!!')
    def fight_monster(self): #create a function  fight_monster
        monster_hp=random.randint(50,100)
        while monster_hp>0:
            player_damage=random.randint(10,20)
            monster_hp -=player_damage
            print(f'you attack the monster and {player_damage} damage')
           
            if monster_hp<=0:
                print('you defeated the monster')
                break
            monster_damage=random.randint(10,25)
            if not self.player.take_damage(monster_damage):
                print('Game Over!!')
                exit()
    def use_item(self): #create function in user_item
        print("Inventory: ")
        print(self.player.inventory)
        item=input('Enter item to use: ')
        self.player.use_item(item)

if __name__=='__main__':
    Game()        


































