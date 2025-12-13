from . import Feature as Feature, FeatureTestResult as FeatureTestResult, PythonModule as PythonModule
from .join_feature import JoinFeature as JoinFeature
from .sagemath import sage__libs__gap as sage__libs__gap
from _typeshed import Incomplete

class GapPackage(Feature):
    '''
    A :class:`~sage.features.Feature` describing the presence of a GAP package.

    A GAP package is "present" if it *can be* loaded, not if it *has
    been* loaded.

    .. SEEALSO::

        :class:`Feature sage.libs.gap <~sage.features.sagemath.sage__libs__gap>`

    EXAMPLES::

        sage: from sage.features.gap import GapPackage
        sage: GapPackage("grape", spkg=\'gap_packages\')
        Feature(\'gap_package_grape\')
    '''
    package: Incomplete
    def __init__(self, package, **kwds) -> None:
        '''
        TESTS::

            sage: from sage.features.gap import GapPackage
            sage: isinstance(GapPackage("grape", spkg=\'gap_packages\'), GapPackage)
            True
        '''

def all_features(): ...
