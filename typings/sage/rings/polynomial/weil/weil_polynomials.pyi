from sage.functions.generalized import sgn as sgn
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class WeilPolynomials:
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/weil/weil_polynomials.pyx (starting at line 389)

        Iterable for Weil polynomials, i.e., integer polynomials with all complex
        roots having a particular absolute value.

        Such polynomials `f` satisfy a functional equation

        .. MATH::

            T^d f(q/T) = s q^{d/2} f(T)

        where `d` is the degree of `f`, `s` is a sign and `q^{1/2}` is the absolute value
        of the roots of `f`.

        If parallel is False, then the order of values is descending lexicographical
        (i.e., polynomials with the largest coefficients of largest degrees sort first).

        If parallel is True, then the order of values is not specified. (Beware that
        due to increased overhead, parallel execution may not yield a significant
        speedup for small problem sizes.)

        INPUT:

        - ``d`` -- integer; the degree of the polynomials

        - ``q`` -- integer; the square of the complex absolute value of the roots

        - ``sign`` -- integer (default: `1`); the sign `s` of the functional equation

        - ``lead`` -- integer (default: `1`); list of integers or pairs of integers

            These are constraints on the leading coefficients of the generated polynomials.
            If pairs `(a, b)` of integers are given, they are treated as a constraint
            of the form `\\equiv a \\pmod{b}`; the moduli must be in decreasing order by
            divisibility, and the modulus of the leading coefficient must be 0.

        - ``node_limit`` -- integer (default: ``None``)

            If set, imposes an upper bound on the number of terminal nodes during the search
            (will raise a :exc:`RuntimeError` if exceeded).

        - ``parallel`` -- boolean (default: ``False``); whether to use multiple processes

            If set, will raise an error unless this file was compiled with OpenMP support
            (see instructions at the top of :mod:`sage.rings.polynomial.weil.weil_polynomials`).

        - ``squarefree`` -- boolean (default: ``False``)

            If set, only squarefree polynomials will be returned.

        - ``polring`` -- (optional) a polynomial ring in which to construct the results

        EXAMPLES:

        Some simple cases::

            sage: from sage.rings.polynomial.weil.weil_polynomials import WeilPolynomials
            sage: list(WeilPolynomials(2,2))
            [x^2 + 2*x + 2, x^2 + x + 2, x^2 + 2, x^2 - x + 2, x^2 - 2*x + 2]
            sage: l = list(WeilPolynomials(4,2))
            sage: l[0], l[-1]
            (x^4 + 4*x^3 + 8*x^2 + 8*x + 4, x^4 - 4*x^3 + 8*x^2 - 8*x + 4)
            sage: l = list(WeilPolynomials(3, 1, sign=-1))
            sage: l[0], l[-1]
            (x^3 + x^2 - x - 1, x^3 - 3*x^2 + 3*x - 1)

        By Kronecker's theorem, a monic integer polynomial has all roots of absolute
        value 1 if and only if it is a product of cyclotomic polynomials. For such a
        product to have positive sign of the functional equation, the factors `x-1`
        and `x+1` must each occur with even multiplicity. This code confirms
        Kronecker's theorem for polynomials of degree 6::

            sage: P.<x> = PolynomialRing(ZZ)
            sage: d = 6
            sage: ans1 = list(WeilPolynomials(d, 1, 1))
            sage: ans1.sort()
            sage: l = [(x-1)^2, (x+1)^2] + [cyclotomic_polynomial(n,x)
            ....:     for n in range(3, 2*d*d) if euler_phi(n) <= d]
            sage: w = WeightedIntegerVectors(d, [i.degree() for i in l])
            sage: ans2 = [prod(l[i]^v[i] for i in range(len(l))) for v in w]
            sage: ans2.sort()
            sage: print(ans1 == ans2)
            True

        Generating Weil polynomials with prescribed initial coefficients::

            sage: w = WeilPolynomials(10,1,sign=1,lead=[3,1,1])
            sage: it = iter(w)
            sage: next(it)
            3*x^10 + x^9 + x^8 + 7*x^7 + 5*x^6 + 2*x^5 + 5*x^4 + 7*x^3 + x^2 + x + 3
            sage: w = WeilPolynomials(10,1,sign=-1,lead=[3,1,1])
            sage: it = iter(w)
            sage: next(it)
            3*x^10 + x^9 + x^8 + 6*x^7 - 2*x^6 + 2*x^4 - 6*x^3 - x^2 - x - 3

        TESTS:

        Test restriction of initial coefficients::

            sage: w1 = WeilPolynomials(10,1,sign=1,lead=3)
            sage: l1 = list(w1)
            sage: w2 = WeilPolynomials(10,1,sign=1,lead=[3,1,1])
            sage: l2 = list(w2)
            sage: l3 = [i for i in l1 if i[1] == 1 and i[2] == 1]
            sage: l2 == l3
            True

            sage: w = WeilPolynomials(4,2,lead=[(1,0),(0,2)])
            sage: l = list(w)
            sage: l[0], l[-1]
            (x^4 + 4*x^3 + 8*x^2 + 8*x + 4, x^4 - 4*x^3 + 8*x^2 - 8*x + 4)
            sage: sorted(list(set(i[3] for i in l)))
            [-4, -2, 0, 2, 4]

        Test restriction to squarefree polynomials::

            sage: for (d,q,sign) in ((6,2,1),(6,4,-1),(5,4,-1)):
            ....:     w1 = WeilPolynomials(d,q,sign=sign)
            ....:     l1 = list(w1)
            ....:     w2 = WeilPolynomials(d,q,sign=sign,squarefree=True)
            ....:     l2 = list(w2)
            ....:     l3 = [i for i in l1 if i.is_squarefree()]
            ....:     print(l2 == l3)
            True
            True
            True

        Test that :issue:`29475` is resolved::

            sage: P.<x> = QQ[]
            sage: u = x^6 + x^5 + 6*x^4 - 2*x^3 + 66*x^2 + 121*x + 1331
            sage: u.is_weil_polynomial()
            True
            sage: u in WeilPolynomials(6, 11, 1, [1,1,6])
            True
            sage: u in WeilPolynomials(6, 11, 1, [(1,0),(1,11),(6,11)])
            True

        Test that :issue:`31809` is resolved::

            sage: from sage.rings.polynomial.weil.weil_polynomials import WeilPolynomials
            sage: foo = list(WeilPolynomials(12, 3, lead=(1,0,9,2,46), squarefree=False))
            sage: bar = list(WeilPolynomials(12, 3, lead=(1,0,9,2,46), squarefree=True))
            sage: bar == [f for f in foo if f.is_squarefree()]
            True

        Test that :issue:`32348` is resolved::

            sage: list(WeilPolynomials(10, 2, lead=(1,-3,5,-5,5,-5)))
            [x^10 - 3*x^9 + 5*x^8 - 5*x^7 + 5*x^6 - 5*x^5 + 10*x^4 - 20*x^3 + 40*x^2 - 48*x + 32]

        Test that :issue:`37860` is resolved::

            sage: list(WeilPolynomials(-1, 1))
            []
            sage: list(WeilPolynomials(0, 1, sign=-1))
            []
    """
    def __init__(self, d, q, sign=..., lead=..., node_limit=..., parallel=..., squarefree=..., polring=...) -> Any:
        """WeilPolynomials.__init__(self, d, q, sign=1, lead=1, node_limit=None, parallel=False, squarefree=False, polring=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/weil/weil_polynomials.pyx (starting at line 547)

        Initialize this iterable.

        EXAMPLES::

            sage: from sage.rings.polynomial.weil.weil_polynomials import WeilPolynomials
            sage: w = WeilPolynomials(10,1,sign=1,lead=[3,1,1])
            sage: w.__init__(10,1,sign=1,lead=[3,1,-1]) # Change parameters before iterating
            sage: it = iter(w)
            sage: next(it) # Results reflect the changed parameters
            3*x^10 + x^9 - x^8 + 7*x^7 + 5*x^6 - 2*x^5 + 5*x^4 + 7*x^3 - x^2 + x + 3"""
    @overload
    def node_count(self) -> Any:
        """WeilPolynomials.node_count(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/weil/weil_polynomials.pyx (starting at line 580)

        Return the number of terminal nodes found in the tree, excluding actual solutions.

        EXAMPLES::

            sage: from sage.rings.polynomial.weil.weil_polynomials import WeilPolynomials
            sage: w = WeilPolynomials(10,1,sign=1,lead=[3,1,1])
            sage: l = list(w)
            sage: w.node_count()
            158"""
    @overload
    def node_count(self) -> Any:
        """WeilPolynomials.node_count(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/weil/weil_polynomials.pyx (starting at line 580)

        Return the number of terminal nodes found in the tree, excluding actual solutions.

        EXAMPLES::

            sage: from sage.rings.polynomial.weil.weil_polynomials import WeilPolynomials
            sage: w = WeilPolynomials(10,1,sign=1,lead=[3,1,1])
            sage: l = list(w)
            sage: w.node_count()
            158"""
    @overload
    def __iter__(self) -> Any:
        """WeilPolynomials.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/weil/weil_polynomials.pyx (starting at line 564)

        Construct the associated iterator.

        EXAMPLES::

            sage: from sage.rings.polynomial.weil.weil_polynomials import WeilPolynomials
            sage: w = WeilPolynomials(10,1,sign=1,lead=[3,1,1])
            sage: it = w.__iter__()
            sage: next(it)
            3*x^10 + x^9 + x^8 + 7*x^7 + 5*x^6 + 2*x^5 + 5*x^4 + 7*x^3 + x^2 + x + 3"""
    @overload
    def __iter__(self) -> Any:
        """WeilPolynomials.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/weil/weil_polynomials.pyx (starting at line 564)

        Construct the associated iterator.

        EXAMPLES::

            sage: from sage.rings.polynomial.weil.weil_polynomials import WeilPolynomials
            sage: w = WeilPolynomials(10,1,sign=1,lead=[3,1,1])
            sage: it = w.__iter__()
            sage: next(it)
            3*x^10 + x^9 + x^8 + 7*x^7 + 5*x^6 + 2*x^5 + 5*x^4 + 7*x^3 + x^2 + x + 3"""

class WeilPolynomials_iter:
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/weil/weil_polynomials.pyx (starting at line 234)

        Iterator created by WeilPolynomials.

        EXAMPLES::

            sage: from sage.rings.polynomial.weil.weil_polynomials import WeilPolynomials
            sage: w = WeilPolynomials(10,1,sign=1,lead=[3,1,1])
            sage: it = iter(w)
            sage: next(it)
            3*x^10 + x^9 + x^8 + 7*x^7 + 5*x^6 + 2*x^5 + 5*x^4 + 7*x^3 + x^2 + x + 3
            sage: w = WeilPolynomials(10,1,sign=-1,lead=[3,1,1])
            sage: it = iter(w)
            sage: next(it)
            3*x^10 + x^9 + x^8 + 6*x^7 - 2*x^6 + 2*x^4 - 6*x^3 - x^2 - x - 3
    """
    def __init__(self, d, q, sign, lead, node_limit, parallel, squarefree, polring=...) -> Any:
        """WeilPolynomials_iter.__init__(self, d, q, sign, lead, node_limit, parallel, squarefree, polring=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/weil/weil_polynomials.pyx (starting at line 250)

        Create an iterator for Weil polynomials.

        EXAMPLES::

            sage: from sage.rings.polynomial.weil.weil_polynomials import WeilPolynomials
            sage: w = WeilPolynomials(10,1,sign=1,lead=[3,1,1])
            sage: it = iter(w)
            sage: next(it)
            3*x^10 + x^9 + x^8 + 7*x^7 + 5*x^6 + 2*x^5 + 5*x^4 + 7*x^3 + x^2 + x + 3"""
    @overload
    def node_count(self) -> Any:
        """WeilPolynomials_iter.node_count(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/weil/weil_polynomials.pyx (starting at line 370)

        Return the number of terminal nodes found in the tree, excluding
        actual solutions.

        EXAMPLES::

            sage: from sage.rings.polynomial.weil.weil_polynomials import WeilPolynomials
            sage: w = WeilPolynomials(10,1,sign=1,lead=[3,1,1])
            sage: it = iter(w)
            sage: l = list(it)
            sage: it.node_count()
            158"""
    @overload
    def node_count(self) -> Any:
        """WeilPolynomials_iter.node_count(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/weil/weil_polynomials.pyx (starting at line 370)

        Return the number of terminal nodes found in the tree, excluding
        actual solutions.

        EXAMPLES::

            sage: from sage.rings.polynomial.weil.weil_polynomials import WeilPolynomials
            sage: w = WeilPolynomials(10,1,sign=1,lead=[3,1,1])
            sage: it = iter(w)
            sage: l = list(it)
            sage: it.node_count()
            158"""
    @overload
    def __iter__(self) -> Any:
        """WeilPolynomials_iter.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/weil/weil_polynomials.pyx (starting at line 334)

        Return the iterator (i.e. ``self``).

        EXAMPLES::

            sage: from sage.rings.polynomial.weil.weil_polynomials import WeilPolynomials
            sage: w = WeilPolynomials(10,1,sign=1,lead=[3,1,1])
            sage: it = iter(w)
            sage: it.__iter__() is it
            True"""
    @overload
    def __iter__(self) -> Any:
        """WeilPolynomials_iter.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/weil/weil_polynomials.pyx (starting at line 334)

        Return the iterator (i.e. ``self``).

        EXAMPLES::

            sage: from sage.rings.polynomial.weil.weil_polynomials import WeilPolynomials
            sage: w = WeilPolynomials(10,1,sign=1,lead=[3,1,1])
            sage: it = iter(w)
            sage: it.__iter__() is it
            True"""
    def __next__(self) -> Any:
        """WeilPolynomials_iter.__next__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/weil/weil_polynomials.pyx (starting at line 348)

        Step the iterator forward.

        EXAMPLES::

            sage: from sage.rings.polynomial.weil.weil_polynomials import WeilPolynomials
            sage: w = WeilPolynomials(10,1,sign=1,lead=[3,1,1])
            sage: it = iter(w)
            sage: next(it)
            3*x^10 + x^9 + x^8 + 7*x^7 + 5*x^6 + 2*x^5 + 5*x^4 + 7*x^3 + x^2 + x + 3"""

class dfs_manager:
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/weil/weil_polynomials.pyx (starting at line 82)

        Data structure to manage depth-first search.

        Such a structure is created and managed by an instance of ``WeilPolynomials_iter``.
        There is generally no need for a user to manipulate it directly.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def advance_exhaust(self) -> Any:
        """dfs_manager.advance_exhaust(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/weil/weil_polynomials.pyx (starting at line 177)

        Advance the tree exhaustion.

        This method should not be called directly. Instead, use the iterator
        ``WeilPolynomials_iter`` or the iterable ``WeilPolynomials``.

        TESTS::

            sage: from sage.rings.polynomial.weil.weil_polynomials import WeilPolynomials
            sage: w = WeilPolynomials(10,1,sign=1,lead=[3,1,1])
            sage: it = iter(w)
            sage: it.process.advance_exhaust()[0]
            [3, 1, 1, -5, 1, -2, 1, -5, 1, 1, 3, 0, 0]"""
    @overload
    def advance_exhaust(self) -> Any:
        """dfs_manager.advance_exhaust(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/weil/weil_polynomials.pyx (starting at line 177)

        Advance the tree exhaustion.

        This method should not be called directly. Instead, use the iterator
        ``WeilPolynomials_iter`` or the iterable ``WeilPolynomials``.

        TESTS::

            sage: from sage.rings.polynomial.weil.weil_polynomials import WeilPolynomials
            sage: w = WeilPolynomials(10,1,sign=1,lead=[3,1,1])
            sage: it = iter(w)
            sage: it.process.advance_exhaust()[0]
            [3, 1, 1, -5, 1, -2, 1, -5, 1, 1, 3, 0, 0]"""
    @overload
    def node_count(self) -> long:
        """dfs_manager.node_count(self) -> long

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/weil/weil_polynomials.pyx (starting at line 155)

        Count nodes.

        This method should not be called directly. Instead, use the ``node_count`` method
        of an instance of ``WeilPolynomials`` or ``WeilPolynomials_iter``.

        TESTS::

            sage: from sage.rings.polynomial.weil.weil_polynomials import WeilPolynomials
            sage: w = WeilPolynomials(10,1,sign=1,lead=[3,1,1])
            sage: it = iter(w)
            sage: _ = next(it)
            sage: it.process.node_count()
            158"""
    @overload
    def node_count(self) -> Any:
        """dfs_manager.node_count(self) -> long

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/weil/weil_polynomials.pyx (starting at line 155)

        Count nodes.

        This method should not be called directly. Instead, use the ``node_count`` method
        of an instance of ``WeilPolynomials`` or ``WeilPolynomials_iter``.

        TESTS::

            sage: from sage.rings.polynomial.weil.weil_polynomials import WeilPolynomials
            sage: w = WeilPolynomials(10,1,sign=1,lead=[3,1,1])
            sage: it = iter(w)
            sage: _ = next(it)
            sage: it.process.node_count()
            158"""
