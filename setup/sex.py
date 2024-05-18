"""Contains the `Sex` auxiliary class.
:Author: WildCodeWolf
:Date: Sat May 18 10:58:16 CEST 2024
"""
from enum import Enum

class Sex(str, Enum):
    """The two possible values for the Sex; either `female` or `male`."""
    f = 'female'
    m = 'male'

    def __str__(self):
        return self.value