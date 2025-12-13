from . import Executable as Executable
from .join_feature import JoinFeature as JoinFeature
from sage.env import RUBIKS_BINS_PREFIX as RUBIKS_BINS_PREFIX

class cu2(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of ``cu2``.

    EXAMPLES::

        sage: from sage.features.rubiks import cu2
        sage: cu2().is_present()  # optional - rubiks
        FeatureTestResult('cu2', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.rubiks import cu2
            sage: isinstance(cu2(), cu2)
            True
        """

class size222(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of ``size222``.

    EXAMPLES::

        sage: from sage.features.rubiks import size222
        sage: size222().is_present()  # optional - rubiks
        FeatureTestResult('size222', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.rubiks import size222
            sage: isinstance(size222(), size222)
            True
        """

class optimal(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of ``optimal``.

    EXAMPLES::

        sage: from sage.features.rubiks import optimal
        sage: optimal().is_present()  # optional - rubiks
        FeatureTestResult('optimal', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.rubiks import optimal
            sage: isinstance(optimal(), optimal)
            True
        """

class mcube(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of ``mcube``.

    EXAMPLES::

        sage: from sage.features.rubiks import mcube
        sage: mcube().is_present()  # optional - rubiks
        FeatureTestResult('mcube', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.rubiks import mcube
            sage: isinstance(mcube(), mcube)
            True
        """

class dikcube(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of ``dikcube``.

    EXAMPLES::

        sage: from sage.features.rubiks import dikcube
        sage: dikcube().is_present()  # optional - rubiks
        FeatureTestResult('dikcube', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.rubiks import dikcube
            sage: isinstance(dikcube(), dikcube)
            True
        """

class cubex(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of ``cubex``.

    EXAMPLES::

        sage: from sage.features.rubiks import cubex
        sage: cubex().is_present()  # optional - rubiks
        FeatureTestResult('cubex', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.rubiks import cubex
            sage: isinstance(cubex(), cubex)
            True
        """

class Rubiks(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of the
    :class:`cu2`, :class:`cubex`, :class:`dikcube`, :class:`mcube`, :class:`optimal`, and
    :class:`size222` programs from the :ref:`rubiks <spkg_rubiks>` package.

    EXAMPLES::

        sage: from sage.features.rubiks import Rubiks
        sage: Rubiks().is_present()  # optional - rubiks
        FeatureTestResult('rubiks', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.rubiks import Rubiks
            sage: isinstance(Rubiks(), Rubiks)
            True
        """

def all_features(): ...
