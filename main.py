import random


random_number = random.randint(1, 10)
score = 0
tries = 3
print("Welcome to my Number Guessing Game!")
while tries > 0:
    user_input = input("Please guess a number between 1 and 10. You have " + str(tries) + " attempt(s) remaining.\n")
    try:
           user_input == int(user_input)
           user_input = int(user_input)
           if user_input >= 1 and user_input <= 10:

                if user_input == random_number:
                    score += 1
                    print("You guessed the correct number, " + str(random_number) + " , nice job!\n")
                    break
                else:
                    tries -= 1
                    if tries == 0:
                        print("Game over, the number was " +str(random_number) + ".")
                        break
                    elif random_number > user_input:
                            print("Too low, try again.")
                    elif random_number < user_input:
                            print("Too high, try again.")
                    else:
                        print("You guessed the wrong number.")

           else:
               print("Invalid input. Must be a whole number between 1 and 10.")
    except ValueError:
        #tries -= 1
        print("Invalid input.")