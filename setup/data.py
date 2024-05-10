import pandas as pd

from .col import Col, DF
from .sex import Sex
from .region import Region
from .utils import to_bool

df = pd.DataFrame(DF)
df[Col.sex] = df.sex.apply(Sex.parse)
df[Col.smoker] = df.smoker.apply(to_bool)
df[Col.region] = df.region.apply(Region)