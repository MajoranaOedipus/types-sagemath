from . import Feature as Feature, FeatureTestResult as FeatureTestResult, PythonModule as PythonModule
from .join_feature import JoinFeature as JoinFeature

class MIPBackend(Feature):
    """
    A :class:`~sage.features.Feature` describing whether a :class:`MixedIntegerLinearProgram` backend is available.
    """

class CPLEX(MIPBackend):
    """
    A :class:`~sage.features.Feature` describing whether the :class:`MixedIntegerLinearProgram` backend ``CPLEX`` is available.
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.mip_backends import CPLEX
            sage: CPLEX()._is_present()  # optional - cplex
            FeatureTestResult('cplex', True)
        """

class Gurobi(MIPBackend):
    """
    A :class:`~sage.features.Feature` describing whether the :class:`MixedIntegerLinearProgram` backend ``Gurobi`` is available.
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.mip_backends import Gurobi
            sage: Gurobi()._is_present()  # optional - gurobi
            FeatureTestResult('gurobi', True)
        """

class COIN(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing whether the :class:`MixedIntegerLinearProgram` backend ``COIN`` is available.
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.mip_backends import COIN
            sage: COIN()._is_present()  # optional - sage_numerical_backends_coin
            FeatureTestResult('sage_numerical_backends_coin', True)
        """

class CVXOPT(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing whether the :class:`MixedIntegerLinearProgram` backend ``CVXOPT`` is available.
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.mip_backends import CVXOPT
            sage: CVXOPT()._is_present()  # optional - cvxopt
            FeatureTestResult('cvxopt', True)
        """

def all_features(): ...
