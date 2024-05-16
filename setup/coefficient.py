import pandas as pd

from .col import Col
from .data import df, df_low
from .utils import quick_regression

df[Col.bmi30] = df[Col.bmi] <= 30
model = quick_regression(df[Col.age]**2, df[Col.charges])
df[Col.offsets] = df.charges - model.slope * df.age**2

df_lower = df[(df[Col.smoker]) & (df[Col.bmi30])].copy()
df_upper = df[(df[Col.smoker]) & (~df[Col.bmi30])].copy()
df_lower_filtered = df_lower[df_lower[Col.offsets] < 18.7e3].copy()
df_upper_filtered = df_upper[df_upper.eval('offsets < 5e2 * (bmi - 30) + 37e3')].copy()
df_upper_filtered_shifted = df_upper_filtered.copy()

model = quick_regression(df_low[Col.age2], df_low[Col.charges])
A = model.slope
A_lower = model.slope_lower
A_upper = model.slope_upper
B0 = model.intercept
B0_lower = model.intercept_lower
B0_upper = model.intercept_upper

STEP = df_upper_filtered[df_upper_filtered.bmi < 30.5].offsets.min() - \
    df_lower_filtered[df_lower_filtered.bmi > 29.5].offsets.min()

df_upper_filtered_shifted.offsets -= STEP
df_filtered_joined = pd.concat([df_lower_filtered, df_upper_filtered_shifted], axis=0)
model = quick_regression(df_filtered_joined.bmi, df_filtered_joined.offsets)
B1 = model.slope
B1_lower = model.slope_lower
B1_upper = model.slope_upper
