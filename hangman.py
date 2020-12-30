import random

# store previous inputs
input_list = []

# replace characters in word with " _ "
guess_word = []

# define list of easy words
easy_words = ["apple","baby","actor","dancer","dog","cat","bear","winter","summer","friend","angry","animal","sugar","sand","shoe","dark","female","parent","family","school","money","chips","water","food","class","teacher","frame","picture","movie","music","foot","hand","model","father","mother","daughter","holiday","tree","pet","frog","horse","sun","moon","stairs","ladder","morning","night","dark","funny","comedy"]

# randomize words
random_easy = random.choice(easy_words)

# define list of medium words
med_words = ["destruction","advertisement","apparatus","argument","authority","automatic","announcement","attraction","punishment","acknowledgement","adequate","diversity","aristocracy","benevolent","cognitive","conjunction","environment","neuroscience","gregarious","ethinicity","infrastructure","paradigm","seasoning","invisible","staircase","television","relationship","crosswalk","mechanic","different","mississippi"]

# randomize words
random_med = random.choice(med_words)

# define list of difficult sentences
hard_words = ["you are my sunshine","xylophone","squawk","mnemonic","grogginess","frazzled","be careful","the dog is barking","the cat is purring","the phone is ringing","it is past your curfew","it is bedtime","when you wish upon a star","i am happy","i love to sing in the shower","my favorite color is blue","stop drop and roll","i love karaoke","it is cold in the winter","it is hot in the summer","the united states of america"]

# randomize words
random_hard = random.choice(hard_words)

# begin game
print("Do you want to begin? Types yes")
user_choice = input("Do you want to begin? Type yes").lower()
if user_choice == "yes":
    print("What level of difficulty? Type easy, medium, or difficult to begin.")
elif user_choice == "no":
    print("No worries! Game will not begin.")

# user's difficulty level
game_level = input ("What level of difficulty? Type easy, medium, or difficult to begin.").lower()

# tell the difference between levels - total characters
if game_level == "easy":
    # replace characters with " _ "
    for x in random_easy:
        guess_word.append(" _ ")
    # print total character's in random word
    print("There are" , len(random_easy) , "total letters. Guess a letter.")
elif game_level == "medium":
    # replace characters with " _ "
    for x in random_med:
        guess_word.append(" _ ")
    # print total character's in random word
    print("There are" , len(random_med) , "total letters. Guess a letter.")
elif game_level == "hard":
    # replace characters with " _ "
    for x in random_hard:
        guess_word.append(" _ ")
    # print total character's in random word
    print("There are" , len(random_hard) , "total letters. Guess a letter.")
elif game_level != ["easy" , "medium" , "hard"]:
    print("Invalid input. Please type easy, medium, or hard.")

# easy game begin

# loop the game until word is guessed
while game_level == "easy":

    # define user's guesses
    user_guess = input("Guess a letter.").lower()

    # if user does not guess a correct letter
    if user_guess not in str(random_easy):
        input_list.append(user_guess)
        print("There is no" , user_guess , "in the word. Try again.")
        print(" ".join(guess_word))
    # if user guesses same letter more than once
    elif user_guess in input_list:
        print("You already guessed that letter. Try again.")
    # if user guesses more than one letter
    elif len(user_guess) > 1:
        print("Please only guess one letter at a time. Try again.")
    # if user guesses a correct letter
    else:
        if user_guess in random_easy:
            input_list.append(user_guess)
            print("Yay! The letter" , user_guess , "is in the word.")
            # show user's correct guess the amount of times it occurs
            for x in range(0 , len(random_easy)):
                if random_easy[x] == user_guess:
                    guess_word[x] = user_guess
            print(" ".join(guess_word))
            if not " _ " in guess_word:
                print("You won! The word was" , random_easy)
                print("Thanks for playing!")

# medium game begin

# loop the game until word is guessed
while game_level == "medium":

    # define user's guesses
    user_guess = input("Guess a letter.").lower()

    # if user does not guess a correct letter
    if user_guess not in str(random_med):
        input_list.append(user_guess)
        print("There is no" , user_guess , "in the word. Try again.")
        print(" ".join(guess_word))
    # if user guesses same letter more than once
    elif user_guess in input_list:
        print("You already guessed that letter. Try again.")
    # if user guesses more than one letter
    elif len(user_guess) > 1:
        print("Please only guess one letter at a time. Try again.")
    # if user guesses a correct letter
    else:
        if user_guess in random_med:
            input_list.append(user_guess)
            print("Yay! The letter" , user_guess , "is in the word.")
            # show user's correct guess the amount of times it occurs
            for x in range(0 , len(random_med)):
                if random_med[x] == user_guess:
                    guess_word[x] = user_guess
            print(" ".join(guess_word))
            if not " _ " in guess_word:
                print("You won! The word was" , random_med)
                print("Thanks for playing!")

# hard game begin

# loop the game until word is guessed
while game_level == "hard":

    # define user's guesses
    user_guess = input("Guess a letter.").lower()

    # if user does not guess a correct letter
    if user_guess not in str(random_hard):
        input_list.append(user_guess)
        print("There is no" , user_guess , "in the word. Try again.")
        print(" ".join(guess_word))
    # if user guesses same letter more than once
    elif user_guess in input_list:
        print("You already guessed that letter. Try again.")
    # if user guesses more than one letter
    elif len(user_guess) > 1:
        print("Please only guess one letter at a time. Try again.")
    # if user guesses a correct letter
    else:
        if user_guess in random_hard:
            input_list.append(user_guess)
            print("Yay! The letter" , user_guess , "is in the word.")
            # show user's correct guess the amount of times it occurs
            for x in range(0 , len(random_hard)):
                if random_hard[x] == user_guess:
                    guess_word[x] = user_guess
            print(" ".join(guess_word))
            if not " _ " in guess_word:
                print("You won! The word was" , random_hard)
                print("Thanks for playing!")