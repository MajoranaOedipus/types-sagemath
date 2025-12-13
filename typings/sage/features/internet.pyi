from . import Feature as Feature, FeatureTestResult as FeatureTestResult

class Internet(Feature):
    '''
    A :class:`~sage.features.Feature` describing if Internet is available.

    Failure of connecting to the site "https://www.sagemath.org" within a second
    is regarded as internet being not available.

    EXAMPLES::

        sage: from sage.features.internet import Internet
        sage: Internet()
        Feature(\'internet\')
    '''
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.internet import Internet
            sage: Internet() is Internet()
            True
        """

def all_features(): ...
