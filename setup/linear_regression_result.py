from scipy.stats import t
from scipy.stats._stats_mstats_common import LinregressResult
from sklearn.linear_model import LinearRegression
from statsmodels.regression.linear_model import RegressionResultsWrapper

class LinearRegressionResult:
    """A convenience class to store and access linear regression
    results from one of the three packages explored in the
    notebooks uniformly."""
    def __init__(self, result, score=None):
        self.result = result
        self._score = score

        match result:
            case LinregressResult():
                tinv = lambda p, df: abs(t.ppf(p/2, df))
                ts = tinv(.05, len(df_1) - 2)
                self._intercept_lower = result.intercept - ts * result.intercept_stderr
                self._intercept_upper = result.intercept + ts * result.intercept_stderr
                self._slope_lower = result.slope - ts * result.stderr
                self._slope_upper = result + ts * result.stderr
            case RegressionResultsWrapper():
                self._intercept_lower = result.conf_int_el(0)[0]
                self._intercept_upper = result.conf_int_el(0)[1]
                self._slope_lower = result.conf_int_el(1)[0]
                self._slope_upper = result.conf_int_el(1)[1]
    
    @property
    def intercept(self) -> float:
        match self.result:
            case LinearRegression():
                return self.result.intercept_[0]
            case LinregressResult():
                return self.result.intercept
            case RegressionResultsWrapper():
                return self.result.params.iloc[0]
    
    @property
    def intercept_lower(self) -> float | None:
        match self.result:
            case LinregressResult() | RegressionResultsWrapper():
                return self._intercept_lower
            case LinearRegression():
                return None
    
    @property
    def intercept_upper(self) -> float | None:
        match self.result:
            case LinregressResult() | RegressionResultsWrapper():
                return self._intercept_upper
            case LinearRegression():
                return None
    
    @property
    def slope(self) -> float:
        match self.result:
            case LinearRegression():
                return self.result.coef_[0, 0]
            case LinregressResult():
                return self.result.slope
            case RegressionResultsWrapper():
                return self.result.params.iloc[1]
    
    @property
    def slope_lower(self) -> float | None:
        match self.result:
            case LinregressResult() | RegressionResultsWrapper():
                return self._slope_lower
            case LinearRegression():
                return None
    
    @property
    def slope_upper(self) -> float | None:
        match self.result:
            case LinregressResult() | RegressionResultsWrapper():
                return self._slope_upper
            case LinearRegression():
                return None
    
    @property
    def score(self) -> float:
        match self.result:
            case LinearRegression():
                return self._score
            case LinregressResult():
                return self.result.rvalue**2
            case RegressionResultsWrapper():
                return self.result.rsquared

    def predict(self, *args):
        return self.result.predict(args)