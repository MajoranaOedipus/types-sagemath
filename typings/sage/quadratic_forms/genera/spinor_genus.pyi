from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupElement_gap as AbelianGroupElement_gap, AbelianGroupGap as AbelianGroupGap
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ

class SpinorOperator(AbelianGroupElement_gap):
    """
    A spinor operator seen as a tuple of square classes.

    For `2` the square class is represented as one of `1,3,5,7` and for
    `p` odd it is `1` for a `p`-adic unit square and `-1` for a non-square.

    EXAMPLES::

        sage: from sage.quadratic_forms.genera.spinor_genus import *
        sage: A = SpinorOperators((2, 3, 7))
        sage: A.an_element()
        [2:7, 3:-1, 7:-1]
    """

class SpinorOperators(AbelianGroupGap):
    """
    The group of spinor operators of a genus.

    It is a product of `p`-adic unit square classes
    used for spinor genus computations.

    INPUT:

    - a tuple of primes `(p_1=2,\\dots, p_n`)

    EXAMPLES::

        sage: from sage.quadratic_forms.genera.spinor_genus import *
        sage: SpinorOperators((2, 3, 7))
        Group of SpinorOperators at primes (2, 3, 7)
    """
    def __init__(self, primes) -> None:
        """
        Initialize the group of spinor operators.

        TESTS::

            sage: from sage.quadratic_forms.genera.spinor_genus import *
            sage: S = SpinorOperators((2, 3, 7))
            sage: TestSuite(S).run()
        """
    def __reduce__(self):
        """
        Implement pickling.

        OUTPUT:

        a tuple ``f`` such that this element is ``f[0](*f[1])``

        EXAMPLES::

            sage: from sage.quadratic_forms.genera.spinor_genus import SpinorOperators
            sage: S = SpinorOperators((2, 3, 7))
            sage: S == loads(dumps(S))
            True
        """
    Element = SpinorOperator
    def to_square_class(self, x, p):
        """
        Return `(1,...,1,x,1,...,1)` with the square class of `x` at position `p`.

        INPUT:

        - ``p`` -- a prime

        - ``x`` -- nonzero rational number

        EXAMPLES::

            sage: from sage.quadratic_forms.genera.spinor_genus import SpinorOperators
            sage: AS = SpinorOperators((2, 3, 7))
            sage: AS.to_square_class(5, 7)
            [2:1, 3:1, 7:-1]
            sage: AS.to_square_class(5, 2)
            [2:5, 3:1, 7:1]
            sage: AS.to_square_class(-5, 2)
            [2:3, 3:1, 7:1]
            sage: AS.to_square_class(7, 2)
            [2:7, 3:1, 7:1]
        """
    def delta(self, r, prime=None):
        """
        Diagonal embedding of rational square classes.

        INPUT:

        - ``r`` -- a nonzero integer; if ``prime`` is ``None``, ``r`` must not
          be divisible by the defining primes of ``self``

        - ``prime`` -- (default: ``None``) a prime or `-1`

        OUTPUT:

        If a prime `p` is given, the method returns
        `\\Delta_p(r)`
        otherwise returns `\\Delta(r)`
        where both are as defined by Conway-Sloane in
        Chapter 15 9.3 of [CS1988]_.

        EXAMPLES::

            sage: from sage.quadratic_forms.genera.spinor_genus import SpinorOperators
            sage: AS = SpinorOperators((2, 3, 7))
            sage: AS.delta(5)
            [2:5, 3:-1, 7:-1]
            sage: AS.delta(2, prime=3)
            [2:1, 3:-1, 7:1]
            sage: AS.delta(11)
            [2:3, 3:-1, 7:1]
            sage: AS.delta(3, prime=7)
            [2:1, 3:1, 7:-1]
        """
