from sage.rings.infinity import infinity as infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.element import AdditiveGroupElement as AdditiveGroupElement
from sage.structure.richcmp import op_EQ as op_EQ, op_NE as op_NE, richcmp as richcmp

class QmodnZ_Element(AdditiveGroupElement):
    """
    The ``QmodnZ_Element`` class represents an element of the abelian
    group `\\Q/n\\Z`.

    INPUT:

    - ``q`` -- a rational number

    - ``parent`` -- the parent abelian group `\\Q/n\\Z`

    OUTPUT: the element `q` of abelian group `\\Q/n\\Z`, in standard form

    EXAMPLES::

        sage: G = QQ/(19*ZZ)
        sage: G(400/19)
        39/19
    """
    def __init__(self, parent, x, construct: bool = False) -> None:
        """
        Create an element of `\\Q/n\\Z`.

        EXAMPLES::

            sage: G = QQ/(3*ZZ)
            sage: G.random_element().parent() is G
            True
        """
    def lift(self):
        """
        Return the smallest nonnegative rational number reducing to
        this element.

        EXAMPLES::

            sage: G = QQ/(5*ZZ)
            sage: g = G(2/4); g
            1/2
            sage: q = lift(g); q
            1/2

        TESTS::

            sage: q.parent() is QQ
            True
        """
    def __neg__(self):
        """
        Return the additive inverse of this element in `\\Q/n\\Z`.

        EXAMPLES::

            sage: from sage.groups.additive_abelian.qmodnz import QmodnZ
            sage: G = QmodnZ(5/7)
            sage: g = G(13/21)
            sage: -g
            2/21

        TESTS::

            sage: G = QmodnZ(19/23)
            sage: g = G(15/23)
            sage: -g
            4/23
            sage: g + -g == G(0)
            True
        """
    def division_by(self, other):
        """
        Division by an integer.

        .. WARNING::

            Division of `x` by `m` does not yield a well defined
            result, since there are `m` elements `y` of `\\Q/n\\Z`
            with the property that `x = my`.  We return the one
            with the smallest nonnegative lift.

        EXAMPLES::

            sage: G = QQ/(4*ZZ)
            sage: x = G(3/8)
            sage: x.division_by(4)
            3/32
        """
    def __hash__(self):
        """
        Hashing.

        TESTS::

            sage: G = QQ/(4*ZZ)
            sage: g = G(4/5)
            sage: hash(g)
            2135587864 # 32-bit
            -7046029254386353128 # 64-bit
            sage: hash(G(3/4))
            527949074 # 32-bit
            3938850096065010962 # 64-bit
            sage: hash(G(1))
            1
        """
    def additive_order(self):
        """
        Return the order of this element in the abelian group `\\Q/n\\Z`.

        EXAMPLES::

            sage: G = QQ/(12*ZZ)
            sage: g = G(5/3)
            sage: g.additive_order()
            36
            sage: (-g).additive_order()
            36
        """
