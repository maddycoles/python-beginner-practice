import random

# define number to guess
cpu_num = int(random.randint(1,50))

# loop until guesses correctly
while True:

    # define user's guess
    user_guess = int(input("Guess a number between 1 and 50"))

    # define outcome to user guesses
    if user_guess < int(1):
        print("You guessed:", user_guess)
        print("Invalid input. Answer must be a whole number between 1 and 50.")
    elif user_guess > int(50):
        print("You guessed:", user_guess)
        print("Invalid input. Answer must be a whole number between 1 and 50.")
    elif user_guess > cpu_num:
        print("You guessed:", user_guess)
        print("Too high! Try again.")
    elif user_guess < cpu_num:
        print("You guessed:", user_guess)
        print("Too low! Try again.")
    else:
        print("You guessed:", user_guess)
        print("You guessed it! Congrats.")
        break