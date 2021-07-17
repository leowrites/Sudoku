# changing all np array to list

class Subgrid:
    def __init__(self, num:int):
        self.num = num
        self.avaliable_numbers = [i for i in range(1, 10)]
    
    def remove_number(self, value:int)->None:
        """Remove number from avaliable numbers"""
        self.avaliable_numbers.remove(value)
    
    def add_number(self, value:int)->None:
        """Add a number to avaliable numbers where there is a 0"""
        self.avaliable_numbers.append(value)
    
    def is_full(self):
        """Return True if there are no more avaliable numbers (no more options)"""
        if not self.avaliable_numbers:
            return True