"""Contains the `LinearRegression` auxiliary class.
:Author: WildCodeWolf
:Date: Sat May 18 10:58:16 CEST 2024
"""
import numpy as np
from scipy.stats import t
from scipy.stats._stats_mstats_common import LinregressResult
from sklearn.linear_model import LinearRegression
from statsmodels.regression.linear_model import RegressionResultsWrapper
import statsmodels.api as sm

from .data import df_low

class LinearRegressionResult:
    """A convenience class to store and access linear regression
    results from one of the three packages explored in the
    notebooks uniformly.
    Parameters
    ----------
    result :
        Return value of the respective regression (fitting) function.
    score :
        Score of the fit.  Required *only* for a `LinearRegression` result,
        as accessing it without keeping track of the original arguments for
        the model is not possible.
    Attributes
    ----------
    intercept : float
        The computed intercept.
    intercept_lower : float | None
        The computed lower confidence margin (95%) for the intercept.
    intercept_upper : float | None
        The computed upper confidence margin (95%) for the intercept.
    slope : float
        The computed slope.
    slope_lower : float | None
        The computed lower confidence margin (95%) for the slope.
    slope_upper : float | None
        The computed upper confidence margin (95%) for the slope.
    score : float
        The regression's :math:`R^2` score.
    """
    def __init__(self, result: LinearRegression | LinregressResult | RegressionResultsWrapper, score: float | None = None):
        self.result = result
        self._score = score if score is not None else 0.0

        match result:
            case LinregressResult():
                tinv = lambda p, df: abs(t.ppf(p/2, df))
                ts = tinv(.05, len(df_low) - 2)
                self._intercept_lower = result.intercept - ts * result.intercept_stderr
                self._intercept_upper = result.intercept + ts * result.intercept_stderr
                self._slope_lower = result.slope - ts * result.stderr
                self._slope_upper = result + ts * result.stderr
            case RegressionResultsWrapper():
                self._intercept_lower = result.conf_int_el(0)[0]
                self._intercept_upper = result.conf_int_el(0)[1]
                self._slope_lower = result.conf_int_el(1)[0]
                self._slope_upper = result.conf_int_el(1)[1]
    
    @property(doc='')
    def intercept(self) -> float:
        """The intercept."""
        match self.result:
            case LinearRegression():
                return self.result.intercept_[0]
            case LinregressResult():
                return self.result.intercept
            case RegressionResultsWrapper():
                return self.result.params.iloc[0]
    
    @property(doc='')
    def intercept_lower(self) -> float | None:
        """The lower confidence margin for the intercept (95%)."""
        match self.result:
            case LinregressResult() | RegressionResultsWrapper():
                return self._intercept_lower
            case LinearRegression():
                return None
    
    @property(doc='')
    def intercept_upper(self) -> float | None:
        """The upper confidence margin for the intercept (95%)."""
        match self.result:
            case LinregressResult() | RegressionResultsWrapper():
                return self._intercept_upper
            case LinearRegression():
                return None
    
    @property(doc='')
    def slope(self) -> float:
        """The slope."""
        match self.result:
            case LinearRegression():
                return self.result.coef_[0, 0]
            case LinregressResult():
                return self.result.slope
            case RegressionResultsWrapper():
                return self.result.params.iloc[1]
    
    @property(doc='')
    def slope_lower(self) -> float | None:
        """The lower confidence margin for the slope (95%)."""
        match self.result:
            case LinregressResult() | RegressionResultsWrapper():
                return self._slope_lower
            case LinearRegression():
                return None
    
    @property(doc='')
    def slope_upper(self) -> float | None:
        """The upper confidence margin for the slope (95%)."""
        match self.result:
            case LinregressResult() | RegressionResultsWrapper():
                return self._slope_upper
            case LinearRegression():
                return None
    
    @property(doc='')
    def score(self) -> float:
        """The score."""
        match self.result:
            case LinearRegression():
                return self._score
            case LinregressResult():
                return self.result.rvalue**2
            case RegressionResultsWrapper():
                return self.result.rsquared

    def predict(self, *args) -> pd.Series:
        """Return the model's prediction for the given input.

        If the stored model is *NOT* from `statsmodels.api`, you need
        to pass the input as you would to the respective models.
        Otherwise, you can pass the `x`-value(s) directly.
        """
        match self.result:
            case LinearRegression() | LinregressResult():
                return self.result.predict(args)
            case RegressionResultsWrapper():
                return self.result.predict(sm.add_constant(*args))