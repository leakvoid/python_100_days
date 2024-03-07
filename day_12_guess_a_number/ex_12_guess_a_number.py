import random

def select_difficulty():
    """Select difficulty for """
    difficulty = input("Choose a difficulty level, between easy(e) and hard(h): ")
    if difficulty == 'e':
        print("Selected easy difficulty.")
        number_of_attempts = 10
    else:
        print("Selected hard difficulty.")
        number_of_attempts = 5
    return number_of_attempts

def play():
    number_of_attempts = select_difficulty()

    target_number = random.randint(1, 100)

    while number_of_attempts > 0:
        player_guess = int(input("Input a number between 1-100: "))
        if player_guess == target_number:
            print("You won.")
            return
        elif player_guess > target_number:
            print("Target is lower than your guess.")
        else:
            print("Target is higher than your guess.")
        number_of_attempts -= 1
        print("Attempts left: ", number_of_attempts)
    print("You lost.")


while input("Do you want to play another game, y or n? ") == "y":
    play()

