import seaborn as sns

from .col import Col, DF
from .children import Children
from .coefficient import A, B0, B1, STEP
from .data import df, df_low
from .palette import Palette
from .region import Region
from .sex import Sex
from .utils import quick_regression

sns.set(rc={'figure.facecolor':'#eee'})    # to produce consistently looking plots when imported

__all__ = [
    'children',
    'coefficient',
    'col',
    'data',
    'linear_regression_result',
    'palette',
    'region',
    'sex',
    'utils'
]