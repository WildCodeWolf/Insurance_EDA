import pandas as pd

from .children import Children
from .col import Col, DF
from .linear_regression_result import LinearRegressionResult
from .sex import Sex
from .region import Region
from .utils import to_bool

df = pd.DataFrame(DF)
df[Col.children] = df.children.apply(Children)
df[Col.children_cat] = df.children.apply(Children.category)
df[Col.sex] = df.sex.apply(Sex)
df[Col.smoker] = df.smoker.apply(to_bool)
df[Col.region] = df.region.apply(Region)

df_low = pd.DataFrame(df[df.charges / df.age < 260])
df_low[Col.age2] = df_low.age**2