import random
import string
import requests

class Game:
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy()
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return self.exists(word)

    def exists(self, word):
        test = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        resultat = test.json()
        return resultat['found']
