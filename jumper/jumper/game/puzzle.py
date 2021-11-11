class Puzzle:

    def __init__(self):
        self._puzzle_list = []
        self._current_puzzle = ""
        self.revealed_puzzle = []
        self._guessed_letter = ""
        self.incorrect_guesses = 0

    def get_curr_puzzle(self):
        """Gets a puzzle from the list of puzzles"""

    def get_guess(self, guess):
        """Gets the guess from the user"""

    def is_guess_right(self):
        """Determines if the letter guessed is inside the current puzzle"""

    def is_solved(self):
        """Determines if the puzzle has been solved"""
    
    def convert_curr_puzzle_to_dashes(self):
        """Converts the current puzzle to a list of dashes to be stored in revealed puzzle"""
    
    def reveal_puzzle(self):
        """Adds the guessed letter to the right indexes in the revealed puzzle list if the letter is located in the list"""

    def display_revealed_puzzle(self):
        """Displays the revealed puzzle in a readable format"""