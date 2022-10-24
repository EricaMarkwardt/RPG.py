from Hero import hero
from Villain_1 import villain_1
from Villain_2 import villain_2
from Villain_3 import villain_3
import Fun_features #will have to access each part with Fun_features.
import random
print("")
Fun_features.slow_print("\033[38;5;206mInto the fire")
print("")
Fun_features.slow_print("\033[38;5;206mYour quest, should you choose to accept, will be filled with trials and tears; though not all from sadness.")

# (5 points): As a user, I want the ability to select my Hero’s attacks based on my input.  

print(hero["attacks"])


# (5 points): As a user, I want the Enemy’s attack to be chosen at random.



#(5 points): As a user, I want my Hero or Enemy’s health to decrease based on the power of the successful attack. 
 
# (2.5 points): As a user, I want the results of each attack to be printed to the terminal.

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