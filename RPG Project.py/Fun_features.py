# print("Villains")
# print("")
sly_devil = ("\U0001F608")
# print(sly_devil, "Sly Devil")
flying_spaghetti_monster = ("\U0001F47E")
# print(flying_spaghetti_monster, "Flying Spaghetti Monster")
mandarin = ("\U0001F977")
# print(mandarin, "", "Mandarin")
walker = ("\U0001F9DF")
# print(walker, "Walker")
death = ("\U0001F480")
# print(death, "death")
# print("")
# print("Heroes")
# print("")
gandalf = ("\U0001F9D9")
# print(gandalf, "Gandalf")
morgan_le_fay = ("\U0001F9DA")
# print(morgan_le_fay, "Morgan le Fay")
arwen = ("\U0001F9DD")
# print(arwen, "Arwen")
# print("")
# print("Powers")
# print("")
super_strength = ("\U0001F3CB")
# print(super_strength, "", "Super Strength")
sword_skills = ("\U0001F93A")
# print(sword_skills, "Sword Skills")
equestrian = ("\U0001F3C7")
# print(equestrian, "Equestian")
strength_in_numbers = ("\U0001F407")
# print(strength_in_numbers, "Strength in Numbers")
stealthy_flight = ("\U0001F989")
# print(stealthy_flight, "Stealthy Flight")
venom = ("\U0001F40D")
# print(venom, "Venom")
archery = ("\U0001F3F9")
# print(archery)
brains = ("\U0001F9E0")
# print(brains)
bad_breath = ("\U0001F32C")
# print(bad_breath)

import sys, time
from xml.etree.ElementPath import get_parent_map

def slow_print(string_to_slow_print):
    for letter in string_to_slow_print:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.075)
    print('')
    
# slow_print("\033[38;5;206mHello world")

# ANSI escape codes

# \033[1;32;40m = Bold Green
# \0033[1;31;40m = Bold Red
# \033[1;33;40m = Bold Yellow
# \033[38;5;206m = Bold Pink



# \003[ = Escape Code
# 1 = Text Style (1 is Bold)
# 32, = Text Color (32 is Green)
# 40, = Background (40 is Black)