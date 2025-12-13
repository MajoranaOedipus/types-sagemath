from . import Executable as Executable
from .join_feature import JoinFeature as JoinFeature

class dot(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of ``dot``.

    TESTS::

        sage: from sage.features.graphviz import dot
        sage: dot().is_present()  # optional - graphviz
        FeatureTestResult('dot', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.graphviz import dot
            sage: isinstance(dot(), dot)
            True
        """

class neato(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of ``neato``.

    TESTS:

        sage: from sage.features.graphviz import neato
        sage: neato().is_present()  # optional - graphviz
        FeatureTestResult('neato', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.graphviz import neato
            sage: isinstance(neato(), neato)
            True
        """

class twopi(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of ``twopi``.

    TESTS::

        sage: from sage.features.graphviz import twopi
        sage: twopi().is_present()  # optional - graphviz
        FeatureTestResult('twopi', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.graphviz import twopi
            sage: isinstance(twopi(), twopi)
            True
        """

class Graphviz(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of
    the :class:`dot`, :class:`neato`, and :class:`twopi` executables from the
    :ref:`graphviz <spkg_graphviz>` package.

    EXAMPLES::

        sage: from sage.features.graphviz import Graphviz
        sage: Graphviz().is_present()  # optional - graphviz
        FeatureTestResult('graphviz', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.graphviz import Graphviz
            sage: isinstance(Graphviz(), Graphviz)
            True
        """

def all_features(): ...
