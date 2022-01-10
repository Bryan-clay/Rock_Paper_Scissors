#rock paper scissors

#score counter
user_score = 0
computer_score = 0
playAgain = 'yes'
#user input
while playAgain.lower() == 'yes':
    prompt = "Select 'rock', 'paper', or 'scissors' "
    user = input(prompt)
    #create win and loss message
    win = '\nCONGRATULATIONS, YOU WIN!'
    lose = '\nCOMPUTER WINS!'

    print(f"You selected '{user.upper()}'")
    if user == 'rock':
        user = 0
    elif user == 'paper':
        user = 1
    elif user == 'scissors':
        user = 2
    else:
        print('Invalid input, please try again.')
    #create a number generator 1-3 and assign it rock paper or scissors
    import random
    computer = random.randint(0,2)

    if computer == 0:
        print("Computer selected 'ROCK'")
    elif computer == 1:
        print("Computer selected 'PAPER'")
    else:
        print("Computer selected 'SCISSORS'")

#compare user and computer

    if user == computer:
        print('TIE!')
        print("\nTRY AGAIN")

    elif user == 0 and computer == 1:
        print(lose)
        computer_score += 1
        print(f'\tComputer: {computer_score}')
        print(f'\tUser: {user_score}')

    elif user == 1 and computer == 2:
        print(lose)
        computer_score += 1
        print(f'\tComputer: {computer_score}')
        print(f'\tUser: {user_score}')

    elif user == 2 and computer == 0:
        print(lose)
        computer_score += 1
        print(f'\tComputer: {computer_score}')
        print(f'\tUser: {user_score}')

    elif user == 0 and computer == 2:
        print(win)
        user_score += 1
        print(f'\tComputer: {computer_score}')
        print(f'\tUser: {user_score}')

    elif user == 1 and computer == 0:
        print(win)
        user_score += 1
        print(f'\tComputer: {computer_score}')
        print(f'\tUser: {user_score}')

    elif user == 2 and computer == 1:
        print(win)
        user_score += 1
        print(f'\tComputer: {computer_score}')
        print(f'\tUser: {user_score}')

    playAgain = input("\nWould you like to play again? yes / no ")
