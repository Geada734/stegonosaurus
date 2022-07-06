'''Custom exceptions made for this library'''

class StegonosaurusIncorrectFormatException(Exception):
    '''Raised when a function receives a file that isn't a .PNG multiband image'''
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)