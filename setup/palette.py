from enum import Enum

class Palette(str, Enum):
    """One of the color palettes to be used inside the notebooks."""
    bl = 'Blues'
    cw = 'coolwarm'
    pa = 'Pastel1'

    def __str__(self):
        return self.value