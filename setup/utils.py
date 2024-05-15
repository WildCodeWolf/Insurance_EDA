import pandas as pd
import statsmodels.api as sm

from .linear_regression_result import LinearRegressionResult

to_bool = lambda non_bool: non_bool == 'yes'

def quick_regression(x: pd.Series, y: pd.Series) -> LinearRegressionResult:
    """Perform a linear regression using the `statsmodel.api` package and return the result."""
    return LinearRegressionResult(sm.OLS(y, sm.add_constant(x)).fit())
