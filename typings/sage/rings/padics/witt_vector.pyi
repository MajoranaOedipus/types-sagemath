from sage.misc.functional import log as log
from sage.misc.latex import tuple_function as tuple_function
from sage.modules.free_module_element import vector as vector
from sage.rings.integer import Integer as Integer
from sage.rings.padics.factory import QqFP as QqFP, Zp as Zp
from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base as MPolynomialRing_base
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic as PolynomialRing_generic
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.element import CommutativeRingElement as CommutativeRingElement
from sage.structure.richcmp import op_EQ as op_EQ, op_NE as op_NE

class WittVector(CommutativeRingElement):
    """
    Base class for truncated Witt vectors.

    EXAMPLES::

        sage: W = WittVectorRing(GF(25), p=5, prec=3)
        sage: W(12)
        (2, 1, 3)

        sage: W = WittVectorRing(Integers(6), p=3, prec=4)
        sage: w = W([1,2,3,4]) * W([4,5,0,0])
        sage: w
        (4, 1, 3, 4)

        sage: TestSuite(w).run()
    """
    def __init__(self, parent, vec=None) -> None:
        """
        Common class for all kinds of Witt vectors.

        EXAMPLES::

            sage: W = WittVectorRing(GF(3))
            sage: e = W.one(); e
            (1)
            sage: e^2
            (1)
            sage: -e
            (2)

            sage: W = WittVectorRing(GF(3), prec=4)
            sage: t = W([1,2,0,1])
            sage: t^2
            (1, 1, 0, 2)
            sage: -t
            (2, 1, 0, 2)
            sage: 1/t
            (1, 1, 1, 0)

            sage: W = WittVectorRing(ZZ, p=5, prec=2)
            sage: WW = WittVectorRing(ZZ, p=5, prec=2)
            sage: W((4,10)) * WW((-5,12,1))
            (-20, -18362)
            sage: WW((1,2,3)) + W((1,2))
            (2, -2)
        """
    def __getitem__(self, i):
        """
        Return the ``i``-th coordinate of ``self``.

        EXAMPLES::

            sage: W = WittVectorRing(ZZ, p=2, prec=4)
            sage: t = W([-1,2,-4,8])
            sage: t[2]
            -4
        """
    def __hash__(self) -> int:
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: W = WittVectorRing(GF(3), prec=4)
            sage: t = W([1,2,0,1])
            sage: hash(t)  # random
            -2438844084280889141
        """
    def __invert__(self):
        """
        Return the inverse of ``self``.

        EXAMPLES::

            sage: W = WittVectorRing(GF(3), prec=3)
            sage: w = W([1,1,1])
            sage: ~w
            (1, 2, 0)
            sage: W = WittVectorRing(GF(3), prec=4)
            sage: w = W([1,2,0,1])
            sage: ~w
            (1, 1, 1, 0)
            sage: W = WittVectorRing(QQ, p=3, prec=4)
            sage: w = W([1,1,1,1])
            sage: ~w
            (1, -1/4, -81/832, -12887559/359956480)
        """
    def __len__(self) -> int:
        """
        Return the length of ``self``.

        EXAMPLES::

            sage: W = WittVectorRing(QQ, p=11, prec=100)
            sage: t = W.zero()
            sage: len(t)
            100
        """
    def coordinates(self):
        """
        Return the underlying tuple of the truncated Witt vector.

        EXAMPLES::

            sage: W = WittVectorRing(GF(7), p=7, prec=3)
            sage: v = W([1,2,3])
            sage: v.coordinates()
            (1, 2, 3)
        """

class WittVector_phantom(WittVector):
    """
    Child class for truncated Witt vectors using the ``phantom``
    algorithm.

    Here, a Witt vector with coefficients in `\\mathbb F_q` (respectively in a
    polynomial ring over that field), is lifted to another Witt vector with
    coefficients in `\\mathbb Q_q` (respectively in the corresponding
    polynomial ring with coefficients in that field), whose phantom components
    are stored. Computations are done with these phantom components, and the
    corresponding Witt vectors in `\\mathbb F_q` (respectively in the
    polynomial ring) are computed from them only when needed.

    EXAMPLES::

        sage: W = WittVectorRing(GF(7), prec=5)
        sage: t = W.one()
        sage: t
        (1, 0, 0, 0, 0)
        sage: t.phantom()
        (1, 1, 1, 1, 1)
        sage: u = 7*t
        sage: u.phantom(lift=True)
        (7, 7, 7, 7, 7)
        sage: u[1]
        1
    """
    def __init__(self, parent, vec=None, phantom=None) -> None:
        """
        Initialises ``self`` from the data.

        EXAMPLES::

            sage: W = WittVectorRing(GF(7), prec=3)
            sage: e = W.one(); e
            (1, 0, 0)
            sage: 7*e
            (0, 1, 0)
        """
    def __getitem__(self, i):
        """
        Return the ``i``-th coordinate of ``self``.

        EXAMPLES::

            sage: W = WittVectorRing(GF(13,'t'), prec=3)
            sage: t = W([10,5,2])
            sage: t[1]
            5
        """
    def coordinates(self):
        """
        Return the underlying tuple of the truncated Witt vector.

        EXAMPLES::

            sage: W = WittVectorRing(GF(7), p=7, prec=3)
            sage: v = W([1,2,3])
            sage: v.coordinates()
            (1, 2, 3)
        """
    def phantom(self, lift: bool = False):
        """
        Return the phantom components of the lift of ``self``.

        INPUT:

        - ``lift`` -- a Boolean (default: ``False``). When ``True``, return
          the phantom components in the lift of the coefficient ring.

        EXAMPLES::

            sage: W = WittVectorRing(GF(5,'t'), prec=3)
            sage: t = W([1,1,3])
            sage: t.phantom()
            (1, 1, 1)
            sage: t.phantom(lift=True)
            (1, 1 + 5, 1 + 5 + 3*5^2)
        """

class WittVector_finotti(WittVector):
    """
    Child class for truncated Witt vectors using Finotti's algorithm.

    EXAMPLES::

        sage: W = WittVectorRing(GF(7), prec=4, algorithm='finotti')
        sage: 49*W.one()
        (0, 0, 1, 0)
    """
class WittVector_pinvertible(WittVector):
    """
    Child class for truncated Witt vectors using the ``p_invertible``
    algorithm.

    EXAMPLES::

        sage: W = WittVectorRing(QQ, p=3, prec=3)
        sage: t = W.random_element()
        sage: t-t
        (0, 0, 0)
    """
class WittVector_standard(WittVector):
    """
    Child class for truncated Witt vectors using the ``standard`` algorithm.

    EXAMPLES::

        sage: W = WittVectorRing(GF(5), prec=3, algorithm='standard')
        sage: 5*W.one()
        (0, 1, 0)
    """
