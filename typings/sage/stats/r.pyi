from _typeshed import Incomplete
from sage.interfaces.r import R as R

myR: Incomplete

def ttest(x, y, conf_level: float = 0.95, **kw):
    """
    T-Test using R.

    INPUT:

    - ``x``, ``y`` -- vectors of same length
    - ``conf_level`` -- confidence level of the interval, [0,1) in percent

    OUTPUT:

    Tuple: (p-value, R return object)

    EXAMPLES::

        sage: a, b = ttest([1,2,3,4,5],[1,2,3,3.5,5.121]); a  # abs tol 1e-12  # optional - rpy2
        0.9410263720274274
    """
