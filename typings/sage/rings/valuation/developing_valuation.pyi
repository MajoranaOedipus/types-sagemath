from .valuation import DiscretePseudoValuation as DiscretePseudoValuation
from _typeshed import Incomplete
from collections.abc import Generator
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method

class DevelopingValuation(DiscretePseudoValuation):
    """
    Abstract base class for a discrete valuation of polynomials defined over
    the polynomial ring ``domain`` by the `\\phi`-adic development.

    EXAMPLES::

        sage: R.<x> = QQ[]
        sage: v = GaussValuation(R, QQ.valuation(7))

    TESTS::

        sage: TestSuite(v).run()                # long time                             # needs sage.geometry.polyhedron
    """
    def __init__(self, parent, phi) -> None:
        """
        TESTS::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, QQ.valuation(7))
            sage: from sage.rings.valuation.developing_valuation import DevelopingValuation
            sage: isinstance(v, DevelopingValuation)
            True
        """
    def phi(self):
        """
        Return the polynomial `\\phi`, the key polynomial of this valuation.

        EXAMPLES::

            sage: R = Zp(2,5)
            sage: S.<x> = R[]                                                           # needs sage.libs.ntl
            sage: v = GaussValuation(S)                                                 # needs sage.libs.ntl
            sage: v.phi()                                                               # needs sage.libs.ntl
            (1 + O(2^5))*x

        Use
        :meth:`~sage.rings.valuation.inductive_valuation.InductiveValuation.augmentation_chain`
        to obtain the sequence of key polynomials of an
        :class:`~sage.rings.valuation.inductive_valuation.InductiveValuation`::

            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, QQ.valuation(2))
            sage: v = v.augmentation(x, 1)
            sage: v = v.augmentation(x^2 + 2*x + 4, 3)

            sage: v
            [ Gauss valuation induced by 2-adic valuation, v(x) = 1, v(x^2 + 2*x + 4) = 3 ]

            sage: [w.phi() for w in v.augmentation_chain()[:-1]]
            [x^2 + 2*x + 4, x]

        A similar approach can be used to obtain the key polynomials and their
        corresponding valuations::

            sage: [(w.phi(), w.mu()) for w in v.augmentation_chain()[:-1]]
            [(x^2 + 2*x + 4, 3), (x, 1)]

        """
    def effective_degree(self, f, valuations=None):
        """
        Return the effective degree of ``f`` with respect to this valuation.

        The effective degree of `f` is the largest `i` such that the valuation
        of `f` and the valuation of `f_i\\phi^i` in the development `f=\\sum_j
        f_j\\phi^j` coincide (see [Mac1936II]_ p.497.)

        INPUT:

        - ``f`` -- a nonzero polynomial in the domain of this valuation

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R = Zp(2,5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: v.effective_degree(x)
            1
            sage: v.effective_degree(2*x + 1)
            0
        """
    def coefficients(self, f) -> Generator[Incomplete]:
        """
        Return the `\\phi`-adic expansion of ``f``.

        INPUT:

        - ``f`` -- a monic polynomial in the domain of this valuation

        OUTPUT:

        An iterator `f_0, f_1, \\dots, f_n` of polynomials in the domain of this
        valuation such that `f=\\sum_i f_i\\phi^i`

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R = Qp(2,5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: f = x^2 + 2*x + 3
            sage: list(v.coefficients(f))  # note that these constants are in the polynomial ring
            [1 + 2 + O(2^5), 2 + O(2^6), 1 + O(2^5)]
            sage: v = v.augmentation( x^2 + x + 1, 1)
            sage: list(v.coefficients(f))
            [(1 + O(2^5))*x + 2 + O(2^5), 1 + O(2^5)]
        """
    def newton_polygon(self, f, valuations=None):
        """
        Return the Newton polygon of the `\\phi`-adic development of ``f``.

        INPUT:

        - ``f`` -- a polynomial in the domain of this valuation

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R = Qp(2,5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S)
            sage: f = x^2 + 2*x + 3
            sage: v.newton_polygon(f)                                                   # needs sage.geometry.polyhedron
            Finite Newton polygon with 2 vertices: (0, 0), (2, 0)
            sage: v = v.augmentation( x^2 + x + 1, 1)
            sage: v.newton_polygon(f)                                                   # needs sage.geometry.polyhedron
            Finite Newton polygon with 2 vertices: (0, 0), (1, 1)
            sage: v.newton_polygon( f * v.phi()^3 )                                     # needs sage.geometry.polyhedron
            Finite Newton polygon with 2 vertices: (3, 3), (4, 4)
        """
    @abstract_method
    def valuations(self, f) -> None:
        """
        Return the valuations of the `f_i\\phi^i` in the expansion `f=\\sum f_i\\phi^i`.

        INPUT:

        - ``f`` -- a polynomial in the domain of this valuation

        OUTPUT:

        A list, each entry a rational numbers or infinity, the valuations of
        `f_0, f_1\\phi, \\dots`

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R = Qp(2,5)
            sage: S.<x> = R[]
            sage: v = GaussValuation(S, R.valuation())
            sage: f = x^2 + 2*x + 16
            sage: list(v.valuations(f))
            [4, 1, 0]
        """
