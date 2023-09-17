print("""
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-\"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
_________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************

Welcome to Treasure Island.
Your mission is to find the treasure!
""")

choice_1 = input("You're at a crossroad, where do you want to go? Type 'left' "
                 "or 'right'.\n").lower()

choice_2 = input("After walking for an hour you reach a dock on a lake."
                 "\nA sign tells you the next ferry will be in an hour."
                 "\nDo you swim across the lake or wait for the boat? Type "
                 "'swim' or 'wait'\n").lower()

choice_3 = input("The ferry arrives not long after you arrive and you travel"
                 "safely across the lake to the small island at it's center."
                 "\nThere are four beaches on the small island, North, South,"
                 "East and West."
                 "\nWhich beach will you dig for treasure on? Type 'N', 'S',"
                 "'E' or 'W'\n").lower()


if choice_1 == "right":
    print("Arrgh! You've fallen into a booby trap!\nGAME OVER")
if choice_2 == "swim":
    print("dum dum, dum dum..."
          "\nSeems like this lake contained flesh-eating piranhas!\nGAME OVER")
if choice_3 == "n":
    print("Crabs! As far as the eye can see... and they're gaining on you "
          "quickly...\nMight be time to abandon the treasure hunt and RUN!"
          "\nGAME OVER")
elif choice_3 == "e":
    print("You're shovel hits something hard under the sand... "
          "You brush the sand away to find an empty treasure chest."
          "Someone must have beaten you to the treasure.\nGAME OVER")
elif choice_3 == "w":
    print("Quick Sand! It's sucking you under... it's getting darker..."
          "\nGAME OVER")
else:
    print("Ahoy me heartie! You've found the buried treasure!")
