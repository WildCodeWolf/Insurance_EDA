"""Contains the `Col` auxiliary class.
:Author: WildCodeWolf
:Date: Sat May 18 10:58:16 CEST 2024
"""
from enum import Enum

class Col(str, Enum):
    """One of the column names of the dataset.
    
    The further down the data exploration goes, the more columns
    are defined and frequently used.  Those columns are available
    in here as well.
    
    The column names do not aim to be Python-friendly, but instead
    produce meaningful or nice outputs on plots and graphs (which
    is why there is also some LaTeX syntax in one of them.)

    Attributes
    ----------
    age : str
        The age column.
    age2 : str
        The :math:`age^2` column.
    bmi : str
        The BMI column.
    bmi30 : str
        The :math:`\mathtt{BMI} \leq 30` column.
    charges : str
        The charges column.
    children : str
        The children column.
    children_cat : str
        The children category column.
    line : str
        The line column.
    offsets : str
        The offsets column.
    region : str
        The region column.
    sex : str
        The sex column.
    smoker : str
        The smoker column.
    """
    age          = 'age'
    """The 'age' column.  Can also be accessed via `df.age`."""
    age2         = '$age^2$'
    """The '$age^2$' column."""
    bmi          = 'bmi'
    """The 'bmi' column.  Can also be accessed via `df.bmi`."""
    bmi30        = 'BMI <= 30'
    """The 'BMI <= 30' column."""
    charges      = 'charges'
    """The 'charges' column.  Can also be accessed via `df.charges`."""
    children     = 'children'
    """The 'children' column.  Can also be accessed via `df.children`."""
    children_cat = 'children category'
    """The 'children category' column."""
    line         = 'line'
    """The 'line' column.  Can also be accessed via `df.line` if the column has been defined."""
    offsets      = 'offsets'
    """The 'offsets' column.  Can also be accessed via `df.offsets` if the column has been defined."""
    region       = 'region'
    """The 'region' column.  Can also be accessed via `df.region`."""
    sex          = 'sex'
    """The 'sex' column.  Can also be accessed via `df.sex`."""
    smoker       = 'smoker'
    """The 'smoker' column.  Can also be accessed via `df.smoker`."""
    
    def __str__(self) -> str:
        return self.value
    
    @staticmethod
    def pythonify(name: str) -> str:
        """Return a Python-friendly column name for the given one."""
        return name.lower().replace(' ', '_').replace('^', '_').replace('$', '')
