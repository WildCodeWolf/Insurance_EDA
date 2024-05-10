from enum import Enum

class Sex(int, Enum):
    """The two possible values for the Sex; either `female` or `male`."""
    f = 1
    m = 2

    def __repr__(self):
        return 'female' if self == 1 else 'male'

    @staticmethod
    def parse(string):
        """Parse a string representation of the `sex` column of our data
        frame and return its respective `Sex` object.
        """
        match string:
            case 'female':
                return Sex.f
            case _:
                return Sex.m