from game.console import Console
from game.jumper import Jumper
from game.puzzle import Puzzle

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        puzzle (Puzzle): An instance of the class of objects known as Puzzle.
        jumper (Jumper): An instance of the class of objects known as Jumper.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._console = Console()
        self._jumper = Jumper()
        self._keep_playing = True
        self._puzzle = Puzzle()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._puzzle.get_puzzle()
        self._puzzle.display_revealed_puzzle()
        self._jumper.draw_jumper()

        while self._keep_playing:
            print("")
            print("+-----+-----+-----")
            print("")
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            print("+-----+-----+-----")

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting a guess of a letter from a user.

        Args:
            self (Director): An instance of Director.
        """
        getting_letter = True
        while getting_letter:
            try:
                guess = self._console.read("Guess a letter [a-z]:")
                if guess.lower() >= "a" and guess.lower() <= "z":
                    self._puzzle.get_guess(guess)
                    getting_letter = False
                elif len(guess) > 1:
                    print("Only a single letter is accepted here.")
                else:
                    print("Error: You suck!")
                    
            except ValueError:
                print("Only strings are allowed for this input.")
                print("")
        
    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means the puzzle is revealed and the jumper is cut if necessary.

        Args:
            self (Director): An instance of Director.
        """
        is_right = self._puzzle.is_guess_right()
        if is_right:
            self._puzzle.reveal_puzzle()
        else:
            self._jumper.cut_line()
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the hider provides a hint.

        Args:
            self (Director): An instance of Director.
        """
        self._puzzle.display_revealed_puzzle()
        print("")
        self._jumper.draw_jumper()
        print("")
        