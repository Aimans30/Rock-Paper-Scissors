import random

def get_user_choice():
    while True:
        user_choice = input("Choose 'rock', 'paper', or 'scissors' (or 'quit' to exit): ").lower()
        if user_choice in ['rock', 'paper', 'scissors', 'quit']:
            return user_choice
        else:
            print("Invalid choice. Please choose again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == 'quit':
        return "Thanks for playing! Goodbye."

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        if user_choice == 'quit':
            print(determine_winner(user_choice, ''))
            break

        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}.")
        print(f"Computer chose {computer_choice}.")
        result = determine_winner(user_choice, computer_choice)
        print(result)

        if 'win' in result:
            if result.startswith('You'):
                user_score += 1
            else:
                computer_score += 1

        print(f"Score: You - {user_score}, Computer - {computer_score}")
        
        if user_score == 3:
            print("You won the game!")
            break
        elif computer_score == 3:
            print("Computer won the game!")
            break

if __name__ == "__main__":
    play_game()
