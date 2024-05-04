import random

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

game_images = [rock, paper, scissors]

user_choice = int(input("Enter 0 for rock, 1 for paper and 2 for scissors: "))
print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice > 2 or user_choice < 0:
    print("Wrong number. You lose.")
elif (user_choice == 0 and computer_choice == 2) or \
    (user_choice == 1 and computer_choice == 0) or \
    (user_choice == 2 and computer_choice == 1):
    print("You win.")
elif user_choice == computer_choice:
    print("Draw.")
else:
    print("You lose.")

    