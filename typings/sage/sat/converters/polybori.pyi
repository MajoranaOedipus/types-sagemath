from _typeshed import Incomplete
from sage.combinat.permutation import Permutations as Permutations
from sage.functions.other import ceil as ceil
from sage.misc.cachefunc import cached_function as cached_function, cached_method as cached_method
from sage.rings.integer_ring import ZZ as ZZ
from sage.sat.converters import ANF2CNFConverter as ANF2CNFConverter

class CNFEncoder(ANF2CNFConverter):
    """
    ANF to CNF Converter using a Dense/Sparse Strategy. This converter distinguishes two classes of
    polynomials.

    1. Sparse polynomials are those with at most ``max_vars_sparse`` variables. Those are converted
    using reduced truth-tables based on PolyBoRi's internal representation.

    2. Polynomials with more variables are converted by introducing new variables for monomials and
    by converting these linearised polynomials.

    Linearised polynomials are converted either by splitting XOR chains -- into chunks of length
    ``cutting_number`` -- or by constructing XOR clauses if the underlying solver supports it. This
    behaviour is disabled by passing ``use_xor_clauses=False``.

    .. automethod:: __init__
    .. automethod:: __call__
    """
    random_generator: Incomplete
    one_set: Incomplete
    empty_set: Incomplete
    solver: Incomplete
    max_vars_sparse: Incomplete
    cutting_number: Incomplete
    use_xor_clauses: Incomplete
    ring: Incomplete
    def __init__(self, solver, ring, max_vars_sparse: int = 6, use_xor_clauses=None, cutting_number: int = 6, random_seed: int = 16) -> None:
        """
        Construct ANF to CNF converter over ``ring`` passing clauses to ``solver``.

        INPUT:

        - ``solver`` -- a SAT-solver instance

        - ``ring`` -- a :class:`sage.rings.polynomial.pbori.BooleanPolynomialRing`

        - ``max_vars_sparse`` -- maximum number of variables for direct conversion

        - ``use_xor_clauses`` -- use XOR clauses; if ``None`` use if
          ``solver`` supports it. (default: ``None``)

        - ``cutting_number`` -- maximum length of XOR chains after
          splitting if XOR clauses are not supported (default: 6)

        - ``random_seed`` -- the direct conversion method uses
          randomness, this sets the seed (default: 16)

        EXAMPLES:

        We compare the sparse and the dense strategies, sparse first::

            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: from sage.sat.converters.polybori import CNFEncoder
            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: fn = tmp_filename()
            sage: solver = DIMACS(filename=fn)
            sage: e = CNFEncoder(solver, B)
            sage: e.clauses_sparse(a*b + a + 1)
            sage: _ = solver.write()
            sage: print(open(fn).read())
            p cnf 3 2
            -2 0
            1 0
            sage: e.phi
            [None, a, b, c]

        Now, we convert using the dense strategy::

            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: from sage.sat.converters.polybori import CNFEncoder
            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: fn = tmp_filename()
            sage: solver = DIMACS(filename=fn)
            sage: e = CNFEncoder(solver, B)
            sage: e.clauses_dense(a*b + a + 1)
            sage: _ = solver.write()
            sage: print(open(fn).read())
            p cnf 4 5
            1 -4 0
            2 -4 0
            4 -1 -2 0
            -4 -1 0
            4 1 0
            sage: e.phi
            [None, a, b, c, a*b]

        .. NOTE::

            This constructor generates SAT variables for each Boolean polynomial variable.
        """
    def var(self, m=None, decision=None):
        """
        Return a *new* variable.

        This is a thin wrapper around the SAT-solvers function where
        we keep track of which SAT variable corresponds to which
        monomial.

        INPUT:

        - ``m`` -- something the new variables maps to, usually a monomial
        - ``decision`` -- is this variable a decision variable?

        EXAMPLES::

            sage: from sage.sat.converters.polybori import CNFEncoder
            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: ce = CNFEncoder(DIMACS(), B)
            sage: ce.var()
            4
        """
    @property
    def phi(self):
        """
        Map SAT variables to polynomial variables.

        EXAMPLES::

            sage: from sage.sat.converters.polybori import CNFEncoder
            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: ce = CNFEncoder(DIMACS(), B)
            sage: ce.var()
            4
            sage: ce.phi
            [None, a, b, c, None]
        """
    def zero_blocks(self, f):
        """
        Divide the zero set of ``f`` into blocks.

        EXAMPLES::

            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: from sage.sat.converters.polybori import CNFEncoder
            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: e = CNFEncoder(DIMACS(), B)
            sage: sorted(sorted(d.items()) for d in e.zero_blocks(a*b*c))
            [[(c, 0)], [(b, 0)], [(a, 0)]]

        .. NOTE::

            This function is randomised.
        """
    def clauses_sparse(self, f):
        """
        Convert ``f`` using the sparse strategy.

        INPUT:

        - ``f`` -- a :class:`sage.rings.polynomial.pbori.BooleanPolynomial`

        EXAMPLES::

            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: from sage.sat.converters.polybori import CNFEncoder
            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: fn = tmp_filename()
            sage: solver = DIMACS(filename=fn)
            sage: e = CNFEncoder(solver, B)
            sage: e.clauses_sparse(a*b + a + 1)
            sage: _ = solver.write()
            sage: print(open(fn).read())
            p cnf 3 2
            -2 0
            1 0
            sage: e.phi
            [None, a, b, c]
        """
    def clauses_dense(self, f) -> None:
        """
        Convert ``f`` using the dense strategy.

        INPUT:

        - ``f`` -- a :class:`sage.rings.polynomial.pbori.BooleanPolynomial`

        EXAMPLES::

            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: from sage.sat.converters.polybori import CNFEncoder
            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: fn = tmp_filename()
            sage: solver = DIMACS(filename=fn)
            sage: e = CNFEncoder(solver, B)
            sage: e.clauses_dense(a*b + a + 1)
            sage: _ = solver.write()
            sage: print(open(fn).read())
            p cnf 4 5
            1 -4 0
            2 -4 0
            4 -1 -2 0
            -4 -1 0
            4 1 0
            sage: e.phi
            [None, a, b, c, a*b]
        """
    @cached_method
    def monomial(self, m):
        """
        Return SAT variable for ``m``.

        INPUT:

        - ``m`` -- a monomial

        OUTPUT: an index for a SAT variable corresponding to ``m``

        EXAMPLES::

            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: from sage.sat.converters.polybori import CNFEncoder
            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: fn = tmp_filename()
            sage: solver = DIMACS(filename=fn)
            sage: e = CNFEncoder(solver, B)
            sage: e.clauses_dense(a*b + a + 1)
            sage: e.phi
            [None, a, b, c, a*b]

        If monomial is called on a new monomial, a new variable is created::

            sage: e.monomial(a*b*c)
            5
            sage: e.phi
            [None, a, b, c, a*b, a*b*c]

        If monomial is called on a monomial that was queried before,
        the index of the old variable is returned and no new variable
        is created::

            sage: e.monomial(a*b)
            4
            sage: e.phi
            [None, a, b, c, a*b, a*b*c]

        .. NOTE::

            For correctness, this function is cached.
        """
    @cached_function
    def permutations(length, equal_zero):
        """
        Return permutations of length ``length`` which are equal to
        zero if ``equal_zero`` and equal to one otherwise.

        A variable is false if the integer in its position is smaller
        than zero and true otherwise.

        INPUT:

        - ``length`` -- the number of variables
        - ``equal_zero`` -- should the sum be equal to zero?

        EXAMPLES::

            sage: from sage.sat.converters.polybori import CNFEncoder
            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: ce = CNFEncoder(DIMACS(), B)
            sage: ce.permutations(3, True)
            [[-1, -1, -1], [1, 1, -1], [1, -1, 1], [-1, 1, 1]]

            sage: ce.permutations(3, False)
            [[1, -1, -1], [-1, 1, -1], [-1, -1, 1], [1, 1, 1]]
        """
    def split_xor(self, monomial_list, equal_zero):
        """
        Split XOR chains into subchains.

        INPUT:

        - ``monomial_list`` -- list of monomials
        - ``equal_zero`` -- is the constant coefficient zero?

        EXAMPLES::

            sage: from sage.sat.converters.polybori import CNFEncoder
            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: B.<a,b,c,d,e,f> = BooleanPolynomialRing()
            sage: ce = CNFEncoder(DIMACS(), B, cutting_number=3)
            sage: ce.split_xor([1,2,3,4,5,6], False)
            [[[1, 7], False], [[7, 2, 8], True], [[8, 3, 9], True], [[9, 4, 10], True], [[10, 5, 11], True], [[11, 6], True]]

            sage: ce = CNFEncoder(DIMACS(), B, cutting_number=4)
            sage: ce.split_xor([1,2,3,4,5,6], False)
            [[[1, 2, 7], False], [[7, 3, 4, 8], True], [[8, 5, 6], True]]

            sage: ce = CNFEncoder(DIMACS(), B, cutting_number=5)
            sage: ce.split_xor([1,2,3,4,5,6], False)
            [[[1, 2, 3, 7], False], [[7, 4, 5, 6], True]]
        """
    def clauses(self, f) -> None:
        """
        Convert ``f`` using the sparse strategy if ``f.nvariables()`` is
        at most ``max_vars_sparse`` and the dense strategy otherwise.

        INPUT:

        - ``f`` -- a :class:`sage.rings.polynomial.pbori.BooleanPolynomial`

        EXAMPLES::

            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: from sage.sat.converters.polybori import CNFEncoder
            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: fn = tmp_filename()
            sage: solver = DIMACS(filename=fn)
            sage: e = CNFEncoder(solver, B, max_vars_sparse=2)
            sage: e.clauses(a*b + a + 1)
            sage: _ = solver.write()
            sage: print(open(fn).read())
            p cnf 3 2
            -2 0
            1 0
            sage: e.phi
            [None, a, b, c]

            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: from sage.sat.converters.polybori import CNFEncoder
            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: fn = tmp_filename()
            sage: solver = DIMACS(filename=fn)
            sage: e = CNFEncoder(solver, B, max_vars_sparse=2)
            sage: e.clauses(a*b + a + c)
            sage: _ = solver.write()
            sage: print(open(fn).read())
            p cnf 4 7
            1 -4 0
            2 -4 0
            4 -1 -2 0
            -4 -1 -3 0
            4 1 -3 0
            4 -1 3 0
            -4 1 3 0

            sage: e.phi
            [None, a, b, c, a*b]
        """
    def __call__(self, F):
        """
        Encode the boolean polynomials in ``F`` .

        INPUT:

        - ``F`` -- an iterable of :class:`sage.rings.polynomial.pbori.BooleanPolynomial`

        OUTPUT: an inverse map int -> variable

        EXAMPLES::

            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: from sage.sat.converters.polybori import CNFEncoder
            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: fn = tmp_filename()
            sage: solver = DIMACS(filename=fn)
            sage: e = CNFEncoder(solver, B, max_vars_sparse=2)
            sage: e([a*b + a + 1, a*b+ a + c])
            [None, a, b, c, a*b]
            sage: _ = solver.write()
            sage: print(open(fn).read())
            p cnf 4 9
            -2 0
            1 0
            1 -4 0
            2 -4 0
            4 -1 -2 0
            -4 -1 -3 0
            4 1 -3 0
            4 -1 3 0
            -4 1 3 0

            sage: e.phi
            [None, a, b, c, a*b]
        """
    def to_polynomial(self, c):
        """
        Convert clause to :class:`sage.rings.polynomial.pbori.BooleanPolynomial`.

        INPUT:

        - ``c`` -- a clause

        EXAMPLES::

            sage: B.<a,b,c> = BooleanPolynomialRing()
            sage: from sage.sat.converters.polybori import CNFEncoder
            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: fn = tmp_filename()
            sage: solver = DIMACS(filename=fn)
            sage: e = CNFEncoder(solver, B, max_vars_sparse=2)
            sage: _ = e([a*b + a + 1, a*b+ a + c])
            sage: e.to_polynomial( (1,-2,3) )
            a*b*c + a*b + b*c + b
        """
