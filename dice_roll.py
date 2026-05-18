import random

while True:

    a= input ("Roll the dice? (y/n): ").lower()

    if a == "y":

        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        print ("You rolled a", dice1, "and", dice2)

    elif a == "n":
        print ("Goodbye!")

        break
    else:
        print ("Invalid input. Please enter 'y' or 'n'.")