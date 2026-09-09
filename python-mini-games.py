import random

WIN_SCORE = 5
MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 10

#User plays rock paper scissors
def rps():
    play = True

    options = ['rock', 'paper', 'scissors']

    while play:
        user_win = 0
        computer_win = 0
        game_round = 1
        print(f'\nStarting Round. First to {WIN_SCORE} wins!')

        while True:
            user_input = input(f'Round: {game_round}\nType Rock/Paper/Scissors or type S to stop: ').lower()
            if user_win == WIN_SCORE:
                print('Congrats! You won the game!')
                break

            if computer_win == WIN_SCORE:
                print('You lose!\n')
                break

            if user_input == 's':
                print('Stopping game')
                break

            if user_input not in options:
                print('Invalid input.\n')
                continue
    
            comp_pick = random.choice(options)
            print(f'Computer has picked: {comp_pick}.\n')

            if (
                (user_input == 'rock' and comp_pick == 'scissors') or
                (user_input == 'paper' and comp_pick == 'rock') or
                (user_input == 'scissors' and comp_pick == 'paper')
            ):
                print('You won this round!\n')
                user_win += 1
                game_round += 1

            elif user_input == comp_pick:
                print('Its a Tie! Try again.\n')

            else:
                print('You lost this round.\n')
                computer_win += 1
                game_round += 1
            
        user_rounds = 'round' if user_win == 1 else 'rounds'
        comp_rounds = 'round' if computer_win == 1 else 'rounds'
        print(f'\nYou won {user_win} {user_rounds}.')
        print(f'The computer won {computer_win} {comp_rounds}.')

        while True:
            play_again = input('\nPlay this game again?(y/n): ').lower()
            if play_again == 'n':
                print('Thanks for playing Rock Paper Scissors!')
                play = False
                break
            elif play_again == 'y':
                print('Playing again!')
                break
            else:
                print('Invalid input. Please type y or n')
                
#User plays guess the number
def guess_num():
    playing = True

    while playing:
        print(f'\nGuess the correct number between {MIN_NUMBER}-{MAX_NUMBER} to win.\n')
        print(f'You get {MAX_ATTEMPTS} attempts to guess the number.\n')
        
        answer = random.randint(MIN_NUMBER, MAX_NUMBER)
        
        counter = 0
        round = 1
        guessed_nums = set()

        while counter < MAX_ATTEMPTS:
            print(f'Round {round}.')
            round += 1
            player_input = input("Enter a number or type 'S' to stop: ")

            if player_input.lower() == "s":
                print('Stopping game.')
                break
            try:
                num = int(player_input)
            except ValueError:
                print("Please enter an integer or 'S' to stop.\n")
                continue
            
            if num < MIN_NUMBER or num > MAX_NUMBER:
                print(f'Out of range. Please enter a number between {MIN_NUMBER}-{MAX_NUMBER}.\n')
                continue

            if num in guessed_nums:
                print('You guessed that number already. Enter a new number.\n')
                continue

            guessed_nums.add(num)
            counter += 1

            if num == answer:
                if counter == 1:
                    print('You won on your first try! Congratulations.')
                    break
                else: 
                    print(f'You win! The number was {answer}. It took you {counter} tries.')
                    break

            elif num > answer:
                print('Your number is too high. Enter a lower number.\n')

            else:
                print('Your number is too low. Enter a higher number.\n')

        if counter >= MAX_ATTEMPTS and num != answer:
                print(f'You lose. The number was {answer}.')

        while True:
                play_again = input('\nPlay this game again?(y/n): ').lower()
                if play_again == 'n':
                    print('Thanks for playing Guess the Number!')
                    playing = False
                    break
                elif play_again == 'y':
                    print('Playing again!')
                    break
                else:
                    print('Invalid input. Please type y or n')

#Displays game menu    
def main_menu():
    while True:
        print("\n---- Game Menu ----")
        print("1. Rock-Paper-Scissors")
        print("2. Guess the Number")
        print("3. Quit")
        choice = input("Select a game (1-3): ")

        if choice == '1':
            rps()
        elif choice == '2':
            guess_num()
        elif choice == '3':
            print("Thank you for playing!")
            break
        else:
            print("Invalid selection. Choose 1, 2, or 3.")

# Run the menu
main_menu()
        

        
    
        
