import random
r= random.choice(["rock", "paper", "scissors"])

while True:

    a= input("Choose your first move (r/p/s): ").lower()

    if a == "r":
        print ("You chose rock. Computer chose", r)
    
    elif a == "p":
        print ("You chose paper. Computer chose", r)

    elif a == "s":
        print ("You chose scissors. Computer chose", r)
    
    else:
        print ("Invalid input. Please enter 'r', 'p', or 's'.")
        continue