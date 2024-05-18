__all__ = [
    'children',
    'col',
    'linear_regression_result',
    'palette',
    'region',
    'sex',
    'utils'
]

import seaborn as sns

from .col import Col
from .children import Children
from .palette import Palette
from .region import Region
from .sex import Sex
from .utils import quick_regression

sns.set(rc={'figure.facecolor':'#eee'})    # to produce consistently looking plots when imported