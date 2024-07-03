rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

game_list=[rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice_index = random.randint(0,2)
computer_choice = game_list[computer_choice_index]
your_choice = game_list

print(your_choice)
print("Computer chose:" + computer_choice)

if computer_choice_index == choice:
    print("It's a Draw.")
elif choice > 2:
    print("Invalid input")
elif computer_choice_index == 0 and choice == 2:
    print("Computer Wins.")
elif computer_choice_index == 1 and choice == 0:
    print("Computer Wins.")
elif computer_choice_index == 2 and choice == 1:
    print("Computer Wins.")
elif computer_choice_index == 0 and choice == 1:
    print("You Win!")
elif computer_choice_index == 1 and choice == 2:
    print("You Win!")
else:
    print("You win!")
    