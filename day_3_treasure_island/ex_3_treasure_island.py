print('''
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
''')
print("Welcome to the treasure island")
print("Your mission is to find the treasure")

choice_1 = input("You're at the cross road. Chose where you want to go: left or right: ")
if choice_1 == "left":
    choice_2 = input("You've come to a lake. There is an island in the middle. Type \"wait\" to wait for boat, type \"swim\" to swim across: ")
    if choice_2 == "wait":
        choice_3 = input("You arrived at the island unharmed. There is a house with 3 doors. One is red, second is green, third is blue. Select colour: ")
        if choice_3 == "red":
            print("There was bunch of cats inside of the house. When you went outside you discovered other two doors dissapeared. You opted to return back home. Game over.")
        elif choice_3 == "green":
            print("You found a pretty girl and decided to marry her. But before that you become a game developer. You won.")
        else:
            print("You found a treasure and got rich. Game over.")
    else:
        print("You swimmed a third of the path, got tired and decided to return back home. Game over.")
else:
    print("You got lost and decided to return home. Game over.")