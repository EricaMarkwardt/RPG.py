
sly_devil = ("\U0001F608")

flying_spaghetti_monster = ("\U0001F47E")

mandarin = ("\U0001F977")

walker = ("\U0001F9DF")

death = ("\U0001F480")

gandalf = ("\U0001F9D9")

morgan_le_fay = ("\U0001F9DA")

arwen = ("\U0001F9DD")

super_strength = ("\U0001F3CB")

swordsman = ("\U0001F93A")

huntsman = ("\U0001F3C7")

speed = ("\U0001F407")

silent_flight = ("\U0001F989")

venom = ("\U0001F40D")

archer = ("\U0001F3F9")

brain_consumption = ("\U0001F9E0")

bad_breath = ("\U0001F32C")


import sys, time
from xml.etree.ElementPath import get_parent_map

def slow_print(string_to_slow_print):
    for letter in string_to_slow_print:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.060)
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