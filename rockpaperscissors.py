import random

# loop to play again

while True:
    user_choice = input("Welcome to Rock, Paper, Scissors!")

# define cpu choice as string
    random_num = random.randint(0,2)

    if random_num == 0:
        cpu_choice = "rock"
    if random_num == 1:
        cpu_choice = "paper"
    if random_num == 2:
        cpu_choice = "scissors"

 # what code shows       
    print( "Your Choice:", user_choice )
    print( "Computer's Choice:", cpu_choice)

# define player's outcome - win, lose, tie
    if user_choice == "rock":
        if cpu_choice == "rock":
            print("It's a tie!")
        elif cpu_choice == "paper":
            print("You lost!")
        else:
            print("You win!")
    if user_choice == "paper":
        if cpu_choice == "paper":
            print("It's a tie!")
        elif cpu_choice == "scissors":
            print("You lost!")
        else:
            print("You win!")
    if user_choice == "scissors":
        if cpu_choice == "scissors":
            print("It's a tie!")
        elif cpu_choice == "rock":
            print("You lost!")
        else:
            print("You win!")