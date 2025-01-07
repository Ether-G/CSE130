# 1. Name:
#      -Ben B-
# 2. Assignment Name:
#      Lab 01: Guessing Game
# 3. Assignment Description:
#      This program allows the user to guess a random number between 1 and a user-specified upper limit.
#      It provides feedback on whether guesses are too high or too low and displays the total guesses and the guessed numbers at the end.
# 4. What was the hardest part? Be as specific as possible.
#      Trying to come up with a compact way to represent this code.
# 5. How long did it take for you to complete the assignment?
#      ~ 15-30 minutes. Have prior Python Experience.

import random

def main():
    print("This is the \"guess a number\" game.")
    print("You try to guess a random number in the smallest number of attempts.")

    # upper limit
    try:
        upper_limit = int(input("Pick a positive integer: "))
        if upper_limit <= 0:
            print("The number must be positive.")
            return
    except ValueError:
        print("Please enter a valid positive integer.")
        return

    # generate random number
    secret_number = random.randint(1, upper_limit)
    print(f"Guess a number between 1 and {upper_limit}.")

    # Init var
    guesses = []
    while True:
        try:
            guess = int(input("> "))
            if guess < 1 or guess > upper_limit:
                print(f"Please guess a number between 1 and {upper_limit}.")
                continue
            guesses.append(guess)

            if guess > secret_number:
                print("\tToo high!")
            elif guess < secret_number:
                print("\tToo low!")
            else:
                print(f"You were able to find the number in {len(guesses)} guesses.")
                print(f"The numbers you guessed were: {guesses}")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
