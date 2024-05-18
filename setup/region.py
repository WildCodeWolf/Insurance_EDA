"""Contains the `Region` auxiliary class.
:Author: WildCodeWolf
:Date: Sat May 18 10:58:16 CEST 2024
"""
from enum import Enum

class Region(str, Enum):
    """One of the four different regions of our dataset.
    Attributes
    ----------
    sw : str
        Southwestern region.
    se : str
        Southeastern region.
    nw : str
        Northwestern region.
    ne : str
        Northeastern region.
    is_east : bool
        Whether the region is eastern.
    is_west : bool
        Whether the region is western.
    is_north : bool
        Whether the region is northern.
    is_south : bool
        Whether the region is southern.
    """
    sw = 'southwest'
    se = 'southeast'
    nw = 'northwest'
    ne = 'northeast'

    @property(doc='')
    def is_north(self) -> bool:
        """`True` if `self` is `northeast` or `northwest`.  `False` otherwise."""
        return self == self.ne or self == self.nw
    
    @property(doc='')
    def is_east(self) -> bool:
        """`True` if `self` is `northeast` or `southeast`.  `False` otherwise.`"""
        return self == self.ne or self == self.se
    
    @property(doc='')
    def is_south(self) -> bool:
        """`True` if `self` is `southeast` or `southwest`.  `False` otherwise."""
        return self == self.se or self == self.sw
    
    @property(doc='')
    def is_west(self) -> bool:
        """`True` if `self` is `northwest` or `southwest`.  `False` otherwise."""
        return self == self.nw or self == self.sw
    
    def __str__(self):
        return self.value