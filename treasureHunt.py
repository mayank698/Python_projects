print(''' _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 ''')

directions = input("Where you want to go LEFT or RIGHT: ").lower()
transport = input("You want to walk or fly: ").lower()
door = input("Which door you want to select RED,YELLOW or GREEN: ").lower()

if (directions == "left") and (transport == "fly") and (door == "green"):
    print("You won!")
if (directions == "right") and (transport == "fly") and (door == "yellow"):
    print("You won!")
else:
    print("You lose! Better luck next time")


# https://ascii.co.uk/art
