from . import Executable as Executable, FeatureTestResult as FeatureTestResult
from .join_feature import JoinFeature as JoinFeature

class Lrs(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of the ``lrs``
    binary which comes as a part of ``lrslib``.

    EXAMPLES::

        sage: from sage.features.lrs import Lrs
        sage: Lrs().is_present()  # optional - lrslib
        FeatureTestResult('lrs', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.lrs import Lrs
            sage: isinstance(Lrs(), Lrs)
            True
        """
    def is_functional(self):
        """
        Test whether ``lrs`` works on a trivial input.

        EXAMPLES::

            sage: from sage.features.lrs import Lrs
            sage: Lrs().is_functional()  # optional - lrslib
            FeatureTestResult('lrs', True)
        """

class LrsNash(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of the ``lrsnash``
    binary which comes as a part of ``lrslib``.

    EXAMPLES::

        sage: from sage.features.lrs import LrsNash
        sage: LrsNash().is_present()  # optional - lrslib
        FeatureTestResult('lrsnash', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.lrs import LrsNash
            sage: isinstance(LrsNash(), LrsNash)
            True
        """
    def is_functional(self):
        """
        Test whether ``lrsnash`` works on a trivial input.

        EXAMPLES::

            sage: from sage.features.lrs import LrsNash
            sage: LrsNash().is_functional()  # optional - lrslib
            FeatureTestResult('lrsnash', True)
        """

class Lrslib(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of the executables
    :class:`lrs <Lrs>` and :class:`lrsnash <LrsNash>` provided by the :ref:`lrslib <spkg_lrslib>` package.

    EXAMPLES::

        sage: from sage.features.lrs import Lrslib
        sage: Lrslib().is_present()  # optional - lrslib
        FeatureTestResult('lrslib', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.lrs import Lrslib
            sage: isinstance(Lrslib(), Lrslib)
            True
        """

def all_features(): ...
