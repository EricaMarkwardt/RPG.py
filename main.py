from Hero import hero
from Villain_1 import villain_1
from Villain_2 import villain_2
from Villain_3 import villain_3
from Fun_features import slow_print 
import random

print("")
slow_print("\033[38;5;206mFollow me Into The Fire")
print("")
slow_print("On our journey, we will find treasure beyond measure, courageous battles, laughter, and tears") 

hero_attack = (hero["attacks"])
# print statement to show user available attack choices
choose_your_hero_attack = input(f"Please choose your hero's attack{hero_attack} ")

enemy_attack = random.choice(villain_1["attacks"])
slow_print(f"Your enemy's attack is {enemy_attack} ")
# here we will reduce the hero's health by damaage of enemy attack
# now subtract hero's damage from enemy's health

# report the news/ use print to show user results
# After Testing a single attack, try using a while loop
# use the hero and villian health values as the conditions
