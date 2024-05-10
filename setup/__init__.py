import seaborn as sns

from .col import Col, DF
from .data import df
from .palette import Palette
from .region import Region
from .sex import Sex

sns.set(rc={'figure.facecolor':'#eee'})    # to produce consistently looking plots when imported

__all__ = [
    'col',
    'data',
    'palette',
    'region',
    'sex'
]