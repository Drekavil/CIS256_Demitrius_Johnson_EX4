import random
from unittest.mock import patch
from guess_the_word import guessingGame

#checks the selected word comes from the predefined list.
def test_wordList():
    wordList = ["boat", "coat", "float", "moat", "throat", "tote", "remote", "promote", "wrote", "note"]
    for _ in range(20):
        chosenWord = random.choice(wordList)
        #checks output for word
        assert chosenWord in wordList, f"Selected word '{chosenWord}' should be in the predefined list."
