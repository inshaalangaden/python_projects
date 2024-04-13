print('''  _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
                                                                 ''')

print("Welcome to Treasure Island. Your mission is to find the treasure.")
task_1= input("Which direction you want to go? Type Left or Right.")
if task_1 == "Left" :
    task_2= input("There is a river infront of you. Do you want to swim across the river or wait for the boat? type Swim or Wait.")
    if task_2 == "wait":
        task_3 =input("There are 3 doors infront of you. Which will you select? type yellow , blue or red")
        if task_3== "blue":
            print("You won the game! Fantastic!!")
        elif task_3 == "yellow":
            print("Oh uh! You caught up in fire. Game Over!!")
        else:
           print("Oh uh! You ended up in a blackhole. Game Over!!") 
    else:
        print("Oh uh! A hungry crocodile ate you. Game Over!!")
else:  
    print("Oh uh! There is a pit in that direction. Game Over!!")   