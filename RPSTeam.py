import random 

#the game title
print(' ')
print('===================')
print('ROCK PAPER SCISSORS')
print('===================')
print(' ')

#display game choices
print('1) ROCK ✊')
print('2) PAPER 🤚')
print('3) SCISSORS')

# Assigned variables
Rock = 1
Paper = 2
Scissors = 3

def get_choice_name(choice):
    if choice == Rock:
        return 'Rock'
    elif choice == Paper:
        return 'Paper'
    elif choice == Scissors:
        return 'Scissors'

def play_game(opponent):
  # Set player 1's choice
    player1 = int(input('Player One pick a number (1-3): '))

    if opponent == 'friend':
        player2 = int(input('Player Two pick a number (1-3): '))
    elif opponent == 'cpu':
        player2 = random.randint(1, 3)
        print(f'CPU Choose: {get_choice_name(player2)}')

    # Prints the input
    print('Player One Choose: ' + get_choice_name(player1))
    if opponent == 'friend':
        print('Player Two Choose: ' + get_choice_name(player2))

    # If statement for playing the game
    if player1 != player2:
        if (player1 == Rock and player2 == Scissors) or \
            (player1 == Paper and player2 == Rock) or \
            (player1 == Scissors and player2 == Paper):
            print('Player One Wins!🎉')
        else:
            if opponent == 'friend':
                print('Player Two Wins!🎉')
            else:
                print('Sadly the CPU won!🤖')
    else:
        print("It's a tie!🤝")

# Ask if the user wants to play against a friend or CPU
while True:
    print()
    opponent = input("Do you want to play against a friend or the CPU? (Enter 'friend' or 'cpu'): ").lower()
    
    if opponent in ['friend', 'cpu']:
        play_game(opponent)  # Pass the opponent type to the play_game function
        break
    else:
       print("Oops, let's try that again. Please enter 'friend' or 'cpu'.")
