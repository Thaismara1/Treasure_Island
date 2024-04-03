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


choice1= input('You are at a cross road. Where do you want to go? Type "left" or "right"\n')

choice1_lower = choice1.lower()

if (choice1_lower == "left"):
  choice2 = input('you come to a lake, there is an island in the middle of the lake. Type "wait" to wait the boat. Type "swim" to swim across.\n')
  choice2_lower = choice2.lower()
  
  if (choice2_lower == "wait"):
    choice3 = input('you arrived at the island unhamed. there is a house with 3 doors. One red, one yellow and blue. which colour do you chose?\n')
    choice3_lower = choice3.lower()

    if (choice3_lower == "blue"):
      print("You enter a room of beasts. Game Over")
    elif (choice3_lower == "red"):
      print("You entered a room on fire. Game Over")
    elif (choice3_lower == "yellow"):
      print("Very well, you found the treassure! you won the game!")
    else:
      print("Game Over!")
  else:
    print("Attacked by trout. Game Over")
else:
  print("Fall into a hole. Game Over.")


