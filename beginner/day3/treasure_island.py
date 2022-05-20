from calendar import c


print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# choose_direction = input("Would you like to go LEFT or RIGHT ").lower()
# next_task = input("Would you like to SWIM or WAIT? ").lower()
# choose_door = input("Choose the RED or BLUE or YELLOW door ").lower()

choose_direction = input("Would you like to go LEFT or RIGHT ").lower()
if choose_direction == "left":
    print("You chose to go LEFT.")
elif choose_direction == "right":
    print("You fall into a hole and die.")
next_task = input("Would you like to SWIM or WAIT? ").lower()
if next_task == "wait":
    print("You chose to WAIT.")
elif next_task == "swim":
    print("You were attacked by a shark and died")
choose_door = input("Choose the RED or BLUE or YELLOW door ").lower()
if choose_door == "yellow":
    print("You chose the YELLOW door.")
    print("You found the treasure!")
elif choose_door == "red":
    print("You chose the RED door.")
    print("You just died in a fire")
elif choose_door == "blue":
    print("You chose the BLUE door.")
    print("You were eaten by beasts")
else:
    print("GAME OVER")
