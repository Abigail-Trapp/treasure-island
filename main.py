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
print("You finally hit dry land and come across a fork leading to two paths.")
left_or_right = input("Do you go left or right?\n").lower()
if left_or_right == "left":
    print("The path leads you to a huge body of water You're not sure if you should swim or wait for a boat.")
    swim_or_wait = input("Do you swim or wait?\n").lower()
    if swim_or_wait == "wait":
        print(
            "As you wait, Neptune appears before you. With a wave of his staff, you see three doors appear before you: red, yellow, and blue."
        )
        print(
            "Neptune speaks to you saying, 'Choose wisely, for one of these doors leads to the treasure, others to your doom'."
        )
        red_yellow_blue = input("Which door do you chose to enter?\n").lower()
        if red_yellow_blue == "red":
            print(
                "You have opened the door into darkness with a pair of red eyes staring back at you.\nYou are doomed to live the rest of your life in madness never allowed to leave the island again."
            )
            print("Game Over")
        elif red_yellow_blue == "blue":
            print(
                "You see an army of skeletons charging rapidly at you.\nYou try to outrun them but were not fast enough."
            )
            print("Game Over")
        elif red_yellow_blue == "yellow":
            print(
                "You open the door and see a trail leading down the path to the treasure."
            )
            print("Congratulations, you found the treasure!")
            print("Game Won")
        else:
            print("Adventure Over")
    else:
        print("A krakken appeared, and swallowed you whole.")
        print("Game Over")
else:
    print("You fell down a deep hole and are now trapped forever.")
    print("Game Over")