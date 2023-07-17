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


print("===============================================================================")
print("\t\t     -----Welcome to Treasure Island.-----")
print("\t\t     Your mission is to find the treasure.") 
print("===============================================================================")
print("follow the instructions, then make the right decision to reach the treasure")
name = input("before starting the game, enter your name: ")
print("Good luck " + name + "!!" )
print("-------------------------------------------------------------------------------")

print('''After landing on the treasure island, you decide to go follow the treasure 
map then you have arrived at a dungeon. 

at the entrance of the dungeon there is a monster standing guard there, you
have a sword, slingshot and rope in your inventory. 
''')
decision1 = input("What will you do? give the choice (fight or run):\n").lower()
if decision1 == "fight":
    print("-------------------------------------------------------------------------------")
    print("You've decided to fight with the monster, \nchoose the item you will use (Sword, Slingshot or Rope)")
    decision2 = input("Choose item: \n").lower()
    if decision2 == "sword":
        print("-------------------------------------------------------------------------------")
        print("You've decided to fight bravely against the monster with your sword, \nbut your sword broke while fighting against the monster")
        print("\nWhen you look around and try to find a way to defeat the monster \nyou find that above the monster standing there is a beehive, you're trying to\nuse the beehive to fight monsters\n")    
        decision3 = input("choose an item to use (slingshot or rope):\n").lower()
        if decision3 == "slingshot":
            print("-------------------------------------------------------------------------------")
            print("You shoot a beehive using a slingshot, the beehive falls right on the monster! \nthen the bees get angry and start attacking the monster")
            print("the monster ran away because it was attacked by the bees \nYou did it!! now you can enter the dungeon to find treasure")
            print("-------------------------------------------------------------------------------")
            print("After continuing to walk through the dungeon through many obstacles finally, \nyou reach the room where the treasure is stored, but the door to enter the \nroom is closed with a numeric key, and to open the lock there is a hint as \nfollows:\n")
            print("|--------A NUMERIC LOCK HAS A 3 DIGIT KEY-------|")
            print("| 482 : One number is correct and well placed   |")
            print("| 416 : One number is correct but wrong placed  |")
            print("| 204 : Two number are correct but wrong placed |")
            print("| 738 : Nothing is correct                      |")
            print("| 780 : One number is correct but wrong placed  |")
            print("|-----------------------------------------------|")
            decision4 = input("\nInput 3 digit number:\n")
            if decision4 == "042":
                print("-------------------------------------------------------------------------------")
                print("Your answer is correct, the lock is open!!")
                print("You have successfully opened the door and entered the room \nand finally you get the treasure!!")
                print("-------------------------------------------------------------------------------")
                print("-------------------------------------------------------------------------------\n")
                print("\t----------Congratulations you have won this game!!----------")
                print("-------------------------------------------------------------------------------")
            else:
                print("-------------------------------------------------------------------------------")
                print("INCORRECT!!")
                print("Trap activated!!")
                print("Suddenly the floor beneath you stands open and you fall into the lake of fire")
                print("-------------------------------------------------------------------------------")
                print("-------------------------------------------------------------------------------\n")
                print("\t\t---------------GAME OVER!!---------------")
                print("-------------------------------------------------------------------------------")
        else:
            print("-------------------------------------------------------------------------------")
            print("You've decided to use the rope and throw the beehive, but damn it!!")
            print("The rope does not reach the beehive, then the monster attacks \nand you are eaten by the monster")
            print("-------------------------------------------------------------------------------")
            print("-------------------------------------------------------------------------------\n")
            print("\t\t---------------GAME OVER!!---------------")
            print("-------------------------------------------------------------------------------")
    elif decision2 == "slingshot":
        print("-------------------------------------------------------------------------------")
        print("You shoot at the monster with a slingshot, but your attack \ndoesn't deal any damage to the monster")
        print("Damn it!!, the monster quickly attacks and eats you!")
        print("-------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------\n")
        print("\t\t---------------GAME OVER!!---------------")
        print("-------------------------------------------------------------------------------")
    else:
        print("-------------------------------------------------------------------------------")
        print("You try to bind the monster using a rope, but you've failed!! \nand the monster quickly attacks and eats you!")
        print("-------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------\n")
        print("\t\t---------------GAME OVER!!---------------")
        print("-------------------------------------------------------------------------------")
else:
    print("-------------------------------------------------------------------------------")
    print("You've decide to run, and you fall into a pit trap near the entrance of the \ndungeon and get caught by the monster")
    print("-------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------\n")
    print("\t\t---------------GAME OVER!!---------------")
    print("-------------------------------------------------------------------------------")
