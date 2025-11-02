import random

def guessingGame():
wordList = ["boat", "moat", "goat", "coat","promote","wrote","note","tote"]

#chooses the word from the list to use for the guessing game
theWord = random.choice(wordList)
#multiples the amount of letters in the word (*len(theWord)) to show the amount of underscores as hidden letters (["_"]) that haven't been guessed yet (credit goes to W3Schools on "_")
guess = ["_"]*len(theWord)
#sets the amount of guesses to 5
chances = 5
#allows storage of multiple guess values with set()
guessedLetters = set()

print("Try to guess the word, one letter at at time, to win!")
print(f"There are {chances} guesses allowed!\n")

#while loop to allow for the guesses to continue
while chances > 0 and "_" in guess:
    print("The Word:", " ".join(guess))
    #add sorted to show letters guessed in order
    print("The letters guessed:", " ".join(sorted(guessedLetters)))
    #input that lowercases any letter put in to prevent error
    guessing = input("guess a letter: ").lower()
    #error catch if input is not a letter or is more than 1 letter
    if not guessing.isalpha or len(guessing) !=1:
        print("There are only single letter guesses allowed!\n")
        continue
    #error catch if they already used a letter
    if guessing in guess:
        print("That letter was already guessed!\n")
        continue

    #adds to set() with the guess
    guessedLetters.add(guessing)

    #if loop with for loop when the guess is correct, adds the letter to the hidden values of the word if there are multiple values with the same letter (like o in promote)
    if guessing in theWord:
        print("That is correct!\n")
        for i, correctguess in enumerate(theWord):
            if correctguess == guessing:
                guess[i] = guessing
    #removes a chance if incorrect guess
    else:
        chances -= 1
        print(f"That guess is incorrect! You have {chances} guesses left. Try vowels first!\n")

    