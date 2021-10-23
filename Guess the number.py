import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_difficulty():
    difficulty = input("Choose a difficulty. Please type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_LEVEL_ATTEMPTS
    elif difficulty == "hard":
        return HARD_LEVEL_ATTEMPTS
    else:
        print("Wrong! Please type 'easy' or 'hard'.")
        return set_difficulty()

def check_number(answer, guess_number, attempts):
    if answer > guess_number:
        print("Too low.")
        return attempts - 1
    elif answer < guess_number:
        print("Too high.")
        return attempts - 1
    else:
        print(f"You got it! The answer is {answer}.")

def game():
    print("Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 100.")

    numbers = list(range(1, 101))
    answer = random.choice(numbers)

    attempts = set_difficulty()
    
    guess_number = 0
    while guess_number != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        
        guess_number = int(input("Make a guess: "))
           
        attempts = check_number(answer, guess_number, attempts)
        if attempts == 0:
            print("You've run out of guesses. YOU LOSE!!!")
            return
        elif guess_number != answer:
            print("Guess again.")

game()

