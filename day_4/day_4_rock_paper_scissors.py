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

# Write your code below this line 👇

choice = int(input("ROCK PAPER SCISSORS!\nWhat do you choose?\n"
                   "Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

game_moves = [rock, paper, scissors]

computer_choice = random.choice(game_moves)

print(
    f"You chose:\n {game_moves[choice]}\nComputer chose:\n{computer_choice}"
)

if choice == 0 and computer_choice == game_moves[1] or choice == 1 and computer_choice == game_moves[2] or choice == 2 and computer_choice == game_moves[0]:
    print("You Lose 😔")
elif choice == 0 and computer_choice == game_moves[2]  or choice == 1 and computer_choice == game_moves[0] or choice == 2 and computer_choice == game_moves[1]:
    print("You Win 🥳")
else:
    print("It's a draw!")
