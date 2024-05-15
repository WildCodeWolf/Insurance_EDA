from enum import Enum

class Sex(str, Enum):
    """The two possible values for the Sex; either `female` or `male`."""
    f = 'female'
    m = 'male'

    def __str__(self):
        return self.value