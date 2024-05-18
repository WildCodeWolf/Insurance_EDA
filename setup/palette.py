from enum import Enum

class Palette(str, Enum):
    """One of the color palettes to be used inside the notebooks.
    Attributes
    ----------
    bl : str
        Variations from white to blue.
    cw : str
        Variations from blue to red.
    pa : str
        A set of pastel colors.
    """
    bl = 'Blues'
    cw = 'coolwarm'
    pa = 'Pastel1'

    def __str__(self):
        return self.value