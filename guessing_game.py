# Number Guessing Game
# Built by [Meghna]
# A simple game where user guesses a random number between 1-100import random
play_again = "yes"
while play_again == "yes":
    k = random.randint(1,100)
    attempts = 0
    guess = False
    while guess == False:
        m = int(input("Enter a number between 1-100: "))
        attempts += 1
        if m == k:
            print("Correct!")
            guess = True
            break
        elif m < k:
            print("too low")
        else:
            print("too high")
            
    print("you got in",attempts,"attempts!")
    play_again = input("Do you want to play again: ")
