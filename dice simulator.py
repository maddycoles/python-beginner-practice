import random

roll_again = "yes"

while roll_again == "yes":
    print("The values are..")
    print(random.randint(1,6))
    print(random.randint(1,6))

    new_roll = input("Do you want to roll again? Type yes")
    if new_roll == "yes":
        continue
    else:
        break