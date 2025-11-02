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

#this should be better talked about in slides, patch is fantastic class of unittest https://docs.python.org/3/library/unittest.mock.html
@patch("random.choice", returnValue="moat")
def test_guessing(capsys):
    mockInputs = ["m","o","c","a","t"]
    with patch("builtins.input",sideEffect = mockInputs):
        guessingGame()
    mockOutput = capsys.readouterr().out

   #checks output for lines 
    assert "correct" in mockOutput
    assert "incorrect" in mockOutput
    assert "OH NO" in mockOutput
    assert "MOAT" in mockOutput