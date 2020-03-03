#guess the number game
import random #random module
import time #time module

print("Hello! What is your name?")
name = input()
print("Hello there, " + name + "! " + "I am thinking of a number")
print("berween 1 and 22. Think you can guess it!?")

time.sleep(1) #wait one second before moving onto the for loop (inside while loop)

t = True #sets t to bool True to satisfy into while loop

while(t): #loop keeps running while condition is true
    randomNum = random.randint(1, 22) #selects random number between 1 and 22
    for guessesTaken in range(1, 7): #loop runs 6 times, gussesTaken variable keeps track of amount of times user guessed (between 1 and 6 times)
        print("What is your guess? You have "  + str((7 - guessesTaken)) + " guesses")
        userGuess = input() #saves user input to variable called userguess
        if int(userGuess) > randomNum: #if input user entered is higher than radnom number
            print("Your guess to too high. Please guess again")
        elif int(userGuess) < randomNum: #if input user entered is lower than radnom numer
            print("Your guess is too low. Please guess again")
        else: #if number guessed is equal to random number (not too high, not too low) program breaks out of loop before 6 iterations
            break

    if int(userGuess) == randomNum: #if user number = random number
        print("You got it! You guessed the correct number in " + str(guessesTaken) + " guess(es)!")
        print("Press y to play again")
        yes = input() 
        if yes == "y": #if user enters y to input,
            t = True #condition is still true, while loop (aka game) runs again
        else: #user enters anything else, program sets t to false, which then does not satify while loop condition - ends program
            print("Goodbye!")
            t = False
    else:
        print("Sorry! Maximum number of guesses allowed. The number was " + str(randomNum))#if for loop goes thru all 6 iterations (aka number not guessed  correctly
        print("Press y to try again")
        yes = input()
        if yes == "y": #same as if else statement in block above
            t = True #continues while loop
        else:
            print("Goodbye!")
            t = False #ends while loop
            
        

