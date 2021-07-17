import random

class Cell:
    def __init__(self, grid=None):
        self.value = None
        self.grid = grid
        self.options = None
    
    def get_value_from_options(self):
        """
        Gives this cell a random value from the options, if options is not empty
        Options gets removed if it has been tried
        If there is no options left, it should backtrace
        """
        try:
            self.value = random.choice(self.options)
            self.options.remove(self.value)
        except ValueError:
            pass
    
    def reset_cell(self):
        """Resets the cell"""
        self.value = None
        self.options = None