from .qmodnz_element import QmodnZ_Element as QmodnZ_Element
from _typeshed import Incomplete
from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups as CommutativeAdditiveGroups
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class QmodnZ(Parent, UniqueRepresentation):
    """
    The ``QmodnZ`` class represents the abelian group `\\Q/n\\Z`.

    INPUT:

    The constructor may be called in any of the following ways.

    #. ``QmodnZ(n)``, where

        - ``n`` -- a rational number (including 0 or negative rational numbers)

    #. ``QQ/(n*ZZ)``, where

        - ``n`` -- integer (including 0 or negative integers)

    OUTPUT: the abelian group `\\Q/n\\Z`

    EXAMPLES::

        sage: from sage.groups.additive_abelian.qmodnz import QmodnZ
        sage: QQ/(19*ZZ)
        Q/19Z

        sage: QmodnZ(19)
        Q/19Z

        sage: QmodnZ(2/3)
        Q/(2/3)Z
    """
    Element = QmodnZ_Element
    n: Incomplete
    def __init__(self, n: int = 1) -> None:
        """
        Initialization.

        EXAMPLES::

            sage: from sage.groups.additive_abelian.qmodnz import QmodnZ
            sage: G = QmodnZ(2)
            sage: G
            Q/2Z

        TESTS::

            sage: G = QQ/(19*ZZ)
            sage: TestSuite(G).run()
        """
    def some_elements(self) -> list:
        """
        Return some elements, for use in testing.

        TESTS::

            sage: L = (QQ/ZZ).some_elements()
            sage: len(L)
            92
        """
    def random_element(self):
        """
        Return a random element of `\\Q/n\\Z`.

        The denominator is selected
        using the ``1/n`` distribution on integers, modified to return
        a positive value.  The numerator is then selected uniformly.

        EXAMPLES::

            sage: G = QQ/(6*ZZ)
            sage: G.random_element().parent() is G
            True
        """
    def __iter__(self):
        """
        Create an iterator that generates the elements of `\\Q/n\\Z` without
        repetition, organized by increasing denominator.

        For a fixed denominator, elements are listed by increasing numerator.

        EXAMPLES:

        The first 19 elements of `\\Q/5\\Z`::

            sage: import itertools
            sage: list(itertools.islice(QQ/(5*ZZ), 19r))
            [0, 1, 2, 3, 4, 1/2, 3/2, 5/2, 7/2, 9/2, 1/3, 2/3, 4/3, 5/3,
             7/3, 8/3, 10/3, 11/3, 13/3]
        """
