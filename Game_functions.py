from Hero import hero
from Villain_1 import villain_1
from Villain_2 import villain_2
from Villain_3 import villain_3
from Fun_features import slow_print 
import random

def display_welcome():
    print("")
    slow_print("\033[38;5;206mFollow me Into The Fire")
    print("")
    slow_print("On our journey, we will find treasure beyond measure, courageous battles, laughter, and tears") 

def choose_your_attack():

    choose_your_hero_attack = input(f"How should {hero['name']} attack her enemy? {hero_attack} ")
    slow_print(f"You have chosen {choose_your_hero_attack}")

def battle(hero,enemy):
    slow_print(f"Your hero is {hero['name']}.")
    while hero["health"] > 0 and enemy["health"] > 0:
        hero_attack = (hero["attacks"][0]) # I would make a funciton that allows user to pick attack and then returns the selected value
        enemy_attack = random.choice(enemy["attacks"])
        slow_print(f"Your enemy's attack is {enemy_attack[0]} and does {enemy_attack[1]} damage.")
        enemy['health'] -= hero_attack[1]
        print(f'{enemy["name"]} was attacked by {hero["name"]} for {hero_attack[1]} damage leaving them with {enemy["health"]} health remaining')
        hero['health'] -= enemy_attack[1]
        print(f'hero attacked by enemy, fix statement next ')
    # here outside of our while loop we can assume there will only be 1 person left standing     
def run_game():
    # Game_functions.display_welcome() #TESTED
    battle(hero,villain_1) 
    battle(hero,villain_2) 
# print("")
# print






# here we will reduce the hero's health by damaage of enemy attack
# now subtract hero's damage from enemy's health

# report the news/ use print to show user results
# After Testing a single attack, try using a while loop
# use the hero and villian health values as the conditions

# (5 points): As a user, I want my Hero or Enemy’s health to decrease based on the power of the successful attack. 

# winner_health = 
 
# (2.5 points): As a user, I want the results of each attack to be printed to the terminal.

# print (winner_health)

# (10 points): As a user, I want to be able to “loot” defeated enemies, which will include: 
# Adding the Enemy’s equipment to the hero character’s equipment Set 
# Adding the Enemy’s gold, silver, or copper coins to the appropriate value in the Hero’s coins Dictionary 

# (5 points): As a data analyst, I want the game to conclude when the Hero’s health reaches 0, or when all three Enemies have been defeated. 

# while the_hero health = 0
#     if the_hero health <= 0:
#         print("And that's the end.")
#     else:
#         print("There's life in you, still! Try again!")
#         the_hero health -= villain 

# (2.5 points): As a data analyst, I want my run_game() function to call my other functions in a logical order that will determine game flow. 

# (5 points): As a data analyst, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing! 

# (5 points): As a user, I want the Hero and Enemy to continue attacking each other until one's health reaches zero.  



# (7.5 points): As a user, I want to increase my Hero’s level after defeating an Enemy, which will include: 
# Incrementing my Hero’s level by 1 
# Adding a new attack of my choosing to my Hero's Attack Tuple. 

# (5 points): As a user, I want a challenges phrase to be randomly selected and printed when my Hero attacks, and a plea phrase to be randomly selected and printed when my Hero is attacked. 