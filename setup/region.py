from enum import Enum

class Region(str, Enum):
    """One of the four different regions of our dataset."""
    sw = 'southwest'
    se = 'southeast'
    nw = 'northwest'
    ne = 'northeast'
    
    def __str__(self):
        return self.value