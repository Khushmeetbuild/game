import random
r= random.randint(1,100)

while True:

    a= int(input("Guess the number from 1 to 100: "))

    if a < r:
        print ("Too low! Try again.")

    elif a > r:
        print ("Too high! Try again.")

    else:
        print ("Correct Answer!", r)

        break