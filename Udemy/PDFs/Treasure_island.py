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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

Choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"').lower()

if Choice1 == "left":
    input(print("You found in front of yourself a bear. You want to fight it or run? Type \"fight\" or \"run\""))
    second_choice = input().lower()
    if second_choice == "fight":
        print("You fought the bear and it killed you.")
        print("Game Over.")
    else:
        input(print("You successfully ran away from the bear. You found three colored doors. Which one do you want to open? Type \"Yellow\", \"green\", \"blue\ or \"none\"."))
        third_choice = input().lower()
        if third_choice == "yellow":
            print("You found a lost book. You open it just to find that the treasure was false. Game Over.")
        elif third_choice == "green":
            print("You found a family of huge bears and they kill you. Game over!")
        elif third_choice == "blue":
            print("You found a magic potion. You drink it and feel like a king!")
            print("Oh no, you realize that the potion you drank was not a poition. It was liquid cocaine! You died from overdose. Game Over!")
        else:
            print("You found a hidden room. You go inside and see a giant bear. You decide to run away.")
            print("Oh no, you realize that the bear is a giant bear. You died from overzealousness. Game Over!")        
else:
    print("Oh no, you fell into a Hole. Game Over.")