#Luisa Gorman
#Guessing Game
#11/11/24
#Period 3

#Function
def guessgame():
    import random
    num = random.randint(1,10)
    guess = None
    lives = 3

    print("Welcome to the Guessing Game!")
    while guess != num:
        guess = int(input("Enter a number between 1 & 10"))
        if guess == num:
            print("Congrats! You got it!")
        else:
            if guess > num:
                print("Oops! You guessed too high! Try again!")
            else:
                print("Oops! You guessed too low! Try again!")
       




#Main
guessgame()


