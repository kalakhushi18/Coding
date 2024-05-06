import random
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors "))
choices = ['Rock', 'Paper', 'Scissors']

print(f"You chose {choices[player_choice]}")

computer_choice = random.randint(0,2)
print(f'Computer chooses {choices[computer_choice]}')

if player_choice == computer_choice:
    print("It's a draw")
elif player_choice == 0:
    if computer_choice == 1:
        print("You lose")
    else:
        print("you win")
elif player_choice == 1: 
    if computer_choice == 0 :
        print("you win")
    else:
        print("You lose")
elif player_choice == 2:
    if computer_choice == 0:
        print('You lose')
    else:
        print("You win")
