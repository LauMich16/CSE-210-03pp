import random

class Puzzle:

    def __init__(self):
        self._puzzle_list = ["jumper", "hangman", "wizard", "torpedo", "banana", "america",]
        self._current_puzzle = ""
        self.revealed_puzzle = []
        self._guessed_letter = ""
        self.incorrect_guesses = 0

    def get_puzzle(self):
        """Gets a puzzle from the list of puzzles"""
        self._current_puzzle = random.choice(self._puzzle_list)
        self.convert_curr_puzzle_to_dashes()

    def get_guess(self, guess):
        """Gets the guess from the user"""
        self._guessed_letter = guess

    def is_guess_right(self):
        """Determines if the letter guessed is inside the current puzzle"""
        if self._guessed_letter in self._current_puzzle:
            return True
        self.incorrect_guesses += 1
        return False

    def is_solved(self):
        """Determines if the puzzle has been solved"""
        if self.revealed_puzzle.count("_") > 0:
            return False
        return True
    
    def convert_curr_puzzle_to_dashes(self):
        """Converts the current puzzle to a list of dashes to be stored in revealed puzzle"""
        for i in range(len(self._current_puzzle)):
            self.revealed_puzzle.append("_")
    
    def reveal_puzzle(self):
        """Adds the guessed letter to the right indexes in the revealed puzzle list if the letter is located in the list"""
        for letter in range(len(self._current_puzzle)):
            if self._current_puzzle[letter] == self._guessed_letter:
                self.revealed_puzzle[letter] = self._current_puzzle[letter]

    def display_revealed_puzzle(self):
        """Displays the revealed puzzle in a readable format"""
        for i in self.revealed_puzzle:
            print(i, end=" ")
        print("")