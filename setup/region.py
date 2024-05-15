from enum import Enum

class Region(str, Enum):
    """One of the four different regions of our dataset."""
    sw = 'southwest'
    se = 'southeast'
    nw = 'northwest'
    ne = 'northeast'

    @property
    def is_north(self):
        return self == self.ne or self == self.nw
    
    @property
    def is_east(self):
        return self == self.ne or self == self.se
    
    @property
    def is_south(self):
        return self == self.se or self == self.sw
    
    @property
    def is_west(self):
        return self == self.nw or self == self.sw
    
    def __str__(self):
        return self.value